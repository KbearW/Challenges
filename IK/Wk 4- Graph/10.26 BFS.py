import collections

def number_of_connected_components(n, edges):
    # Write your code here
    # 1.) build a graph
    
    adjlist = [ [] for _ in range(n)]
    for (src, dst) in edges:
        adjlist[src].append(dst)
        adjlist[dst].append(src)
        
        # This is the short hand to create a visited array of [-1,-1,-1]
        visited = [-1] *n
        
    # def dfs(source):
    #     visited[source] = 1
    #     for neighbor in adjlist[source]:
    #         if visited[neighbor] == -1:
    #             dfs(neighbor)
                 
    def bfs(source):
        # This is use slice method to reassign visited[n] to 1 to in
        visited[source] = 1
        q = collections.deque([source])
        while len(q) != 0:
            node = q.popleft()
            for neighbor in adjlist[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    q.append(neighbor)
        
        # Count # of items 
    items = 0
    for v in range(n):
        if visited[v] == -1:
            items += 1
            # dfs(v)
            bfs(v)
    return items