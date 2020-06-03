

赋值的时候会触发扩容吗？
负载因子是什么？过高会带来什么问题？它的变动会对哈希表操作带来什么影响吗？
溢出桶越多会带来什么问题？
是否要扩容的基准条件是什么？
扩容的容量规则是怎么样的？
扩容的步骤是怎么样的？涉及到了哪些数据结构？
扩容是一次性扩容还是增量扩容？
正在扩容的时候又要扩容怎么办？
扩容时的迁移分流动作是怎么样的？
在扩容动作中，底层汇编承担了什么角色？做了什么事？
在 buckets/overflow buckets 中寻找时，是如何 “快速” 定位值的？低八位、高八位的用途？
空槽有可能出现在任意位置吗？假设已经没有空槽了，但是又有新值要插入，底层会怎么处理

# map

Golang中map的底层实现是一个散列表，因此实现map的过程实际上就是实现散表的过程。
在这个散列表中，主要出现的结构体有两个，
一个叫hmap(a header for a go map)，
一个叫bmap(a bucket for a Go map，通常叫其bucket)

Golang的map中用于存储的结构是bucket数组

低位用于寻找当前key属于hmap中的哪个bucket，
而高位用于寻找bucket中的哪个key。
bucket中有个属性字段是“高位哈希值”数组，这里存的就是蓝色的高位值，
用来声明当前bucket中有哪些“key”，便于搜索查找。

## map基本数据结构

map的底层结构是hmap，核心元素是一个由若干个bucket（结构为bmap），
每个bucket可以存放8个元素，key通过哈希算法被归入不同的bucket；
当超过8个元素需要存入某个bucket时，hmap会使用extra中的overflow来扩展bucket；

```
// A header for a Go map.
type hmap struct {
	// Note: the format of the hmap is also encoded in cmd/compile/internal/gc/reflect.go.
	// Make sure this stays in sync with the compiler's definition.
	count     int // 元素个数；# live cells == size of map.  Must be first (used by len() builtin)
	flags     uint8
	B         uint8  // 包含2^B个bucket，log_2 of # of buckets (can hold up to loadFactor * 2^B items)
	noverflow uint16 // 溢出的bucket个数；approximate number of overflow buckets; see incrnoverflow for details
	hash0     uint32 // hash种子；hash seed

	buckets    unsafe.Pointer // buckets的数组指针；array of 2^B Buckets. may be nil if count==0.
	oldbuckets unsafe.Pointer // 结构扩容时用于复制的buckets数组；previous bucket array of half the size, non-nil only when growing
	nevacuate  uintptr        // 已经搬迁的buckets数量；progress counter for evacuation (buckets less than this have been evacuated)

	extra *mapextra // optional fields
}
```


extra包括overflow、oldoverflow、nextOverflow

```
// mapextra holds fields that are not present on all maps.
type mapextra struct {
	// If both key and elem do not contain pointers and are inline, then we mark bucket
	// type as containing no pointers. This avoids scanning such maps.
	// However, bmap.overflow is a pointer. In order to keep overflow buckets
	// alive, we store pointers to all overflow buckets in hmap.extra.overflow and hmap.extra.oldoverflow.
	// overflow and oldoverflow are only used if key and elem do not contain pointers.
	// overflow contains overflow buckets for hmap.buckets.
	// oldoverflow contains overflow buckets for hmap.oldbuckets.
	// The indirection allows to store a pointer to the slice in hiter.
	overflow    *[]*bmap
	oldoverflow *[]*bmap

	// nextOverflow holds a pointer to a free overflow bucket.
	nextOverflow *bmap
}
```

bucket结构：

tophash用于记录8个key哈希值的高8位，

kv的存储形式为”key0key1key2key3…key7val1val2val3…val7″
而不是key/elem/key/elem/...，可以在key和value的长度不同的时候，节省padding空间

```
// A bucket for a Go map.
type bmap struct {
	// tophash generally contains the top byte of the hash value
	// for each key in this bucket. If tophash[0] < minTopHash,
	// tophash[0] is a bucket evacuation state instead.
	tophash [bucketCnt]uint8
	// Followed by bucketCnt keys and then bucketCnt elems.
	// NOTE: packing all the keys together and then all the elems together makes the
	// code a bit more complicated than alternating key/elem/key/elem/... but it allows
	// us to eliminate padding which would be needed for, e.g., map[int64]int8.
	// Followed by an overflow pointer.
}
```

