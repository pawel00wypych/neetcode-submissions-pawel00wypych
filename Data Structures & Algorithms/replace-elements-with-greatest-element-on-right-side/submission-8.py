class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        r_elem = arr[i]
        arr[i] = -1
        i -= 1
        while i >= 0:
            if arr[i] > r_elem:
                temp = arr[i]
                arr[i] = r_elem
                r_elem = temp
            else:
                arr[i] = r_elem
            i -= 1

        return arr