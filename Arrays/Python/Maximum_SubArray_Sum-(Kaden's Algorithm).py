def longest_sub_aary(nums):
    n = len(nums)
    result = nums[0]
    maxEnding = nums[0]

    for i in range(1,n):
        maxEnding = max(maxEnding+nums[i], nums[i])
        result = max(result,maxEnding)
    return result




nums1 = [2, 3, -8, 7, -1, 2, 3]
nums2 = [-2, -4]
nums3 = [5, 4, -1, 7, 8]
print(longest_sub_aary(nums1))
print(longest_sub_aary(nums2))
print(longest_sub_aary(nums3))