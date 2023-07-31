#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0
        result = 0
        substr = set()
        while r - l > result or r < len(s):
            if s[r] in substr:
                substr.remove(s[l])
                l += 1
                continue
            
            substr.add(s[r])
            r += 1
            result = max(result, len(substr))

        return result
        
# @lc code=end
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring(""))
print(solution.lengthOfLongestSubstring(" "))

