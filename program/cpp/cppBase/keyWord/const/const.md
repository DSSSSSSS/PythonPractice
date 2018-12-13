# const

通过编译器来保证对象的常量性,对象的常量性可以分为两种：物理常量性（即每个bit都不可改变）和逻辑常量性（即对象的表现保持不变）。

## 1

```cpp
const int COMPILE_CONST = 10;
const int RunTimeConst = cin.get();
int a1[COMPLIE_CONST]; // ok in C++ and error in C
int a2[RunTimeConst]; // !error in C++

```

## 2

const变量默认是文件内可见的

```cpp
//a.cpp
extern const int M = 20;

//b.cpp
extern const int M;
```

## const修饰指针与引用

const修饰引用时，其意义与修饰变量相同。
顶层指针:int *const ptr;
底层指针:const int* prt;

