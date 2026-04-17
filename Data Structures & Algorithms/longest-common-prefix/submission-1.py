class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final_prefix = ''
        for l in range(len(min(strs))):
            char = strs[0][l]
            for string in strs:
                if string[l] != char:
                    return final_prefix
            final_prefix += char

        return final_prefix

            
        