class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = dict()
        t_dict = dict()

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in s_dict:
                    s_dict[s[i]] = s_dict[s[i]] + 1
                else:
                    s_dict[s[i]] = 1
                if t[i] in t_dict:
                    t_dict[t[i]] = t_dict[t[i]] + 1
                else:
                    t_dict[t[i]] = 1 
            for l in s:
                if l in s_dict and l in t_dict:
                    if s_dict[l] != t_dict[l]:
                        return False
                else:
                    return False
        return True 