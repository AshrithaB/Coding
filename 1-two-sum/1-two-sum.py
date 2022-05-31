class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            if target-n in hashMap.keys():
                return [hashMap[target-n], i]
            else:
                hashMap[n] = i