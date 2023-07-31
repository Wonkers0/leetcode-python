#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        longestSequence = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                seqLen = 1
                nextNum = num + 1
                while (nextNum in numSet):
                    seqLen += 1
                    nextNum += 1

                if(seqLen > longestSequence):
                    longestSequence = seqLen
        
        return longestSequence
        
# @lc code=end

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([]))
print(solution.longestConsecutive([-1,-2,-3,-8,-4]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
