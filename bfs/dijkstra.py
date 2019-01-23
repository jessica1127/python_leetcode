import heapq
import math

'''
reference: https://www.youtube.com/watch?v=9wV1VxlfBlI
'''
graph = {
    "A":{"B":5, "C":1},
    "B":{"A":5, "C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8, "D":3},
    "F":{"D":6}
}

def init_distance(graph, s):

    distance = {s:0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = float('inf')
    return distance

def dijkstra(graph, s):
    hqueue = []
    #0 is distance, s is the start point
    heapq.heappush(hqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while(len(hqueue) > 0):
        pair = heapq.heappop(hqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(hqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return parent, distance

parent, distance = dijkstra(graph, "A")
print parent
print "distance= ", distance

v = "E"
while v != None:
    print v
    v = parent[v]







