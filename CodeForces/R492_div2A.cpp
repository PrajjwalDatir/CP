#include<iostream>
#include<cmath>
using namespace std;

// 100 20 10 5 1
int main(int argc, char const *argv[])
{
	int n, ans=0;
	cin >> n;
    if(n>=100){
    	ans = int(n/100);
    	n = n%100; 
    }
    if(n>=20){
    	ans += int(n/20);
    	n = n%20;
    }
    if(n>=10){
    	ans += int(n/10);
    	n = n%10;
    }
    if(n>=5){
    	ans += int(n/5);
    	n = n%5;
    }
    if(n>=1){
    	ans += int(n);
    	n = n%1;
    }
    cout << ans << endl;
    return 0;
}