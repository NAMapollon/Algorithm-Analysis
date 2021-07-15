# Solve the given problem using method - 1.
import math
class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        self.n = len(self.data)-1 # Have to reduce heap size. So, index starts from 1 to available multiplication operation.

    def addElt(self, elt): # add elements.
        self.data.append(elt)
        self.n = len(self.data)-1 # adjust n.
        self.siftUp(self.n)

    def siftUp(self, i):
        while(i >= 2): # if i = 1, the node is max node so there is no other nodes to compare.
            if (self.data[i] > self.data[math.floor(i/2)]): # if bigger than parent's node,
                temp = self.data[math.floor(i/2)] # replace it using temp variable.
                self.data[math.floor(i/2)] = self.data[i] # by importing math module, use floor function.
                self.data[i] = temp
            i = math.floor(i/2) # update i.

    def siftDown(self, i):
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while (2 * parent <= self.n and spotfound == False):
            if (2 * parent < self.n and self.data[2 * parent] < self.data[(2 * parent) + 1]): # if bigger than parent's node,
                largerchild = (2 * parent) + 1 # replace it as 'largerchild'. In this case, largerchild is the right side of child node.
            else:
                largerchild = 2 * parent # Here, largerchild is the left side of child node.
            if siftkey < self.data[largerchild]:
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True
        self.data[parent] = siftkey

    def makeheap1(self): # Method - 1.
        s = [0] # set new list with 0.
        for i in range(0, self.n): # self.n means the size of heap.
            s.append(self.data[i]) # append the elements when they are entered as input.
            self.siftUp(i) # siftup the elements.

    def root(self): # check the max key and remove the key from root.
        keyout = self.data[1] # save key of root as keyout.
        self.data[1] = self.data[self.n] # move the key at the bottom node to root.
        del self.data[self.n] # delete the node.
        self.n = self.n-1
        if (self.n > 0):
            self.siftDown(1)
        return keyout

    def removekeys(self):
        s = []
        for i in range(self.n, 0, -1):
            a = self.root() # call the root and save it in 'a'.
            s.append(a) # and append it in list 's'.
        return s

def heapsort(a):
    a = Heap(a)
    a.makeheap1()
    s = a.removekeys()
    return s

a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = Heap(a)
b.makeheap1()
print(b.data)
s = heapsort(a)
print(s)
