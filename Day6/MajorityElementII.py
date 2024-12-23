# Link:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote

from collections import Counter
def MajorityElement(n,arr):
    new_freq_arr=[]
    freq= Counter(arr)
    for i,j in sorted(freq.items()):
        if(j>(n/3)):
            new_freq_arr.append(i)
    return new_freq_arr


n = int(input())
arr=list(map(int,input().split()))
new_arr = MajorityElement(n,arr)
for i in new_arr:
    print(i)
