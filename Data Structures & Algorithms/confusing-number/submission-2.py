class Solution:
    def confusingNumber(self, n: int) -> bool:
        digit_mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
            }

        nums_str = str(n)
        new_n = ''
        for c in nums_str:
            if c not in digit_mapping:
                return False
            else:
                new_n += digit_mapping[c]
        print(f"new n = {new_n}")
        new_n = new_n[::-1]
        if int(new_n) == n:
            return False
        return True