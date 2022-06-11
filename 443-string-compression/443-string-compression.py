class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        start, end, index = 0, 0, 0
        while end < len(chars):
            end = start
            while end<len(chars) and chars[start] == chars[end]:
                end += 1
            chars[index] = chars[start]
            index += 1
            if end-start > 1:
                num = list(str(end-start))
                for x in num:
                    chars[index] = x
                    index += 1
            start = end
        return index
            
            
        