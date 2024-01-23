
#search element

def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

n = 4
arr = [1,2,3,4]
x = 3
print(search(arr,n,x))


#find min and max

def getMinMax( a, n):
    min = a[0]
    max = a[0]
    for i in range (1,n):
        if min > a[i]:
            min = a[i]
        if max < a[i]:
            max = a[i]
        i +=1
    return (min,max)
        
N = 6
A = [3, 2, 1, 56, 10000, 167]
print(getMinMax(A,N))

# rotate array

def leftrotate(arr,n,d):
    
    temp = []
    d = d % n
    for i in range(d):
        temp.append(arr[i])
    for j in range(n-d):
        arr[j] = arr[d+j]
    for m in range(n-d,n):
        arr[m] = temp[m-(n-d)]
    return arr
nums = [1,2,3,4,5]
n=5
d=4
ccc = leftrotate(nums,n,d)
print(ccc)