def reverseArray(arr,d,n):
    d=d%n
    arr=arr[:d][::-1]+arr[d:][::-1]
    arr=arr[::-1]
    return arr


n = int(input())
arr=list(map(int,input().split()))
d=int(input())
arr1=reverseArray(arr,d,n)
for i in arr1:
    print(i,end=" ")