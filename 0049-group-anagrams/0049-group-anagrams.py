class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            count = str(count)
            if count not in res:
                res[count] = []
            res[count].append(s)
        return list(res.values())
        

