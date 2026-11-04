class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv_map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.kv_map:
            self._detach_node(key)
            self._attach_node(key)
            return self.kv_map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            self.kv_map[key].val = value
            self._detach_node(key)
        else:
            new_node = Node(key, value)
            self.kv_map[key] = new_node
            if len(self.kv_map) > self.capacity:
                key_to_delete = self.head.next.key
                self._detach_node(key_to_delete)
                del self.kv_map[key_to_delete]
            
        self._attach_node(key)

    def _attach_node(self, key):
        self.kv_map[key].next = self.tail
        self.kv_map[key].prev = self.tail.prev
        self.tail.prev.next = self.kv_map[key]
        self.tail.prev = self.kv_map[key]

    def _detach_node(self, key):
        self.kv_map[key].next.prev = self.kv_map[key].prev
        self.kv_map[key].prev.next = self.kv_map[key].next
