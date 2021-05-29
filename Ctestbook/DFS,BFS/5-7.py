#graph - list
#node-0,1,2 edge- 0,1:7 0,2:5

'''
graph=[]
for i in range(3):
    graph.append([])
'''
graph=[[] for i in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)