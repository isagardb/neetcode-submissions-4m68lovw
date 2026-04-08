class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in seq:
                count = 0
                while n + count in seq:
                    count += 1 
                res = max(res, count)
        return res