#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	while(--t + 1) {
	    int n;
	    int prev=0, curr;
		int res = 1;
	    cin >> n;
	    while(--n + 1) {
	    	        cin >> curr;
	    	        if (!prev){
	    	        	prev = curr;
	    	        	continue;
	    	        }
	    	        else if( prev <= curr){
	    	        	res = 0;
	    	        }
	    	        else{
	    	        	prev = curr;
	    	        }
	    	    }
	    	if(!res){
	    	    // cout << res;
	    		cout << "YES\n";
	    	}
	    	else{
	    	    // cout << res;
	    		cout << "NO\n";
	    	}

	}
	return 0;
}