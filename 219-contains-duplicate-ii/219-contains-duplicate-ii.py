class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i, v in enumerate(nums):
            if v in hashMap and i - hashMap[v] <= k:
                return True
            hashMap[v] = i
        return False
        '''
        hashMap = {}
        for r in range(len(nums)):
            if nums[r] not in hashMap:
                hashMap[nums[r]] = r
            else:
                if r - hashMap[nums[r]] <= k:
                    return True
                else:
                    hashMap[nums[r]] = r
        return False
        '''
        