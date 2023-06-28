class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            nums = list(str(x))
            i, j = 0, len(nums)-1
            while i <= j:
                if nums[i] != nums[j]:
                    return False
                i += 1
                j -= 1
            return True