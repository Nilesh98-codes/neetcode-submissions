class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force approach
        for row in matrix:
            for n in row:
                if n == target:
                    return True
        return False

        