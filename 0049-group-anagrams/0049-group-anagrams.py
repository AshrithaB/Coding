class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            code = [0]*26
            for ch in s:
                code[ord(ch) - ord('a')] += 1
            hashmap[str(code)].append(s)
        return hashmap.values()