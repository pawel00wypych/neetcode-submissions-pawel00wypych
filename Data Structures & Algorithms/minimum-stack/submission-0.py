class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elements = []

    def push(self, val: int) -> None:
        if len(self.min_elements) == 0:
            self.min_elements.append(val)
        else:
            min_val = self.min_elements.pop()
            self.min_elements.append(min_val)
            if min_val >= val:
                self.min_elements.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        min_val = self.min_elements.pop()
        if val != min_val:
            self.min_elements.append(min_val)

    def top(self) -> int:
        val = self.stack.pop()
        self.stack.append(val)
        return val

    def getMin(self) -> int:
        min_val = self.min_elements.pop()
        self.min_elements.append(min_val)
        return min_val
