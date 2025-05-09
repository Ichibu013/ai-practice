from collections import deque

def bfs(adj,s):
    q = deque()

    visited = [False] * len(adj)

    visited[s] = True
    q.append(s)

    while q:
        current = q.popleft()
        print(current,end='')
        for u in adj[current]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

def add_edge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == '__main__':
    v = 5 

    adj = [[] for _ in range(v)]
    add_edge(adj,0,1)
    add_edge(adj,1,2)
    add_edge(adj,2,3)
    add_edge(adj,3,4)

    print('Graph',adj)

    print('BFS Staring from vertex : ')
    bfs(adj,0)