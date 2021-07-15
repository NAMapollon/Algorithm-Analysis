def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

def printMatrixF(d):
    n = len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print("%5.2f" % d[i][j],end=" ")
        print()

class Node:
    def __init__(self,data):
        self.l_child = None
        self.r_child = None
        self.data = data


def tree(key,r,i,j):
    k=r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child = tree(key,r,i,k-1)
        p.r_child = tree(key,r,k+1,j)
        return p

key = [" ","A","B","C","D","E"]
p = [0, float(4/15), float(5/15), float(1/15), float(3/15), float(2/15)]

#Optsearch using a,r
def optsearchtree(p):
    n = len(p)-1
    a = [[0 for j in range(0,n+2)] for i in range(0,n+2)]
    r = [[0 for j in range(0,n+2)] for i in range(0,n+2)]
    

    for i in range(1,n+1):
        a[i][i] = p[i] # probability of i.
        r[i][i] = i # i root.

    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1): # i in range 1~n-diagonal.
            j = i+diagonal
            minv = 9999 # indicate minimum value.
            
            for k in range(i,j+1):
                if(a[i][k-1]+a[k+1][j])<minv:
                    minv = a[i][k-1]+a[k+1][j] # replace minimum value.
                    mink = k
            
            sum_ = 0
            for m in range(i,j+1):
                sum_ = sum_+p[m] # summation of p[m] in range i~j.
                
            a[i][j] = minv + sum_ #minv = a[i][k-1]+a[k+1][j].
            r[i][j] = mink # k is a value, which gives the minimum value.
            
    return a,r

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


print("(1)"," ")    
a,r = optsearchtree(p)
printMatrixF(a)
print()
printMatrix(r)

n = len(p)-1
root = tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)
print("\n")


####################################################################

a = ['A','A','C','A','G','T','A','C','C']
b = ['T','A','C','G','T','T','C','A']

def DNA_alignment(a, b): # set a function as 'DNA_alignment'.
    m = len(a)
    n = len(b)
    table = [[0 for j in range(0,n+1)] for i in range(0,m+1)]
    minindex = [[(0,0) for j in range(0,n+1)] for i in range(0,m+1)]

    for j in range(n-1,-1,-1): #  y axis.
        table[m][j] = table[m][j+1]+2 

    for i in range(m-1,-1,-1): # x axis.
        table[i][n] = table[i+1][n]+2

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            penalty = 0 # set penalty = 0.
            if a[i] != b[j]:
                penalty = 1 # penalty = 1, when a[i] and b[j] is diffrent.
            table[i][j] = table[i+1][j+1] + penalty # this case, penalty = 1.
            minindex[i][j] = (i+1, j+1) # same meaning : minindex[i][j] = minindex[i+1][j+1].

            if table[i][j] > table[i+1][j]+2: 
                table[i][j] = table[i+1][j]+2 # update table[i][j] as a optimistic cost.
                minindex[i][j] =(i+1, j) # also update minindex.

            if table[i][j] > table[i][j+1]+2: # vice versa.
                table[i][j] = table[i][j+1]+2
                minindex[i][j] = (i, j+1)
    return table, minindex    

print("(2)"," ")
table, minindex = DNA_alignment(a, b)                
printMatrix(table)

x = 0
y = 0
m = len(a)
n= len(b)

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x,y)=minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx]," ",b[ty])
    elif x == tx and y == ty + 1:
        print(" - ", " ", b[ty] )
    else:
        print(a[tx]," "," - ")
    


































    

    









