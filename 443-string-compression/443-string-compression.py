class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        start = index = end = 0
        while end < len(chars):
            end = start
            while end < len(chars) and chars[start] == chars[end]:
                end = end + 1
            chars[index] = chars[start]
            index += 1
            l = end-start
            if l > 1:
                l = str(l)
                for c in l:
                    chars[index] = c
                    index += 1
            start = end
        return index