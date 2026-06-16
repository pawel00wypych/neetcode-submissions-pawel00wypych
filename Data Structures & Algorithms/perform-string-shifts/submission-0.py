class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        deque_s = deque(s)

        for direction_i, amount_i in shift:
            for i in range(amount_i):
                if direction_i == 0:
                    l = deque_s.popleft()
                    deque_s.append(l)
                else:
                    l = deque_s.pop()
                    deque_s.appendleft(l)
        return "".join(deque_s)