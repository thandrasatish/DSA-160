# Reverse an Array:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array


def reverseAnArray(arr):
    n1=len(arr)
    n2=n1/2
    i=0
    while(i<n2):
        arr[i],arr[n1-i-1]= arr[n1-i-1],arr[i]
        i+=1



n = int(input())
arr = list(map(int ,input().split()))
reverseAnArray(arr)
for i in arr:
    print(i,end=" ")