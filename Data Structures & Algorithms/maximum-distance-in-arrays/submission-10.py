class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        max_diff = 0
        diff1 = abs(arrays[0][0] - arrays[1][-1])
        diff2 = abs(arrays[1][0] - arrays[0][-1])
        if diff2 > diff1:
            max_diff = diff2
            global_min = arrays[1][0]
            global_max = arrays[0][-1]
        else:
            max_diff = diff1
            global_min = arrays[0][0]
            global_max = arrays[1][-1]

        for m in range(2, len(arrays)):
            if arrays[m][0] < global_min and max_diff < abs(global_max-arrays[m][0]):
                global_min = arrays[m][0]
                max_diff = abs(global_max - global_min)
            elif arrays[m][-1] > global_max and max_diff < abs(arrays[m][-1] - global_min):
                global_max = arrays[m][-1]
                max_diff = abs(global_max - global_min)

        return max_diff