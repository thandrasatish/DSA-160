def secondLargest(nums,n):
    max_ele = max(nums)
    sec_ele=-1
    for i in range(n):
        if(nums[i]<max_ele):
            sec_ele = max(sec_ele,nums[i])
    return sec_ele


n=int(input())
nums=list(map(int,input().split()))
print(secondLargest(nums,n))