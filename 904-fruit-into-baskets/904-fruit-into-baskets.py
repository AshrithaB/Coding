class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket, start, maxLen = {}, 0, 0
        for end in range(len(fruits)):
            if fruits[end] not in basket:
                basket[fruits[end]] = 1
            else:
                basket[fruits[end]] += 1
            if len(basket) < 3:
                maxLen = max(maxLen, end-start+1)
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    basket.pop(fruits[start])
                start += 1
        return maxLen