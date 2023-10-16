class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        h = len(letters)-1
        while l<=h:
            m = (l+h)//2
            if target == letters[m]:
                while m+1 < len(letters) and letters[m+1] == target:
                    m = m+1
                if m+1 < len(letters):
                    return letters[m+1]
                else:
                    return letters[0]
            elif letters[m] < target:
                l = m+1
            else:
                h = m-1
        return letters[l] if l > 0 and l < len(letters) else letters[0]
