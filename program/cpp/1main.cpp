//GBK
#include<iostream>
#include<vector>
//#include"auto.cpp"
#include"cppBase/keyWord/auto.cpp"
#include<memory>
#include<string>

#include"cppPractice\Ä£Ê½\singleMode.cpp"
using namespace std;

void process(shared_ptr<int> ptr)
{
    cout<<"in process use_count:"<<ptr.use_count()<<endl;
}

int main(int argc, char const *argv[])
{
    double v1=1.0,v2=2.0;
    auto v3 =v1+v2;
    
    vector<int> v ={1,2,3,4,5};

    
    int *p6 = new int(1024);
    process(shared_ptr<int>(p6));
    int v6 = *p6;
    cout<<"v6: "<<v6<<endl;
    string str = "ÄãºÃ";
    cout<<str<<endl;
    system("pause");
    return 0;
}
