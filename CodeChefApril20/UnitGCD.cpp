# include<bits/stdc++.h>
# define limit 1000000007
# define ll long long
# define endl "\n"

using namespace std;
int main(){
	ios_base:: sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	while (t--){
		int n;
			cin >> n;
		if (n == 1){
			cout << "1" << "\n" << "1 " << "1" << "\n";
		continue;
		}
		else if (n == 2){
			cout << "1" << "\n" << "2 " << "1 2 " << "\n";
		continue;
		}
		else if (n == 3){
			cout << "1" << "\n" << "3" << "1 2 3 " << "\n";
		continue;
		}
		else if (n % 2 == 1){
		cout << floor(n / 2) << "\n";
		bool inc = true;
		cout << "3 " << "1 2 3 " << endl;
		for (int i = 4; i < n;i += 2){
    	cout << "2 " << i << " " << i + 1 << endl ;
		}
		continue;
		}
		else if (n % 2 == 0){
			cout << floor(n / 2) << "\n";
			cout << "3 " << "1 2 3 " << endl;
		for (int i = 4; i < n; i += 2){
    	cout << "2 " << i << " " << i + 1 << endl ;
		}
		cout << "1" << " " << n << endl;
		continue;
		}
	}
return 0;
}//this is an online IDE
