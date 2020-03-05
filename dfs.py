g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : [],
      "g" : ["g"]
     }
    
    
cycles = 0
for node in g:
	for neighbour in g[node]:
		if neighbour == node:
			cycles += 1

print("Total Numbers of cycles = ", cycles)


def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated
    
iso = find_isolated_nodes(g)
if iso == []:
	print("Graphs are connected: ")
else :
	print("Graphs are not strongly connected")
