class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("infinity")
        store = {}
        l = 0
        for r in range(len(cards)):
            if cards[r] not in store:
                store[cards[r]] = r
            else:
                res = min(res, r-store[cards[r]]+1)
                store[cards[r]] = r
        return res if res != float("infinity") else -1