#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[]) {
	int t, i;
	cin >> t;
	while(t--) {
		int n, m, k;
		cin >> n >> m >> k;
		vector<int> v[n + 1];
		for(i = 0; i < m; i++) {
			int x, y;
			cin >> x >> y;
			v[x].push_back(y);
			v[y].push_back(x);
		}
		int portals[k] = { 0 };
		for(i = 0; i < k; i++)
			cin >> portals[i];

		priority_queue< pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
		vector<int> distance(n + 1, INT_MAX);

		for(i = 0; i < k; i++) {
			pq.push(make_pair(0, portals[i]));
			distance[portals[i]] = 0;
		}

		while(!pq.empty()) {
			int x = pq.top().second;
			pq.pop();

			for(auto j = v[x].begin(); j != v[x].end(); j++) {
				int y = *j;

				if(distance[y] > (distance[x] + 1)) {
					distance[y] = distance[x] + 1;
					pq.push(make_pair(distance[y], y));
				}
			}
		}

		int q;
		cin >> q;
		while(q--) {
			int x;
			cin >> x;
			if(distance[x] == INT_MAX)
				cout << "-1" << endl;
			else
				cout << distance[x] << endl;
		}
	}
	return 0;
}