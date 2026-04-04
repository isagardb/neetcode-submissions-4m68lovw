class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            hashmap[sortedStr].append(s)
        return list(hashmap.values())

        