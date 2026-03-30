class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_d = {}
        t_d = {}

        for s_i in s:
            if s_i in s_d:
                s_d[s_i] += 1
            else:
                s_d[s_i] = 1

        for t_i in t:
            if t_i in t_d:
                t_d[t_i] += 1
            else:
                t_d[t_i] = 1

        return s_d ==  t_d