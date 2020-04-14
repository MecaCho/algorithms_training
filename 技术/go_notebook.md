

# byte, rune, string

string存储unicode的话，如果有中文，按下标是访问不到的，因为你只能得到一个byte

总结：
rune 能操作 任何字符
byte 不支持中文的操作