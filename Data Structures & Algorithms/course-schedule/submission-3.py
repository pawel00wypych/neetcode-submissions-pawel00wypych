class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        check_cycles = {}
        vertices = set()
        if not prerequisites:
            return True

        for pair in prerequisites:
            a, b = pair[0], pair[1]
            vertices.add(a)
            vertices.add(b)
            if a == b:
                return False
            if b in check_cycles:
                if a in check_cycles[b]:
                    return False # There is a cycle
            if a in check_cycles:
                check_cycles[a].append(b)
            else:
                check_cycles[a] = [b]

        for v in vertices:
            if v not in check_cycles:
                return True
        return False