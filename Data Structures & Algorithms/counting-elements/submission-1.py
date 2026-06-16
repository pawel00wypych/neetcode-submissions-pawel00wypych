class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_map = {}
        c_of_indices = 0

        for i in range(len(arr)):
            arr_map[arr[i]] = arr_map.get(arr[i], 0) + 1

        for i in range(len(arr)):
            if arr[i]+1 in arr_map:
                c_of_indices += 1

        return c_of_indices