
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
# Read inputs
raw = input()
given_n_m = list(map(int, raw.split(' ')))
n = given_n_m[0]
m = given_n_m[1]
graph = []

# Sample data
# n = 4
# m = 8
# graph = []
# rows = [[1, 0], [5, 1, 2, 4, 5, 7], [5, 1, 2, 4, 5, 7], [3, 1, 3, 6]]

# Build graph
# First row elements from index 1 unitl n+1 are 2 else 0
fRow = [0]*(n+m+2) 
for i in range(1, n+1):
    fRow[i] = 2
graph.append(fRow)

# Build the next n rows 
firstNelements = [0]*(n+1)
for i in range(n):
    # given_row = rows[i]
    raw_row = input()
    given_row = list(map(int, raw_row.split(' ')))
    mElements = [1]*(m)
    if given_row[0] > 0:
        for y in range(1, len(given_row)):
            treeIndex = given_row[y]
            mElements[treeIndex] = 0
    row = firstNelements + mElements
    row.append(0)
    graph.append(row)

# Build the next m rows with n+m+1 0 and the last element 1
for i in range(m):
    tRow = [0]*(n+m+1)
    mRow = tRow + [1]
    graph.append(mRow)

# The last row is the sink with all elements as 0
lastRow = [0]*(n+m+2)
graph.append(lastRow)

# Main method
g = Graph(graph) 
source = 0
sink = n+m+1
print(graph)
print (g.FordFulkerson(source, sink)) 
