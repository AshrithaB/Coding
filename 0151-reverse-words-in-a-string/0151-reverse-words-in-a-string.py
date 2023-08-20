class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp = temp[::-1]
        return ' '.join(temp)