class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        start = i = end = 0
        while end < len(chars):
            end = start
            while end < len(chars) and chars[start] == chars[end]:
                end += 1
            chars[i] = chars[start]
            i += 1
            count = end - start
            if count > 1:
                ch = str(count)
                for c in ch:
                    chars[i] = c
                    i += 1
            start = end
        return i