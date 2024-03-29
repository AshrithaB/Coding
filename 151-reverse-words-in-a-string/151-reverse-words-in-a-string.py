class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip(' ').split()
        i, j = 0, len(words)-1
        while i<j:
            words[i], words[j] = words[j], words[i]
            i, j = i+1, j-1
        return ' '.join(words)