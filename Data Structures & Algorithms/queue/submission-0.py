class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = self.head

    def isEmpty(self) -> bool:
        if self.head == None and self.tail == None:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
                
    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self) -> int:
        if self.tail:
            val = self.tail.val
            new_tail = self.tail.prev
            if new_tail:
                new_tail.next = None
                self.tail = new_tail
            else:
                self.tail = None
                self.head = None
            return val

        else:
            return -1

    def popleft(self) -> int:
        if self.head:
            val = self.head.val
            new_head = self.head.next
            if new_head:
                new_head.prev = None
                self.head = new_head
            else:
                self.tail = None
                self.head = None
            return val
        else:
            return -1
