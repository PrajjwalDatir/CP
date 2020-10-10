

#include <bits/stdc++.h>
using namespace std;

// void shourya()
// {
//     ios_base::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);
// }


bool is_check(double a, double b ,double c, double p , double q, double r){
    double mod1 = long(a) % long(p);
    double mod2 = long(b) % long(q);
    double mod3 = long(c) % long(r);
    
    long div1 =a/p;
    long div2 =b/q;
    long div3 =c/r;
    
    if(mod1 == mod2 && mod2 == mod3 && div1 == div2 && div2 == div3)
        return true;
    else
        return false;
    
}

int no_of_opr(double a , double b ,double c, double p , double q, double r){
    int cnt;
    double diff[3] = {a-p, b-q, c-r};
	double divi[3] = {(a/p), (b/q),(c/r)};
	
	if((diff[0] == diff [1])&&(diff[1] == diff [2])){
	    if(diff[0] == 0)
	        cnt =  0;
	    else
	        cnt = 1;
	}
	else if((divi[0] == divi[1])&&(divi[1] == divi[2])){
	    if(divi[0] == 1)
	        cnt = 0;
	    else 
	        cnt =  1;
	}
	else if((divi[0] == divi[1]) || (divi[0] == divi[2]) || (divi[1] == divi[2])){
        if(divi[0] == 1 || divi[1] == 1 ||divi[2] == 1)
            cnt = 1;
        else
            cnt = 2;
    }
    else if((diff[0] == diff [1]) || (diff[0] == diff[2])|| (diff[1] == diff[2])){
        if(diff[0] == 0 || diff[1] == 0 || diff [2] == 0)
            cnt = 1;
        else
            cnt = 2;
    }
    else if(is_check(a,b,c,p,q,r))
        cnt =  2;
    else
        cnt = 3;
    return cnt;
}

int main() {
	// shourya();
	long T;
	cin >> T;
	
	while(T--){
	    long p,q,r,a,b,c;
	  
	    cin >> p >> q >> r >> a >> b >> c;

        a = double(a);
        b = double(b);
        c = double(c);
        p = double(p);
        q = double(q);
        r = double(r);
        
	    int cnt = no_of_opr( a, b, c, p, q, r);
        
        cout << cnt << endl;
	}
	return 0;
}