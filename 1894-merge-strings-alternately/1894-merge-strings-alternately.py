class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr = ''
        end = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(end):
            newstr = newstr + word1[i] + word2[i]
        i += 1
        if end != len(word1):
            newstr += word1[i:]
        else:
            newstr += word2[i:]
        return newstr