using namespace std;
#include<bits/stdc++.h>
#define ll long long
#define pb push_back 
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define all(x) x.begin(), x.end()
#define loopa(i,a,b) for (ll i=a; i<b; i++)
#define loopd(i,b,a) for (ll i=b; i>=a; i--)

//debugging
#define debug1(a) cout<<#a<<" = "<<(a)<<endl;
#define debug2(a,b) cout<<#a<<" = "<<(a)<<", "<<#b<<" = "<<(b)<<endl;
#define debug3(a,b,c) cout<<#a<<" = "<<(a)<<", "<<#b<<" = "<<(b)<<", "<<#c<<" = "<<(c)<<endl;
#define debug4(a,b,c,d) cout<<#a<<" = "<<(a)<<", "<<#b<<" = "<<(b)<<", "<<#c<<" = "<<(c)<<", "<<#d<<" = "<<(d)<<endl;

ll big = 1e+18+3;
ll mod = 1e+9+7;

void do_it(){
	string S,P;
    cin >> S >> P;
    string R = P;
    sort(P.begin(),P.end());
    sort(S.begin(),S.end());
    
    ll j = 0;
    
    int flg;
    ll e = 1;
    while(1){
        if(R[0] == R[e])
            e++;
        if(R[0] > R[e]){
            flg = 0;
            break;
        }
        if(R[0] < R[e]){
            flg = 1;
            break;
        }
    }   
    loopa(i,0,S.size()){
        if(S[i] == P[j]){
            S[i] = '@';
            j++;
        }
    }
    //cout << S << endl;
    vector<char> final;
    
    ll i = 0;
    for(; i < S.size(); i++){
        if(flg == 2){
            i--;
            break;
        }
        if(S[i] < R[0]){
           // cout << S[i] << endl;
            if(S[i] != '@')
                final.push_back(S[i]);
        }
        else if(S[i] == R[0]){
            if(flg == 0)
                flg = 2;
            else 
                final.push_back(S[i]);
        }
        else{
            if(flg == 1 && S[i] > R[0])
                flg = 2;
        }
    }
    string fin(final.begin(),final.end());
   // cout << fin << endl;
    R = fin + R;           
    final.clear();
    loopa(j,i,S.size()){
        if(S[j] != '@')
            final.push_back(S[j]);
    }
    string re(final.begin(),final.end());
    R = R + re;
    cout << R << endl;

}

int main() {
    fast;
    long T;
    cin >> T;
    while(T--){
        do_it();
    }
    return 0;
}