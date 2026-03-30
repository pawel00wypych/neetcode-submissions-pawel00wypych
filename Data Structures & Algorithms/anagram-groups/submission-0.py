class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_of_anagrams = []
        st_dict = {}
        for st in strs:
            sort_st = ''.join(sorted(st))
            if sort_st in st_dict:
                st_dict[sort_st].append(st)
            else:
                st_dict[sort_st] = [st]

        for v in st_dict.values():    
            list_of_anagrams.append(v)

        return list_of_anagrams