#include <bits/stdc++.h>
using namespace std;



int main(int argc, char const *argv[]) {
	int t, i;
	cin >> t;
	while(t--) {
		int n;
		cin >> n;
		vector<int> v[n + 1];
		for(i = 0; i < (n - 1); i++) {
			int x, y;
			cin >> x >> y;
			v[x].push_back(y);
			v[y].push_back(x);
		}

		stack<pair<int, int> > s;
		bool visited[n + 1] = { false };
		int j = 0;
		int maxnode = 0, maxval = -1;

		for(i = 1; i <= n; i++) {
			if(visited[i])
				continue;
			s.push(make_pair(i, 0));
			while(!s.empty()) {
				pair<int, int> p = s.top();
				s.pop();
				int x = p.first, wt = p.second;
				visited[x] = true;
				for(int j = 0; j < v[x].size(); j++) {
					if(visited[v[x][j]] == true)
						continue;
					s.push(make_pair(v[x][j], wt + 1));
					if(maxval < (wt + 1)) {
						maxval = wt + 1;
						maxnode = v[x][j];
					}
				}
			}
		}

		stack<pair<int, int> > news;
		bool newvisited[n + 1] = { false };
		j = 0;
		int oldd = maxnode;
		maxnode = 0;
		maxval = -1;
		news.push(make_pair(oldd, 0));
		while(!news.empty()) {
			pair<int, int> p = news.top();
			news.pop();
			int x = p.first, wt = p.second;
			newvisited[x] = true;
			for(int j = 0; j < v[x].size(); j++) {
				if(newvisited[v[x][j]] == true)
					continue;
				news.push(make_pair(v[x][j], wt + 1));
				if(maxval < (wt + 1)) {
					maxval = wt + 1;
					maxnode = v[x][j];
				}
			}
		}
		cout << (maxval + 1) / 2 << endl;

	}
	return 0;
}