#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int x, y, z, t, xt = 0, yt = 0, zt = 0;
	cin >> t;
	while(--t + 1) {
	    cin >> x >> y >> z;
	    xt += x;
	    yt += y;
	    zt += z;
	}
	if (xt == yt && yt == zt && xt == 0){
		cout << "YES\n";
	} 
	else{
		cout << "NO\n";
	}

	return 0;
}