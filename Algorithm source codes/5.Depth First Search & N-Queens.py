def printMatrix(d):
    m = len(d)
    n = len(d[0])
    for i in range(0, m):
        for j in range(0, n):
            print("%4d" % d[i][j], end=" ")
        print()

e = {0:[1, 2, 3], 1:[2, 5], 2:[3, 4, 5, 6], 3:[4, 6], 4:[6, 7]}
n = 8
a = [[0 for j in range(0, n)] for i in range(0, n)] # a is an adjacency matrix. Here, the graph has no cost..so it only has two values 0 and 1. 0 means not connected and 1 means connected.
for i in range(0, n-1):
    for j in range(i+1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1
print("(1)") # indicates answer of first question.
printMatrix(a)

visited = n*[0]
def DFS(a, v):
    global b # set global variable b.
    visited[v] = 1 # Mark visited node as '1'.
    b.append(v) # append nodes to array b.
    for x in range(0, n):
        if a[v][x] == 1 and visited[x] == 0: # It means that if the node is connected to other nodes and if there is a node that didn't visit yet,
            DFS(a, x) # Run DFS.
b=[] # The empty array for adding nodes.
DFS(a, 0)
for m in range(0, len(b)): # I use this 'for' syntax for printing order and nodes.
    print(m+1, b[m]) # Here, 'm+1' means the order of nodes and b[m] means the nodes.
print(" ")


def promising(i, col):
    k = 0
    switch = True
    while k < i and switch == True:
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k: # check if the other queen is in same column or in the same diagonal.
            switch = False
        k += 1
    return switch

def queens(n, i, col):
    global count # set global variable count.
    if promising(i, col) == True:
        if i == n-1: # 'n-1' means the last order of column.
            count += 1 # when finished positioning queen, count the solution.
            if count == 3: # I have to show only third solution, so when the count is 3, print the solution.
                print("(2)") # indicates answer of second question.
                print("The 3rd solution :", col)
        else:
            for j in range(0, n):
                col[i+1] = j
                queens(n, i+1, col)
count = 0 # initiates count as 0.
n = 7
col = n*[0]
queens(n, -1, col)
print("The number of solutions :", count) # show the solutions of queens problem.


