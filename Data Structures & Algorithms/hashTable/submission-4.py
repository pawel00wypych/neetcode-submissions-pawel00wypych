class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        key_hash = self.hash(key)
        pair = Pair(key, value)
        while True:
            if self.table[key_hash]:
                if self.table[key_hash].key == key:
                    self.table[key_hash].val = value
                    return
                else:
                    key_hash += 1
                    key_hash %= self.capacity
            else:
                self.table[key_hash] = pair
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return

    def get(self, key: int) -> int:
        key_hash = self.hash(key)
        while self.table[key_hash]:
            if self.table[key_hash].key == key:
                return self.table[key_hash].val
            key_hash += 1
            key_hash %= self.capacity
        else:
            return -1

    def remove(self, key: int) -> bool:
        key_hash = self.hash(key)
        while self.table[key_hash]:
            if self.table[key_hash].key == key:
                self.table[key_hash] = None
                self.size -= 1

                # rehashing in order to avoid creating a hole in the list
                next_idx = (key_hash + 1) % self.capacity
                while self.table[next_idx] is not None:
                    pair = self.table[next_idx]
                    self.table[next_idx] = None
                    self.size -= 1
                    self.insert(pair.key, pair.val)
                    next_idx = (next_idx + 1) % self.capacity
                return True
            else:
                key_hash += 1
                key_hash %= self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.size = 0
        old_table = self.table
        self.table = [None] * self.capacity

        for pair in old_table:
            if pair:
                self.hash(pair.key)
                self.insert(pair.key, pair.val)


    def hash(self, key) -> int:
        return key % self.capacity

