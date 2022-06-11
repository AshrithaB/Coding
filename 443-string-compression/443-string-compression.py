class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        start, end, c = 0, 0, 0
        while end<len(chars):
            start = end
            while end<len(chars)-1 and chars[end] == chars[end+1]:
                end += 1
            l = end-start+1
            chars[c] = chars[start]
            c += 1
            if l>9:
                num = list(str(l))
                for x in num:
                    chars[c] = x
                    c += 1
            elif l<10 and l>1:
                chars[c] = str(l)
                c += 1
            end += 1
        return c
            
            
        