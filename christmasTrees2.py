class GFG: 
    def __init__(self,graph): 
          
        # residual graph 
        self.graph = graph  
        self.rows = n
        self.columns = m
    # A DFS based recursive function 
    # that returns true if a matching  
    # for vertex u is possible 
    def bpm(self, u, matchR, seen): 
  
        # Try every column one by one 
        for v in range(self.columns): 
  
            # If row u can place table at  
            # column v and v is not seen 
            if self.graph[u][v] == 1 and seen[v] == False: 
                  
                # Mark v as visited 
                seen[v] = True 
  
                '''If column 'v' is not assigned to 
                   a row OR previously assigned  
                   row for column v (which is matchR[v])  
                   has an alternate column available.  
                   Since v is marked as visited in the  
                   above line, matchR[v]  in the following 
                   recursive call will not get column 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],  
                                               matchR, seen): 
                    matchR[v] = u 
                    return True
        return False
  
    # Returns maximum number of matching  
    def maxBPM(self): 
        '''An array to keep track of the  
           rows assigned to columns.  
           The value of matchR[i] is the  
           row number assigned to column i,  
           the value -1 indicates no row is assigned.'''
        matchR = [-1] * self.columns 
          
        # Count of columns assigned to rows 
        result = 0 
        for i in range(self.rows):  
            # Mark all columns as not seen for next row. 
            seen = [False] * self.columns 
            localResult = 0
            # Find if the row 'u' can get two columns 
            while (self.bpm(i, matchR, seen)): 
                localResult += 1
                result += 1
                if(localResult == 2): 
                    break
        return result 
  
# Read inputs
raw = input()
given_n_m = list(map(int, raw.split(' ')))
n = given_n_m[0]
m = given_n_m[1]
graph = []

# n = 4
# m = 8
# graph = []
# rows = [[1, 0], [5, 1, 2, 4, 5, 7], [5, 1, 2, 4, 5, 7], [3, 1, 3, 6]]

# Build graph
for i in range(n):
    raw = input()
    given_row = list(map(int, raw.split(' ')))
    # given_row = rows[i]
    mElements = [1]*(m)
    if given_row[0] > 0:
        for y in range(1, len(given_row)):
            treeIndex = given_row[y]
            mElements[treeIndex] = 0
    graph.append(mElements)

g = GFG(graph) 
print (g.maxBPM()) 
