# Depth-first
def kp(i, profit, weight):
    global bestset
    global maxp

    if weight <= W and profit > maxp: # This checks that whether itself is valid or whether profit is larger than maxp. 
        maxp = profit # Then profit should be maxp.
        bestset = include[:] # Copy the list using '[:]'. bestset list copies list include.

    if promising(i, weight, profit) == True:
        include[i+1] = 1 # Include the item.
        kp(i+1, profit+p[i+1], weight+w[i+1])
        include[i+1] = 0 # Exclude the item.
        kp(i+1, profit, weight)

def promising(i, weight, profit):
    global maxp

    if weight >= W: # Check if there is empty space.
        return False
    else:
        j = i+1
        bound = profit
        totweight = weight
        while j <= n-1 and totweight + w[j] <= W:
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1

        k = j
        if k <= n-1:
            bound += (W - totweight) * (p[k]//w[k])
        return bound > maxp

n = 4
W = 8
p = [48, 55, 16, 16]
w = [4, 5, 4, 8]
maxp = 0
include = [0, 0, 0, 0]
bestset = [0, 0, 0, 0]
kp(-1, 0, 0)
print("(1)")
print(maxp)
print(bestset)
print("")

# Best-first
import queue

class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include
    def __cmp__(self, other):
        return cmp(self.bound, other.bound)

def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n * [0]
    v = Node(-1, 0, 0, 0.0, temp)
    q = queue.PriorityQueue()
    v.bound = compBound(v)
    q.put((v.bound, v)) # Enqueue v. Here, v.bound means rank and v means item.

    while not q.empty():
        v.bound, v = q.get() # Dequeue v.
        if v.bound < maxProfit:
            u = Node(0, 0, 0, 0.0, temp)
            u.level = v.level + 1
            u.weight = v.weight + w[u.level] # Makes u children of v,which includes next item. Means 'include item.'
            u.profit = v.profit + p[u.level] # Same meaning above one.
            u.include = v.include[:] # u.include copies the list v.include.
            u.include[u.level] = 1 # Include item -> 1.
            u.bound = compBound(u)

            if u.weight <= W and u.profit > maxProfit: # If the solution is best so far.
                maxProfit = - u.profit
                bestset = u.include[:]

            if u.bound < maxProfit:
                q.put((u.bound, u))
            u = Node(0, 0, 0, 0.0, temp)
            u.weight = v.weight # Makes u children of v,which do not include next item. So, there is no change at weight and profit. Means 'Do not include item.'
            u.profit = v.profit
            u.include = v.include[:] # Also copy the list of v.
            u.level = v.level + 1
            u.bound = compBound(u)

            if u.bound < maxProfit:
                q.put((u.bound, u))

def compBound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight

        while j <= n-1 and totweight + w[j] <= W:
            totweight += w[j] # Item's weight.
            result += p[j] # Item's profit.
            j += 1

        k = j

        if k <= n-1:
            result += (W - totweight) * (p[k]//w[k]) # 'W-totweight' means the available space at Kth item, p[k]//w[k] means profit per weight.

        return (-result) # Here, we use minheap so when it completed its calculation, return minus value.

n = 4
W = 8
p = [48, 55, 16, 16]
w = [4, 5, 4, 8]
include = [0] * n
maxProfit = 0
bestset = n * [0]
kp_Best_FS()
print("(2)")
print(bestset)
print(maxProfit)
