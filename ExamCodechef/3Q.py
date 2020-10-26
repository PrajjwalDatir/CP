# Python3 program to find minimum edge 
# between given two vertex of Graph 
import queue 
import sys
INT_MAX = sys.maxsize 



# function for finding minimum 
# no. of edge using BFS 
def minEdgeBFS(edges, u, v, n): 
	# u = source
    # v = destination
    # n = total nodes
	# visited[n] for keeping track 
	# of visited node in BFS 
	visited = [0] * n 

	# Initialize distances as 0 
	distance = [0] * n 

	# queue to do BFS. 
	Q = queue.Queue() 
	distance[u] = 0

	Q.put(u) 
	visited[u] = True
	while (not Q.empty()): 
		x = Q.get()
        if x == r:
            return distance[v]

		for i in range(len(edges[x])): 
			if (visited[edges[x][i]]): 
				continue

			# update distance for i 
			distance[edges[x][i]] = distance[x] + 1
			Q.put(edges[x][i]) 
			visited[edges[x][i]] = 1
	return distance[v] 

# function for addition of edge 
def addEdge(edges, u, v): 
	edges[u].append(v) 
	edges[v].append(u) 

# Driver Code 
# if __name__ == '__main__': 
def useless():
	# To store adjacency list of graph 
	n = 9
	edges = [[] for i in range(n)] 
	addEdge(edges, 0, 1) 
	addEdge(edges, 0, 7) 
	addEdge(edges, 1, 7) 
	addEdge(edges, 1, 2) 
	addEdge(edges, 2, 3) 
	addEdge(edges, 2, 5) 
	addEdge(edges, 2, 8) 
	addEdge(edges, 3, 4) 
	addEdge(edges, 3, 5) 
	addEdge(edges, 4, 5) 
	addEdge(edges, 5, 6) 
	addEdge(edges, 6, 7) 
	addEdge(edges, 7, 8) 
	u = 0
	v = 5
	print(minEdgeBFS(edges, u, v, n)) 

# This code is contributed by PranchalK 

# Driver Code 
if __name__ == "__main__": 
    T = int(input())
    for _ in range(T):
        N,M,K= map(int, input().split(" "))
        edges = [[] for i in range(N)] 

        for i in range(M):
            a,b = map(int, input().split(" "))
            addEdge(edges,a,b)
        portal = list(map(int, input().split(" ")))
        print(edges)
        # print("taking input")
        Q = int(input())
        for __ in range(Q):
            u = int(input())
            if u in portal:
                print("0")
            # Function call 
            else:
                for r in portal:
                    ans = INT_MAX
                    temp = minEdgeBFS(edges,u, r,N)
                    if temp < ans and temp != -1:
                        ans = temp
                print(ans)

