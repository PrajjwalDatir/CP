#include <bits/stdc++.h>
using namespace std;

int main(){


    int t;
    cin >> t;
    while (t--)
    {
        int h,p;
        cin >> h >> p;
        while (h !=0 && p!=0)
        {
            if(h>p){
                h = h-p;
            }
            else{
                h = 0;
            }
            p/=2;
        }
        if (h){
            cout << 0 << endl;
        }
        else
        {
            cout << 1 << endl;
        }
        
        
    }
    
}
