class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height)-1
        res = 0
        while l<r:
            if maxL < maxR:
                l += 1
                if maxL - height[l] > 0:
                    res += (maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                if maxR - height[r] > 0:
                    res += (maxR - height[r])
                maxR = max(maxR, height[r])    
        return res