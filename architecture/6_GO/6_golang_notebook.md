
# make-new

- make:

make也是用于内存分配的，但是和new不同，它只用于chan、map以及切片的内存创建，
而且它返回的类型就是这三个类型本身，而不是他们的指针类型，因为这三种类型就是引用类型，所以就没有必要返回他们的指针了。
注意，因为这三种类型是引用类型，所以必须得初始化，但是不是置为零值，这个和new是不一样的。
```
func make(t Type, size ...IntegerType) Type
```

- new:

它只接受一个参数，这个参数是一个类型，分配好内存后，返回一个指向该类型内存地址的指针。
同时请注意它同时把分配的内存置为零，也就是类型的零值。

```
// The new built-in function allocates memory. The first argument is a type,
// not a value, and the value returned is a pointer to a newly
// allocated zero value of that type.
func new(Type) *Type
```

二者都是内存的分配（堆上），但是make只用于slice、map以及channel的初始化（非零值；
而new用于类型的内存分配，并且内存置为零。所以在我们编写程序的时候，就可以根据自己的需要很好的选择了。

make返回的还是这三个引用类型本身；而new返回的是指向类型的指针。

# byte, rune, string

string存储unicode的话，如果有中文，按下标是访问不到的，因为你只能得到一个byte

总结：
rune 能操作 任何字符
byte 不支持中文的操作

# 值类型/引用类型

值类型分别有：int系列、float系列、bool、string、数组和结构体

引用类型有：指针、slice切片、管道channel、接口interface、map、函数等

值类型的特点是：变量直接存储值，内存通常在栈中分配

引用类型的特点是：变量存储的是一个地址，这个地址对应的空间里才是真正存储的值，内存通常在堆中分配