class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #for i in range(0, len(arr)-1):
        #    arr[i] = max(arr[i+1:])
        #arr[-1] = -1
        #return arr

        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans