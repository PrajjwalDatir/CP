#include <bits/stdc++.h>
using namespace std;

int main(){

    int t;
    cin >> t;
    while (t--)
    {
        int n,k;
        cin >> n >> k;
        int p[n];
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        int mini = 0;
        int location = p[0];
        for (int i = 0; i < n; i++){
            if (k % p[i] == 0){
                if (mini == 0 || (k / p[i] < mini) ){
                    mini = k / p[i];
                    location = p[i];
                }
            }
        }
        if (mini == 0){
            cout << "-1" << endl;
        }
        else{
            cout << location << endl;
        }
    }
}
