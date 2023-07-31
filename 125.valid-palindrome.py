#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            
            if s[l] != s[r] or l > r:
                return False
            else:
                l += 1
                r -= 1
        return True
        
# @lc code=end

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
print(solution.isPalindrome(".,"))