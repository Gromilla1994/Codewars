# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:       
        iter = 0
        for i in range(len(s)):
            if iter != "" and s[i] in t[iter:] and s.count(s[i]) <= t.count(s[i]):
                iter = t.find(s[i]) if iter - 1 < t.find(s[i]) else "" 
            else:
                return False
        return True


obj = Solution()
print(obj.isSubsequence("ab", "baab"))
print("a" in "baab")