class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = len(str1), len(str2)
        if s1 == s2:
            if str1 != str2:
                return ""
            return str1
        else:
            word = str1 if s1 < s2 else str2
            while word != "":
                flag = 0
                for i in range(0, s1, len(word)):
                    if str1[i:i+len(word)] != word:
                        flag = 1
                        break
                if not flag:
                    for i in range(0, s2, len(word)):
                        if str2[i:i+len(word)] != word:
                            flag = 1
                            break
                if not flag:
                    return word
                word = word[:-1]
        return ""