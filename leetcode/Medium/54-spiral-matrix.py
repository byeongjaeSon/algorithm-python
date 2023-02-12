class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        matrix = deque([deque(m) for m in matrix])
        while matrix:
            if matrix: result.extend(matrix.popleft())
            result.extend([row.pop() for row in matrix if row])
            if matrix: result.extend(reversed(matrix.pop()))
            result.extend(reversed([row.popleft() for row in matrix if row]))
        return result
