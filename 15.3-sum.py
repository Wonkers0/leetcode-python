#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            firstNum = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + firstNum
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:                    
                    triplets.append([firstNum, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return triplets
        
# @lc code=end

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 1, 1]))
print(solution.threeSum([0, 0, 0]))