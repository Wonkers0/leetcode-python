#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = {}
        for anagram in strs:
            chars = list(anagram)
            chars.sort()

            sorted = "".join(chars)
            groups[sorted] = groups.get(sorted, []) + [anagram]
        
        return list(groups.values())
        
# @lc code=end

print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
