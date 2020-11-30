#include <iostream>
#include <set>
using namespace std;
int main(int argc, char const *argv[])
{
	set<int> S;
	S.insert(1);
	S.insert(2);
	S.insert(-1);
	S.insert(-10);
	S.insert(5312);

	for (auto x : S)
	{
		cout << x << " ";
	}
	cout << endl;

	auto it = S.find(2);
	cout << *S.end();
	if(it == S.end()){
		cout << "not present\n";
	}
	else{
		cout << "present\n";
		cout << *it << endl;
	}
return 0;
}