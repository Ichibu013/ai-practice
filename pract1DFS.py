from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_tree(self,key,value):
        self.graph[key].append(value)

    def dfs_logic(self,value,visited):
        visited.add(value)
        print(value,end=' ')
        for key in self.graph[value]:
            if key not in visited:
                self.dfs_logic(key,visited)
    
    def dfs(self,value):
        visited = set()
        self.dfs_logic(value,visited)

if __name__ == '__main__':

    g = Graph()
    g.add_tree(0,1)
    g.add_tree(0,2)
    g.add_tree(1,2)
    g.add_tree(2,0)
    g.add_tree(2,3)
    g.add_tree(3,3)

    graph = g.graph
    print('Graph : ', graph)
    print('DFS starting for 2 :')
    g.dfs(1) 