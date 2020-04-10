#!python 

def prims(G, startv):
    total_weight = 0
    selected = set([startv])
    for _ in range(len(G)-1):
        end = None
        start = None
        weight = 9999999 
        for startv in selected:
            for endv in G[startv]:
                if endv[1] < weight and endv[0] not in selected:
                    start, end, weight = startv, endv[0], endv[1]
        print('{0} to {1} = {2}'.format(start, end, weight))
        total_weight += weight
        selected.add(end)
    print('Total weight of the path:', total_weight)

if __name__ == "__main__":
    vertices = int(input('Enter the number of vertices: '))
    edges = int(input('Enter the number of edges:'))
    G = {}
    print('Enter the edges:  {start} {end} {weight}')
    for _ in range(edges):
        start, end, weight = map(int, input().split())
        if not G.get(start):
            G[start] = [(end, weight)]
        else:
            G[start].append((end, weight))
    startvertex = int(input('Enter start vertex:'))
    for vert in G.keys():
        print(vert, G[vert])
    prims(G, startvertex)



"""
OUTPUT
Enter the number of vertices: 7
Enter the number of edges:9
Enter the edges:  {start} {end} {weight}
1 2 28
2 3 16
3 4 12
4 5 22
5 6 25
6 1 10
2 7 19
7 5 24
7 4 12
Enter start vertex:1
1 [(2, 28)]
2 [(3, 16), (7, 19)]
3 [(4, 12)]
4 [(5, 22)]
5 [(6, 25)]
6 [(1, 10)]
7 [(5, 24), (4, 12)]
1 to 2 = 28
2 to 3 = 16
3 to 4 = 12
2 to 7 = 19
4 to 5 = 22
5 to 6 = 25
Total weight of the path: 122
"""