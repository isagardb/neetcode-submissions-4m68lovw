class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        # iterate each value and upddate the count
        for i, v in enumerate(nums):
            count[v] = 1 + count.get(v, 0)
        
        # iterate each key, val of dict and update the freq
        for n, c in count.items():
            freq[c].append(n)

        # now find the top k number. iterate from N-1 to 0
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        