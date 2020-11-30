#include <bits/stdc++.h>
using namespace std;
void sortString(string &str)
{
   sort(str.begin(), str.end());
   cout << str;
}
int main()
{
	std::ios::sync_with_stdio(false);
	int T;
	cin>>T;
	// cin.ignore(); must be there when using getline(cin, s)
	while(T--)
	{
        string s, p;
		cin >> s;
        cin >> p;
		int n = s.length(), m = p.length();
		char char_s[n];
		char char_p[m];
		strcpy(char_s, s.c_str());
		strcpy(char_p, p.c_str());
		sortString(char_s);
		for (int i = 0; i < n; i++) {
			/* code */
		}



	}
	return 0;
}
