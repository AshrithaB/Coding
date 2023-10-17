class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            values = self.store[key]
            l = 0
            h = len(values)-1
            while l <= h:
                m = (l + h)//2
                if values[m][1] <= timestamp:
                    l = m + 1
                else:
                    h = m - 1
            if -1 < h < len(values):
                return values[h][0]
        return ""

 
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)