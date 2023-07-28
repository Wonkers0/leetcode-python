#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prior = set()
        for num in nums:
            if num in prior:
                return True
            else:
                prior.add(num)
        
        return False
        
# @lc code=end

