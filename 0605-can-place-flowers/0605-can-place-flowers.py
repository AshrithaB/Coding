class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        f = len(flowerbed)
        if f % 2 == 0:
            maxplant = f / 2
        else:
            maxplant = (f+1) / 2
        if maxplant < (n + flowerbed.count(1)):
            return False
        else:
            flowerbed.insert(0, 0)
            flowerbed.append(0)
            l, r = 0, 3
            while r <= len(flowerbed):
                if flowerbed[l:r] == [0,0,0]:
                    flowerbed[l+1] = 1
                    n -= 1
                if not n:
                    return True
                l, r = l+1, r+1
            