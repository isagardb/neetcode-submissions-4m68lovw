class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using HasSet
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# TC : O(N^2)
# SC : O(1)
        