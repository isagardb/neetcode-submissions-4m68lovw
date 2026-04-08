class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0;
        hasData = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hasData:
                hasData.remove(s[l])
                l += 1
            hasData.add(s[r])
            res = max(res, r- l +1)
        return res