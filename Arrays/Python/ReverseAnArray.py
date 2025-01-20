def ReverseAnArray(nums,n):
    j=0
    m=n//2;
    for i in range(m):
        nums[i],nums[n-j-1]=nums[n-j-1],nums[i]
        j +=1
    return nums


n=int(input())
nums=list(map(int,input().split()))
print(ReverseAnArray(nums,n))