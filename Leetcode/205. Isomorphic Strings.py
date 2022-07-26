# Given two strings s and t, determine if they are isomorphic.  Two strings s and t are isomorphic if
# the characters in s can be replaced to get t.  All occurrences of a character must be replaced
# with another character while preserving the order of characters. No two characters may map to the same character,
# but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s, hash_t = {}, {}
        arr_s, arr_t = [], []
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = str(i)
            arr_s.append(hash_s[s[i]])

        for i in range(len(t)):
            if t[i] not in hash_t:
                hash_t[t[i]] = str(i)
            arr_t.append(hash_t[t[i]])

        if arr_s == arr_t:
            return True
        return False


sol = Solution()

print(sol.isIsomorphic("title", "paper"))
