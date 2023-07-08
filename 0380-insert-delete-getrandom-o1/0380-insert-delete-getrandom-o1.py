import random 
class RandomizedSet:

    def __init__(self):
        self.random = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.random:
            return False
        self.random.add(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            self.size -= 1
            return True
        return False
        
    def getRandom(self) -> int:
        temp = random.randint(0, self.size-1)
        new = list(self.random)
        return new[temp]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()