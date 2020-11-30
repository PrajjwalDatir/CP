#include <iostream>
#include <cmath> 
using namespace std;
int main(){
    double n , m, a;
    cin >> n >> m >> a;
    cout << (long long) ceil(n/a)* (long long) ceil(m/a) << endl; 
    /*
    |------------|
    |            |
    |            |
    |____________|
    */
    return 0;
}