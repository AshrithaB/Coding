class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = defaultdict()
 
    def set(self, index: int, val: int) -> None:
        if index not in self.arr:
            self.arr[index] = []
            self.arr[index].append([val, self.snap_id])
            return
        if self.snap_id == self.arr[index][-1][1]:
            self.arr[index][-1][0] = val
        else:
            self.arr[index].append([val, self.snap_id])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.arr:
            values = self.arr[index]
            l = 0
            h = len(values)-1
            while l <= h:
                m = (l + h)//2
                if values[m][1] <= snap_id:
                    l = m + 1
                else:
                    h = m - 1
            if -1 < h < len(values):
                return values[h][0]
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)