class MyHashSet:

    def __init__(self):
        self.list_set = []

    def add(self, key: int) -> None:
        if key not in self.list_set:
            self.list_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.list_set:
            self.list_set.remove(key)


    def contains(self, key: int) -> bool:
        if key in self.list_set:
            return True
        return False 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)