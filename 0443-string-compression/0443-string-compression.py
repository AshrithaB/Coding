class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = ["", 0]
        for j in range(len(chars)):
            if res[0] == "":
                res[0] = chars[j]
                res[1] += 1
            elif res[0] == chars[j]:
                res[1] += 1
            else:
                chars[i] = res[0]
                i += 1
                if 10 > res[1] > 1:
                    chars[i] = str(res[1])
                    i += 1
                elif res[1] > 9:
                    temp = list(str(res[1]))
                    for t in temp:
                        chars[i] = t
                        i += 1
                res = [chars[j], 1]
        chars[i] = res[0]
        i += 1
        if 10 > res[1] > 1:
            chars[i] = str(res[1])
            i += 1
        elif res[1] > 9:
            temp = list(str(res[1]))
            for t in temp:
                chars[i] = t
                i += 1
        return i
