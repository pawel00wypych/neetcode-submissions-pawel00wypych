class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, n = 0, 0
        anagram = [-1] * len(nums1)
        while i < len(nums1):
            n = i
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and j not in anagram:
                    anagram[i] = j
                    i += 1
                    break
            if n == i: # there was no fitting number in the nums2
                return False
        return anagram
                