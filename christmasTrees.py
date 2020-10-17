
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self.ROW = len(graph) 
        #self.COL = len(gr[0]) 

    def BFS(self,s, t, parent): 

        # Mark all the vertices as not visited 
        visited =[False]*(self.ROW) 
            
        # Create a queue for BFS 
        queue=[] 
            
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
            
            # Standard BFS Loop 
        while queue: 

            #Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
            
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 

        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False

       # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
raw = input()
given_n_m = list(map(int, raw.split(' ')))
n = given_n_m[0]
m = given_n_m[1]
graph = []
    
# n = 4
# m = 8
# graph = []
# rows = [[1, 0], [5, 1, 2, 4, 5, 7], [5, 1, 2, 4, 5, 7], [3, 1, 3, 6]]
fRow = []
for i in range(n+m+2):
    if i > 0 and i<n+1:
        fRow.append(2)
    else:
        fRow.append(0) 
graph.append(fRow)

for i in range(n):
    raw_row = input()
    given_row = list(map(int, raw_row.split(' ')))
    tRow = []
    for x in range(n+m+2):
        if x > n and x < n+m+1:
            tRow.append(1)
        else:
            tRow.append(0)
    if len(given_row) > 0:
        for y in range(1, len(given_row)):
            treeIndex = given_row[y] + n + 1
            tRow[treeIndex] = 0
        graph.append(tRow)


for i in range(n+1, n+m+2):
    tRow = []
    for x in range(n+m+1):
        tRow.append(0)
    tRow.append(1)
    graph.append(tRow)
g = Graph(graph) 
source = 0
sink = n+m+1
print (g.FordFulkerson(source, sink)) 
