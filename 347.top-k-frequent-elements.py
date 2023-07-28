#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Keys: Numbers in `nums`
        # Values: Amount of occurences
        frequencyTable = {}

        for num in nums:
            frequencyTable[num] = frequencyTable.get(num, 0) + 1

        sortedFrequencyTable = sorted(frequencyTable.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for ind, x in enumerate(sortedFrequencyTable) if ind < k] 
        
# @lc code=end

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
print(solution.topKFrequent([-1, -1], 1))
