#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	int t;
	cin >> t;
	while(--t + 1) {
	    int n;
	    cin >> n;
	    int a[n], count = 0;

	    for(int i = 0; i < n; i++) {
	        cin >> a[i];
	    }

	    long long int ans=0;
        for (int j=29; j>=0; j--)
        {
            long long int cnt=0;
            for (int i=0; i<n; i++)
            {
                if (a[i]>=(1<<j)&&a[i]<(1<<(j+1)))
                {
                    cnt++;
                }
            }
            ans+=cnt*(cnt-1)/2;
        }
        cout<<ans<<'\n';
	    }
	return 0;
}