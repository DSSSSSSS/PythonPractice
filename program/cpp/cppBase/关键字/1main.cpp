#include<iostream>

#include"auto.cpp"
    int d()
{
    cout<<"This function shouldn't be called."<<endl;
    return 17;
}
using namespace std;
int main(int argc, char const *argv[])
{
    double v1=1.0,v2=2.0;
    auto v3 =v1+v2;
    

decltype(d()) dval17 = 15.2;
cout<<"test decltype:\n"<<dval17<<endl;

    return 0;
}
