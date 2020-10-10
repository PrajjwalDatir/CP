#include<iostream>
#include<cmath>
using namespace std;

int main(int argc, char const *argv[])
{
	int t, fo = 0, th = 0, tw = 0, on = 0, temp = 0;
	cin >> t;
	while(--t + 1) {
	    /* code */
	    cin >> temp;
	    switch(temp){
	    	case 1:
	    		on += 1;
	    		break;
	    	case 2:
	    		tw += 1;
	    		break;
	    	case 3:
	    		th += 1;
	    		break;
	    	case 4:
	    		fo += 1;
	    		break;
	    }
	}
    // cout << on << tw << th << fo << "\n";
	t = fo;
	t += th;
	if (on > th){
		on -= th;
	}
	else{
		on = 0;
	}
	// cout << on << tw << "\n";
	t += tw/2;
	// cout << tw/2 << "\n";
	tw = tw%2 ? 1 : 0;
	// cout << tw << "\n";
	if (tw == 1){
		if(on >= 2)
			on -= 2;
		else{
			on = 0;
		}
		t += 1;
	}
	on = ceil(float(on)/float(4));

	t += on;
	cout << t << "\n";


	return 0;
}