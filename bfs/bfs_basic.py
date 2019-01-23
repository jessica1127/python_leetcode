def BFS(graph, s):
    # queue is first in first out
    queue = []
    queue.append(s)
    seen =[]
    seen.append(s)
    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.append(w)
        print vertex

def DFS(graph, s):
    #stack is first in last out
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while(len(stack)>0):
        tail = stack.pop()  #the last element of the stack
        nodes = graph[tail]
        for item in nodes:
            if item not in seen:
                stack.append(item)
                seen.add(item)
        print tail

def BFSShortesNode(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = { s: None}
    while(len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for item in nodes:
            if item not in seen:
                queue.append(item)
                seen.add(item)
                parent[item] = vertex
        #print vertex, 
    return parent


if __name__ == '__main__':
    graph = {
    "A":["B", "C"],
    "B":["A", "C","D"],
    "C":["A", "D", "E"],
    "D":["B", "C", "F"],
    "E":["C","D"],
    "F":["D"]
    }
    s = "A"
    #BFS(graph, s)
    #print "Below is DFS result: "
    #DFS(graph, s)
    parent = {}
    parent = BFSShortesNode(graph, "E")
    for key in parent:
        print key , parent[key]
    print "======"
    #suppose we want to go to B
    v = 'B'
    while v != None:
        print v
        v = parent[v]

