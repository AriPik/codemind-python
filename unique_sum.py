def findSum(arr,  n):
    # sort all elements of array
    arr.sort()
  
    sum = arr[0]
    for i in range(0,n-1):
        if (arr[i] != arr[i+1]):
            sum = sum + arr[i+1]
     
    return sum
n=int(input())
l=list(map(int,input().split()))[:n]
print(findSum(l,n))