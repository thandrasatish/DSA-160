def MoveAllZerosToEnd(nums,n):
    j=0
    for i in range(n):
        if(nums[i]!=0):
            nums[i],nums[j]=nums[j],nums[i]
            j +=1
    return nums


n=int(input())
nums=list(map(int,input().split()))
print(MoveAllZerosToEnd(nums,n))