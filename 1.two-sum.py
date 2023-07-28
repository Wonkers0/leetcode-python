#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for index, value in enumerate(nums):
            otherFactor = target - value # Get the other number in the pair
            if otherFactor in seen: # Have we seen this number in the list before?
                return [seen[otherFactor], index]
            else:
                seen[value] = index # Map value to its index
        
# @lc code=end

