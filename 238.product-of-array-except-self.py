#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
def getOrDefault(arr, ind, default):
    try:
        return arr[ind] if ind >= 0 else default
    except:
        return default

class Solution(object):
    def productExceptSelf(self, nums):
        lastIndex = len(nums) - 1
        prefixes, suffixes = [None] * len(nums), [None] * len(nums)

        for i in range(len(nums)):
            prefixes[i] = nums[0] if i == 0 else nums[i] * prefixes[i - 1]

        for i in range(len(nums)):
            ind = lastIndex - i
            suffixes[ind] = nums[ind] if i == 0 else nums[ind] * suffixes[ind + 1]

        return [getOrDefault(prefixes, i - 1, 1) * getOrDefault(suffixes, i + 1, 1) for i in range(len(nums))]

# @lc code=end

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))