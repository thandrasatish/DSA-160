def RotateArray(nums,n,d):
    nums[:d]=nums[:d][::-1]
    nums[d:]=nums[d:][::-1]
    nums=nums[::-1]
    return nums


n=int(input())
d=int(input())
nums=list(map(int,input().split()))
print(RotateArray(nums,n,d))