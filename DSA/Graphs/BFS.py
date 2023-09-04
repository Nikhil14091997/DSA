#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        # starting node is V - this was the worng assumtion
        # V is the total number of nodes, starting node is 0
        # which is given in the question
        ret = []
        visited = []
        queue = []
        visited.append(V)
        queue.append(V)
        while queue:
            m = queue.pop(0)
            ret.append(m)
            for neighbour in adj[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return ret
            


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
        

# } Driver Code Ends