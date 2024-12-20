#Link URL:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751


def secondLargest(nums):
    n=len(nums)

    secLar=-1
    lar = max(nums)
    for i in range(n):
        if(nums[i]<lar):
            secLar=max(secLar,nums[i])
    return secLar





t = int(input())
nums = list(map(int,input().split()))
print(f"Second Largest Number:{secondLargest(nums)}")
