


# elementUI select

1.数组
```
const array1=[1,2,3]

<el-select v-model="seletValue">
   <el-option v-for="item in array1" :key="item" :value="item" :label="item">
   </el-option>
</el-select>
```

2.对象数组

```
const arrayOptions=[{version:0,name:'a'}}]

<el-select v-model="seletValue">
  <el-option v-for="item in arrayOptions" :key="item.version" :value="item.version" :label="item.name">
  </el-option>
</el-select>
```

3.对象

```
const options={0:'a',1:'b',2:'c',}

<el-select v-model="seletValue">
  <el-option v-for="(value,key) in  options" :key="key" :value="key" :label="item.value">
  </el-option>
</el-select>
```
