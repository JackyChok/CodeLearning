class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        
        if mat[0][0] != 0:
            mat[0][0] = m + n
        
        # Travel top down
        for j in range(1, m):
            if mat[0][j] != 0:
                mat[0][j] = mat[0][j - 1] + 1
        
        for i in range(1, n):
            if mat[i][0] != 0:
                mat[i][0] = mat[i - 1][0] + 1
        
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] != 0:
                    mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + 1
        
        # Travel up
        for j in range(m - 2, -1, -1):
            if mat[n - 1][j] != 0:
                mat[n - 1][j] = min(mat[n - 1][j], mat[n - 1][j + 1] + 1)
        
        for i in range(n - 2, -1, -1):
            if mat[i][m - 1] != 0:
                mat[i][m - 1] = min(mat[i][m - 1], mat[i + 1][m - 1] + 1)
        
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = min(mat[i][j], min(mat[i + 1][j], mat[i][j + 1]) + 1)
        
        return mat

# Test cases
solution = Solution()

mat1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
result1 = solution.updateMatrix(mat1)
print(result1)

mat2 = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
result2 = solution.updateMatrix(mat2)
print(result2)
