class DNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def _remove(self, node:Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add_to_head(self, node:Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = DNode()
        self.tail = DNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1




    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = DNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)