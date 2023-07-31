#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) -1 

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            elif sum > target:
                r -= 1
        
# @lc code=end
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([2,3,4], 6))
