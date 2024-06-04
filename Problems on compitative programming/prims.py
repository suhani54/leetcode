import heapq
def prim(graph,start):
    minimum_spanning_tree=[]
    visited=set()
    heap=[(0,start)]
    while heap:
        weight,vertex=heapq.heappop(heap)
        if vertex not in visited:
            visited.add(vertex)
            print(visited)
            print(graph[vertex])
            minimum_spanning_tree.append((weight,vertex))
            print(minimum_spanning_tree)
            for neighbor,neighbor_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap,(neighbor_weight,neighbor))

    return minimum_spanning_tree


graph={
    'A':[('B',7),('D',5)],
    'B':[('A',7),('C',8),('D',9),('E',7)],
    'C':[('B',8),('E',5)],
    'D':[('A',5),('B',9),('E',15),('F',6)],
    'E':[('B',7),('C',5),('D',15),('F',8)],
    'F':[('D',6),('E',8)]
}
start_vertex='A'
mst=prim(graph,start_vertex)
print("Minimum Spanning Tree")
min_spanning_tree_cost=0
for weight,vertex in mst:
    print(f"Edge:{start_vertex}-{vertex}Weight:{weight}")
    min_spanning_tree_cost+=weight
print("min_spanning_tree_cost=",min_spanning_tree_cost)
