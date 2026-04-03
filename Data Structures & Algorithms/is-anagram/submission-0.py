class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lenght of the string are same
        if len(s) != len(t):
            return False
        # Sort both string and compare if its same
        return sorted(s) == sorted(t)

# TC : O(NlogN + MlogM)
# SC : O(N+M) 
        
        

        