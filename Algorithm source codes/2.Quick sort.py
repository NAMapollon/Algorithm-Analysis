def quickSort(s,low,high):

    pivotpoint=[0] # initiate the value of list 0, size is 1.(pass by reference.)

    if high>low:
        partition(s,low,high,pivotpoint)
        quickSort(s,low,pivotpoint[0]-1)
        quickSort(s,pivotpoint[0]+1,high)

def partition(s,low, high, pivotpoint):

    pivotitem=s[low]
    j=low

    for i in range(low+1,high+1): # range : low+1~high.
        if s[i]<pivotitem:
            j+=1
            s[i],s[j]=s[j],s[i] # exchange s[i] and s[j]

    pivotpoint[0]=j
    s[low],s[pivotpoint[0]] = s[pivotpoint[0]],s[low]

s=[3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print("(1)", s)


def prod2(a,b):
    n=max(len(str(a)),len(str(b)))

    if a==0 and b==0:
        return 0

    elif n<=4: # set threshold = 4.
        return a*b

    else:
        m = int(n/2)
        x = int(a/(10**m))
        y = int(a%(10**m))
        w = int(b/(10**m))
        z = int(b%(10**m))
        r = prod2(x+y,w+z)
        p = prod2(x,w)
        q = prod2(y,z)

        return int(p*(10**(2*m)) + (r-p-q)*(10**m) + q)

a=1234567812345678
b=2345678923456789

print("(2)", prod2(a,b)) # use function prod2.
print(a*b) # ordinary multiplication method.
