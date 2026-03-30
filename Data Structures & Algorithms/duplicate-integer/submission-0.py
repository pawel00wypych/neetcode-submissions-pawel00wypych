class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplicates = dict()
        for e in nums:
            if duplicates.get(str(e)) is None:
                duplicates.update({str(e): 1})
            else:
                return True
        return False