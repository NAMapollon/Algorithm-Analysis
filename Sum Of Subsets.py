# Sum of subsets
def promising(i, weight, total):
    return (weight+total >= W) and (weight == W or weight+S[i+1] <= W)

def s_s(i, weight, total, include):
    if promising(i, weight, total) == True:
        if weight == W:
            print ("sol", include)
        else:
            include[i+1] = 1
            s_s(i+1, weight+S[i+1], total-S[i+1], include) # Include S[i+1]
            include[i+1] = 0
            s_s(i+1, weight, total-S[i+1], include) # Exclude S[i+1]

n = 6
S = [1, 2, 3, 4, 5, 6] # Set list as 'S'.
S.sort()
W = 9
print("(1)")
print("items = ", S)
print("W = ", W)
include = n * [0]
total = 0
for k in S:
    total += k
s_s(-1, 0, total, include)
print(" ")

#M-coloring
def color(i, vcolor):
    if promising(i, vcolor) == True:
        if i == n-1: # The last index is 'n-1'.
            print(vcolor)
        else:
            for coloring in range(1, m+1):
                vcolor[i+1] = coloring
                color(i+1, vcolor)

def promising(i, vcolor):
    switch = True
    j = 0 # The first index is 0. So j indicates the first element.
    while j < i and switch:
        if W[i][j] and vcolor[i] == vcolor[j]: # 'W[i][j]' checks whether the nodes are connected each other and 'vcolor[i] == vcolor[j]' means whether the adjacent node has same color.
            switch = False
        j += 1
    return switch
n = 4
W = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vcolor = n * [0]
m = 3
print("(2)")
color(-1, vcolor)