## map的访问

```
// mapaccess1 returns a pointer to h[key].  Never returns nil, instead
// it will return a reference to the zero object for the elem type if
// the key is not in the map.
// NOTE: The returned pointer may keep the whole map live, so don't
// hold onto it for very long.
func mapaccess1(t *maptype, h *hmap, key unsafe.Pointer) unsafe.Pointer {
	if raceenabled && h != nil {
		callerpc := getcallerpc()
		pc := funcPC(mapaccess1)
		racereadpc(unsafe.Pointer(h), callerpc, pc)
		raceReadObjectPC(t.key, key, callerpc, pc)
	}
	if msanenabled && h != nil {
		msanread(key, t.key.size)
	}
	if h == nil || h.count == 0 {
		if t.hashMightPanic() {
			t.key.alg.hash(key, 0) // see issue 23734
		}
		return unsafe.Pointer(&zeroVal[0])
	}
	if h.flags&hashWriting != 0 {
		throw("concurrent map read and map write")
	}
	alg := t.key.alg
	hash := alg.hash(key, uintptr(h.hash0))
	m := bucketMask(h.B)
	b := (*bmap)(add(h.buckets, (hash&m)*uintptr(t.bucketsize)))
	if c := h.oldbuckets; c != nil {
		if !h.sameSizeGrow() {
			// There used to be half as many buckets; mask down one more power of two.
			m >>= 1
		}
		oldb := (*bmap)(add(c, (hash&m)*uintptr(t.bucketsize)))
		if !evacuated(oldb) {
			b = oldb
		}
	}
	top := tophash(hash)
bucketloop:
	for ; b != nil; b = b.overflow(t) {
		for i := uintptr(0); i < bucketCnt; i++ {
			if b.tophash[i] != top {
				if b.tophash[i] == emptyRest {
					break bucketloop
				}
				continue
			}
			k := add(unsafe.Pointer(b), dataOffset+i*uintptr(t.keysize))
			if t.indirectkey() {
				k = *((*unsafe.Pointer)(k))
			}
			if alg.equal(key, k) {
				e := add(unsafe.Pointer(b), dataOffset+bucketCnt*uintptr(t.keysize)+i*uintptr(t.elemsize))
				if t.indirectelem() {
					e = *((*unsafe.Pointer)(e))
				}
				return e
			}
		}
	}
	return unsafe.Pointer(&zeroVal[0])
}
```

## map的扩容    

```
func hashGrow(t *maptype, h *hmap) {
	// If we've hit the load factor, get bigger.
	// Otherwise, there are too many overflow buckets,
	// so keep the same number of buckets and "grow" laterally.
	bigger := uint8(1)
	if !overLoadFactor(h.count+1, h.B) {
		bigger = 0
		h.flags |= sameSizeGrow
	}
	oldbuckets := h.buckets
	newbuckets, nextOverflow := makeBucketArray(t, h.B+bigger, nil)

	flags := h.flags &^ (iterator | oldIterator)
	if h.flags&iterator != 0 {
		flags |= oldIterator
	}
	// commit the grow (atomic wrt gc)
	h.B += bigger
	h.flags = flags
	h.oldbuckets = oldbuckets
	h.buckets = newbuckets
	h.nevacuate = 0
	h.noverflow = 0

	if h.extra != nil && h.extra.overflow != nil {
		// Promote current overflow buckets to the old generation.
		if h.extra.oldoverflow != nil {
			throw("oldoverflow is not nil")
		}
		h.extra.oldoverflow = h.extra.overflow
		h.extra.overflow = nil
	}
	if nextOverflow != nil {
		if h.extra == nil {
			h.extra = new(mapextra)
		}
		h.extra.nextOverflow = nextOverflow
	}

	// the actual copying of the hash table data is done incrementally
	// by growWork() and evacuate().
}
```

当以上的哈希表增长的时候，Go语言会将bucket数组的数量扩充一倍，
产生一个新的bucket数组，并将旧数组的数据迁移至新数组

### 加载因子    

判断扩充的条件，就是哈希表中的加载因子(即loadFactor)。

