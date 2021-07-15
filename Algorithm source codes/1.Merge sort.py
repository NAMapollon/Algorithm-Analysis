def mergesort(n,S):
    global size  # set global variables
    global point
    h=n//2
    m=n-h

    if n==1: 
        point = False # We have to consider returning used spaces, so when the size of space is 1, do not need to add anymore.
        
    if n>1:
        U=S[:h]
        V=S[h:n]

        if point:
            size += len(U)+len(V) # add the two spaces

        mergesort(h,U)
        mergesort(m,V)
        merge(h,m,U,V,S)

        
        

def merge(h,m,U,V,S):
    i=0
    j=0
    k=0

    while i<h and j<m:
        if U[i]<V[j]: # U and V are sorted list. (It means the items of U is smaller than those of V.)
            S[k]=U[i] # Then, the items of U is added to list S.
            i+=1
        else: # Otherwise, U is right and V is left.
            S[k]=V[j] # Then, the items of V is added to list S.
            j+=1
        k+=1
    if i>=h: # when the index i is bigger than index of mid.(it means left list has finished.)
        S[k:h+m]=V[j:m] # When the while syntax finished, the other list is added to list S (In this case, after all of U's items added to S, then the rest of item in V added to S.)
    else:
        S[k:h+m]=U[i:h] # vice versa.

size = 0
point = True
S= [3,16,13,1,9,2,7,5,8,4,11,6,15,14,10,12] # given list.
mergesort(len(S),S)
print("mergesort :" , size) # print additional spaces
print(S)



def mergesort2(s,low,high):
    mid=0
    if low < high:
        mid = (low+high)//2
        mergesort2(s,low,mid) # merge from low to mid.
        mergesort2(s,mid+1,high) # merge from mid+1 to high.
        merge2(s,low,mid,high) 

   

def merge2(S,low,mid,high):
    global size1
    i=low
    j=mid+1
    k=0
    U=[0 for i in range(high-low+1)] # high-low+1 means the size of list
    size1 = max(size1, len(U)) # find the max size of U and it is the added space.
    while i<=mid and j<=high: # it means i is in the left side, and j is in the right side.
        if S[i] < S[j]: # compare the items in list S.
            U[k] = S[i] # Then, the smaller one is added to temporal list 'U'.
            i+=1
        else:
            U[k] = S[j]
            j+=1
        k+=1
    
    if i>mid:
        U[k:high-low+1]=S[j:high+1] # When one list completed adding to U list, the other list is added in this process.
    else:
        U[k:high-low+1]=S[i:mid+1]
    S[low:high+1] = U[0:high-low+1] # Finally, after completed adding all items to list U, copy the list U to list S.

    
size1=0
s= [3,16,13,1,9,2,7,5,8,4,11,6,15,14,10,12]
mergesort2(s,0,len(s)-1) # =(s, low, high)
print("mergesort2 :", size1)
print(s)







        
