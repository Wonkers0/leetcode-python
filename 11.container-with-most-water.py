#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        greatestArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > greatestArea:
                greatestArea = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return greatestArea
        
# @lc code=end
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))


