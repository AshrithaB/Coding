class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        strnum = str(num)
        for l in range(len(strnum)-k+1):
            div = int(strnum[l:l+k])
            if div and num % div == 0:
                count += 1
        return count
        