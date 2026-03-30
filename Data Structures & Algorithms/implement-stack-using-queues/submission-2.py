from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.q_help = deque()

    def push(self, x: int) -> None:
        q_len = len(self.q)
        for e in range(q_len):
            self.q_help.append(self.q.pop())
        q_help_len = len(self.q_help)
        for e in range(q_help_len):
            self.q.append(self.q_help.pop())
        self.q.append(x)
        
    def pop(self) -> int:
        return self.q.pop()
        
    def top(self) -> int:
        top = self.q.pop()
        self.q.append(top) 
        return top

    def empty(self) -> bool:
        print(f"len of queue: {len(self.q)}")
        return False if len(self.q) > 0 else True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()