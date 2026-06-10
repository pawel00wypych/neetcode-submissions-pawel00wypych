class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            new_max = max(arr[i], prev_max)
            arr[i] = prev_max
            prev_max = new_max
            
        arr[-1] = -1
        return arr
        