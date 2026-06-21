class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_of_old_passengers = 0
        for p in details:
            age = int(p[-4:-2])
            if age > 60:
                num_of_old_passengers += 1
        return num_of_old_passengers