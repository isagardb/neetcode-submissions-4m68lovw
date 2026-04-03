class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i , v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if v == nums[j]:
                    return True
        return False
        