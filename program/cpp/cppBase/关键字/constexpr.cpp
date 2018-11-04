
//C++11标准中新增constexpr用于声明常量表达式，
//编译器会验证此变量的值是否是一个常量表达式。

// constexpr还可以用于函数，constexpr函数是指能用于常量表达式的函数，它遵循以下几条约定：

// a.返回类型是字面值类型 
// b.形参类型是字面值类型 
// c.函数体中必须有且仅有一条return语句

constexpr int sz() { return 42; }
constexpr int new_sz(int cnt) { return sz() * cnt; }
constexpr int size = sz();
constexpr int nsize = new_sz(4);

#include<iostream>
int main(int argc, char const *argv[])
{
    
    return 0;
}
