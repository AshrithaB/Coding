class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        sCount, pCount = [0]*26, [0]*26
        indices = []
        for j in range(len(p)):
            pCount[ord(p[j]) - ord('a')] += 1
            sCount[ord(s[j]) - ord('a')] += 1
        matches = 0    
        for i in range(26):
            matches += 1 if sCount[i] == pCount[i] else 0
        l = 0
        for r in range(len(p), len(s)):
            if matches == 26: indices.append(l)
            index = ord(s[r]) - ord('a')
            sCount[index] += 1
            if sCount[index] == pCount[index]:
                matches += 1
            elif pCount[index] + 1 == sCount[index]:
                matches -= 1
            index = ord(s[l]) - ord('a')
            sCount[index] -= 1
            if sCount[index] == pCount[index]:
                matches += 1
            elif pCount[index] - 1 == sCount[index]:
                matches -= 1
            l += 1
        if matches == 26: indices.append(l)
        return indices
        