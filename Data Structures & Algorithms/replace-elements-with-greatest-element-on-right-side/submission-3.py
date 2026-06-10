class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        def find_max(i: int) -> (int, int):
            max_e, max_i = arr[i], i
            j = i
            while j < len(arr):
                if max_e < arr[j]:
                    max_e, max_i = arr[j], j
                j += 1
            return (max_e, max_i)

        for i in range(len(arr)-1):
            m_j, j = find_max(i+1)
            while i < j:
                arr[i] = m_j
                i += 1
        arr[-1] = -1
        return arr
        
        

