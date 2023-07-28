#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        letterCountS, letterCountT = {}, {}

        for i in range(len(s)):
            letterCountS[s[i]] = letterCountS.get(s[i], 0) + 1
            letterCountT[t[i]] = letterCountT.get(t[i], 0) + 1
        
        return letterCountS == letterCountT

        
        
# @lc code=end

