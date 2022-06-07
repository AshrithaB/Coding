class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        match = 0
        for j in range(26):
            match += 1 if s1Count[j]==s2Count[j] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: 
                return True
            index = ord(s2[r])-ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                match += 1
            elif s2Count[index] == s1Count[index]+1:
                match -= 1
            index = ord(s2[l])-ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                match += 1
            elif s2Count[index]+1 == s1Count[index]:
                match -= 1
            l += 1
        return False if match != 26 else True
        