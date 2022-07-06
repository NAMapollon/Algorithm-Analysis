def allShortestPath(g,n):
    i=0
    j=0
    k=0
    d=[[0 for i in range(n)] for j in range(n)] # n by n matrix.(column and row size is same.)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if g[i][j] > g[i][k] + g[k][j]: # k is the node located between i and j node, in this case i is the depart point and j is destination.
                    d[i][j] = k + 1 # matrix 'd' contains the cost, which generated when the nodes pass through each other.
                    g[i][j]=min(g[i][j],g[i][k]+g[k][j]) # choose the minimum number between two methods, and indicate the chosen method using matrix g.    
    return g,d
                

def path(p,q,r):
    if p[q-1][r-1]!= 0:
        path(p,q,p[q-1][r-1])
        print("v",p[q-1][r-1],end=" ")
        path(p,p[q-1][r-1],r)



def printMatrix(d):
    n=len(d[0]) # initiate n using length of matrix d, here d[0] means the first list of matrix d (matrix d consists of two lists.)
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()


inf=1000
g=[[0,1,inf,1,5],
   [9,0,3,2,inf],
   [inf,inf,0,4,inf],
   [inf,inf,2,0,3],
   [3,inf,inf,inf,0]]
d,p=allShortestPath(g,5) # the number of nodes = 5, g is a given matrix.
print()
printMatrix(d) # d is a matrix, which shows the cost.
print()
printMatrix(p) # p is a matrix,which shows the path that the nodes pass through.
path(p,5,3) # show the nodes between node 5 and 3,which represents the shortest path.
