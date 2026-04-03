class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i , v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if  target - v == nums[j]:
                    return [i, j]
        return [0,0]


# TC : O(N^2)
# SC : O(1)
        
