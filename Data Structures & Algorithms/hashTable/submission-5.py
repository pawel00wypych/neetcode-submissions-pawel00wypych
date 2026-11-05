class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv_map = [None] * self.cap
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        new_hash = self._hash(key)
        while self.kv_map[new_hash]:
            if self.kv_map[new_hash][0] == key:
                self.kv_map[new_hash] = (key, value)
                return None
            new_hash += 1
            new_hash %= self.cap

        self.kv_map[new_hash] = (key, value)
        self.size += 1
        if self.size >= self.cap / 2:
            self.resize()

    def get(self, key: int) -> int:
        find_hash = self._hash(key)
        while self.kv_map[find_hash]:
            if self.kv_map[find_hash][0] == key:
                return self.kv_map[find_hash][1]
            find_hash += 1
        return -1

    def remove(self, key: int) -> bool:

        find_hash = self._hash(key)
        while self.kv_map[find_hash]:
            if self.kv_map[find_hash][0] == key:
                self.size -= 1
                self.kv_map[find_hash] = None
                return True
            find_hash += 1

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap = self.cap * 2
        temp = self.kv_map
        self.kv_map = [None] * self.cap
        self.size = 0
        for kv_pair in temp:
            if kv_pair:
                self.insert(kv_pair[0], kv_pair[1])

    def _hash(self, key) -> int:
        return key % self.cap

