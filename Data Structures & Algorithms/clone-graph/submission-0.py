"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        layer = deque()
        layer.append(node)
        visited = {}

        while layer:
            for i in range(len(layer)):
                old_node = layer.popleft()
                if old_node.val in visited:
                    new_node = visited[old_node.val]
                elif old_node.val not in visited:
                    new_node = Node(old_node.val)
                    visited[old_node.val] = new_node

                for neighbor in old_node.neighbors:
                    if neighbor.val in visited:
                        new_node_neighbor = visited[neighbor.val]
                    elif neighbor.val not in visited:
                        new_node_neighbor = Node(neighbor.val)
                        visited[neighbor.val] = new_node_neighbor
                        layer.append(neighbor)

                    new_node.neighbors.append(new_node_neighbor)
                    
        first_node = visited[node.val]
        return first_node