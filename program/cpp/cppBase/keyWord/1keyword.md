# cpp keyword

## decltype

```cpp
decltype(d()) dval17 = 15.2;//d() ->int
```

## auto

### 使用 auto 缩写类型

```cpp
string name = "Yubo";
auto length = name.size();
```

### 使用 auto 简化声明

```cpp
int val25[3][4] = {
    {0, 1, 2, 3},
    {4, 5, 6, 7},
    {8, 9, 10, 11}
};
cout<<"test auto to simplify type:\n";
cout<<"old way:\n";
for(int (*p)[4] = val25; p != val25 + 3; p++)
{
    for(int *q = *p; q != *p + 4; q++)
    {
        cout<<*q<<'\t';
    }
    cout<<'\n';
}
cout<<"new way:\n";
for(auto ap = val25; ap != val25 + 3; ap++)
{
    for(auto aq = *ap; aq != *ap + 4; aq++)
    {
        cout<<*aq<<'\t';
    }
    cout<<'\n';
}

```
