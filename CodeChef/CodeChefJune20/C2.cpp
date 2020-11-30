
//C2.cpp
#include <iostream>
using namespace std;

int main(void){
	int test_cases, pair, mode = 0;
	char back, current;
	cin << test_cases;
	cin << back;
	for (int i = 1; i < test_cases; i++){
		while (!cin.eof())
		{
		cin << current;		
		if (mode == 1){
			mode = 0;
			continue;
		}
		else if (back != current){
			pair += 1;
			mode = 1;
		}
		back = current;
		}
		
	}
}