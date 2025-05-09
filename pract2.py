import heapq

def a_star(graph, start, goal):
    open_set = [(0,start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _,current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return [start] + path [::-1]
        
        for neighbor ,cost in graph[current].items():
            new_cost = g_score[current] + cost
            if new_cost < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_cost
                heapq.heappush(open_set,(new_cost,neighbor))
    return None

graph = {
    'A' : {'B':1,'C':4},
    'B' : {'A':1,'C':2, 'D':5},
    'C' : {'A':4,'B':2, 'D':1},
    'D' : {'B':3,'C':1}
}

path = a_star(graph,'A','D')
print('Path : ', path)