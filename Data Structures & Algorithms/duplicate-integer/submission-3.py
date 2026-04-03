class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hash set length
        return len(set(nums)) < len(nums)

# TC : O(N)
# SC : O(N)
        