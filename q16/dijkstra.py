def creategraph(vertices):
    return [[0]*vertices for _ in range(vertices)]


def dijkstra(G, root, vertices):
    def _mindistance(distance, vertices, selected):
        mn = 10**8
        for v in range(vertices):
            if distance[v] < mn and v not in selected:
                mn = distance[v]
                min_idx = v
        return min_idx

    distance = [10**8]*vertices
    distance[root] = 0
    selected = set()
    for _ in range(vertices):
        u = _mindistance(distance, vertices, selected)
        selected.add(u)
        for v in range(vertices):
            if G[u][v] > 0 and v not in selected and distance[v] > distance[u]+G[u][v]:
                distance[v] = distance[u] + G[u][v]
    
    for i in range(vertices):
        print('From {} to {} -> {}'.format(root, i, distance[i]))



"""
vertices = int(input("enter number of vertices: "))
edges = int(input("enter number of edges: "))
G = creategraph(vertices)
print('Enter', edges, 'edges:')
print('eg: (vertex1 vertex2 weight)')
for _ in range(edges):
    s, e, w = map(int, input().split())
    G[s][e] = w

dijkstra(G, 0, vertices)

"""
G = [   [0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]
dijkstra(G, 0, 9)