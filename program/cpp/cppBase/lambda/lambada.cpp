#include<iostream>
#include<algorithm>

using namespace std;
int main(int argc, char const *argv[])
{

    int test_data[] = {1, 5, 9, 7, 3, 19, 13, 17};
    int border = 8;
    auto f3 = [border](const int &i){ if(i > border) cout<<i<<'\t'; };
    for_each(begin(test_data), end(test_data), f3);
    cout<<endl;

    auto f4=[=](const int &i){ if(i > border) cout<<i<<'\t'; };
    auto f5=[&](const int &i){ if(i > border) cout<<i<<'\t'; };
    auto f7 = [&, border](const int &i){ if(i > border)  cout<<i<<'\t'; };
    return 0;
}
