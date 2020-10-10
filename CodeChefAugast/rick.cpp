#include <bits/stdc++.h>
using namespace std;

int main(){

int t;
cin >> t;
while (t--)
{
    int n,k, num, kum;
    cin >> n >> k;

    if (n % 9 == 0) {
        num = n / 9;
        if (num == 0){
            num = 1;
        }
    } else {
        num = (n / 9) + 1;
    }
    if (k % 9 == 0) {
        kum = k / 9;
        if (kum == 0){
            kum = 1;
        }
    } else {
        kum = (k / 9) + 1;
    }

    if (num < kum) {
        cout << "0 " << num << endl;
    } else {
        cout << "1 " << kum << endl;
        /* code */
    }
}
}
