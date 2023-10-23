class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0] * len(spells)
        potions.sort()
        for i in range(len(spells)):
            s = 0
            e = len(potions) 
            greater = (success + spells[i] - 1)//spells[i]
            while s < e:
                m = s+(e-s)//2
                if potions[m] >= greater:
                    e = m
                else:
                    s = m + 1
            pairs[i] = len(potions) - s
        return pairs