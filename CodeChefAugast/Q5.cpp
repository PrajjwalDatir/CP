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
	    ll n,k;
        cin>>n>>k;
        ll a[n+1];
        map<ll,ll>mp;
        ll ans=0,vc=0,t=1;
        for(int i=0;i<n;i++)
            cin>>a[i];
        ll col[n+1][n+1]={0};
        for(ll i=0;i<n;i++)
        {
            for(ll j=0;j<n;j++)
                col[i][j]=0;
        }
        for(int i=0;i<n;i++)
        {
            mp.clear();
            for(ll j=i;j<n;j++)
            {
                col[i][j]=(j==0)?0:col[i][j-1];
                if(mp.count(a[j]))
                {
                    if(mp[a[j]]==1)
                    {
                         col[i][j]++;
                    }
                    col[i][j]++;
                }
                mp[a[j]]++;

            }

        }
    
    ans=1e18;
    ll table=100;
    ll dp[101][1001]={0};
    for(int i=0;i<=table;i++)
    {
        for(int  j=0;j<=table;j++)
        {
            dp[i][j]=0;
        }
    }
    for(int i=0;i<n+1;i++)
        dp[1][i]=col[0][i-1];
    for(int i=2;i<=table;i++)
    {
        dp[i][1]=0;
    }
    for(int i=2;i<=table;i++)
    {
        for(int j=2;j<=n;j++)
        {
            ll best=1e18;
            for(int p=1;p<j;p++)
            {
                best=min(best,dp[i-1][p]+col[p][j-1]);
            }
            dp[i][j]=best;
        }
    }
    for(table =1;table<=100;table++)
    {
        ans=min(table*k+dp[table][n],ans);
    }
    cout<<ans<<"\n";

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