加载因子是一个阈值，一般表示为：散列包含的元素数 除以 位置总数。
是一种“产生冲突机会”和“空间使用”的平衡与折中：加载因子越小，说明空间空置率高，空间使用率小，
但是加载因子越大，说明空间利用率上去了，但是“产生冲突机会”高了。

每种哈希表的都会有一个加载因子，数值超过加载因子就会为哈希表扩容。
Golang的map的加载因子的公式是：

map长度 / 2^B
阈值是6.5。其中B可以理解为已扩容的次数。

当Go的map长度增长到大于加载因子所需的map长度时，Go语言就会将产生一个新的bucket数组，
然后把旧的bucket数组移到一个属性字段oldbucket中。
注意：并不是立刻把旧的数组中的元素转义到新的bucket当中，而是，只有当访问到具体的某个bucket的时候，
会把bucket中的数据转移到新的bucket中。

扩容时map并不会立即把新数据做迁移，而是当访问原来旧bucket的数据的时候，才把旧数据做迁移，

并不会直接删除旧的bucket，而是把原来的引用去掉，利用GC清除内存。

```
func growWork(t *maptype, h *hmap, bucket uintptr) {
	// make sure we evacuate the oldbucket corresponding
	// to the bucket we're about to use
	evacuate(t, h, bucket&h.oldbucketmask())

	// evacuate one more oldbucket to make progress on growing
	if h.growing() {
		evacuate(t, h, h.nevacuate)
	}
}
```

## map中数据的删除

1、如果key是一个指针类型的，则直接将其置为空，等待GC清除；

2、如果是值类型的，则清除相关内存。

3、同理，对value做相同的操作。

4、最后把key对应的高位值对应的数组index置为空。

删除map中的元素不会释放内存，仅将对应的tophash[i]设置为empty，并非释放内存；


# sync.Map

Go 1.6之前， 内置的map类型是部分goroutine安全的，并发的读没有问题，
并发的写可能有问题。
自go 1.6之后， 并发地读写map会报错，这在一些知名的开源库中都存在这个问题，
所以go 1.9之前的解决方案是额外绑定一个锁，封装成一个新的struct或者单独使用锁都可以。

空间换时间。
通过冗余的两个数据结构(read、dirty),实现加锁对性能的影响。
使用只读数据(read)，避免读写冲突。
动态调整，miss次数多了之后，将dirty数据提升为read。
double-checking。

延迟删除。 
删除一个键值只是打标记，只有在提升dirty的时候才清理删除的数据。
优先从read读取、更新、删除，因为对read的读取不需要锁。

sync.Map是通过冗余的两个数据结构(read、dirty),实现性能的提升。
为了提升性能，load、delete、store等操作尽量使用只读的read；
为了提高read的key击中概率，采用动态调整，将dirty数据提升为read；
对于数据的删除，采用延迟标记删除法，只有在提升dirty的时候才删除。

```
type Map struct {
    // 当涉及到dirty数据的操作的时候，需要使用这个锁
    mu Mutex

    // 一个只读的数据结构，因为只读，所以不会有读写冲突。
    // 所以从这个数据中读取总是安全的。
    // 实际上，实际也会更新这个数据的entries,如果entry是未删除的(unexpunged), 并不需要加锁。如果entry已经被删除了，需要加锁，以便更新dirty数据。
    read atomic.Value // readOnly

    //包含最新的写入的数据，并且在写的时候，会把read 中未被删除的数据拷贝到该dirty中，因为是普通的map存在并发安全问题，需要用到上面的mu字段。

    // dirty数据包含当前的map包含的entries,它包含最新的entries(包括read中未删除的数据,虽有冗余，
    //但是提升dirty字段为read的时候非常快，不用一个一个的复制，而是直接将这个数据结构作为read字段的一部分),有些数据还可能没有移动到read字段中。
    // 对于dirty的操作需要加锁，因为对它的操作可能会有读写竞争。
    // 当dirty为空的时候， 比如初始化或者刚提升完，下一次的写操作会复制read字段中未删除的数据到这个数据中。
    dirty map[interface{}]*entry

    // 当从Map中读取entry的时候，如果read中不包含这个entry,会尝试从dirty中读取，这个时候会将misses加一，
    // 当misses累积到 dirty的长度的时候， 就会将dirty提升为read,避免从dirty中miss太多次。因为操作dirty需要加锁。
    misses int
}
```