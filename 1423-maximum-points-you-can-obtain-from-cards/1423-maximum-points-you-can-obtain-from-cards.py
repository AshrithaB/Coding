class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curSum = sum(cardPoints[-k:])
        maxSum = curSum
        l = 0
        for r in range(len(cardPoints)-k,len(cardPoints)):
            curSum = curSum + cardPoints[l] - cardPoints[r]
            maxSum = max(maxSum, curSum)
            l += 1
        return maxSum
        