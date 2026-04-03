class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lenght of the string are same
        if len(s) != len(t):
            return False
        # Load th hash map with the char

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT

# TC : O(N+M)
# SC : O(1)  since we have at most 26 different characters.
        
        

        