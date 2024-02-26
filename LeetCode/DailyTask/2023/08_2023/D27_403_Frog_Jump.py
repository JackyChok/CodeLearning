class Solution:
    def canCross_solution1(self, stones):
        if stones[1] != 1:
            return False
        
        n = len(stones)
        dp = [[False] * n for _ in range(n)]
        return self.helper_solution1(stones, 0, 1, dp)
    
    def helper_solution1(self, stones, lastIndex, currentIndex, dp):
        if currentIndex == len(stones) - 1:
            return True
        
        if dp[lastIndex][currentIndex]:
            return False
        
        lastJump = stones[currentIndex] - stones[lastIndex]
        nextIndex = currentIndex + 1
        
        while nextIndex < len(stones) and stones[nextIndex] <= stones[currentIndex] + lastJump + 1:
            nextJump = stones[nextIndex] - stones[currentIndex]
            jump = nextJump - lastJump
            
            if -1 <= jump <= 1:
                if self.helper_solution1(stones, currentIndex, nextIndex, dp):
                    return True
            
            nextIndex += 1
        
        dp[lastIndex][currentIndex] = True
        return False

    def canCross_solution2(self, stones):
        if stones[1] != 1:
            return False
        
        dp = {}
        
        def helper(index, jump):
            if index == len(stones) - 1:
                return True
            
            if (index, jump) in dp:
                return dp[(index, jump)]
            
            ans = False
            for j in range(max(1, jump - 1), jump + 2):
                if j == 0:
                    continue
                
                new_stone = stones[index] + j
                index_new = exists(stones, new_stone)
                
                if index_new != -1:
                    ans |= helper(index_new, j)
            
            dp[(index, jump)] = ans
            return ans
        
        def exists(stone, target):
            left, right = 0, len(stone) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if stone[mid] == target:
                    return mid
                elif stone[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        return helper(1, 1)

# Test cases
stones1 = [0,1,3,5,6,8,12,17]
stones2 = [0,1,2,3,4,8,9,11]

solution = Solution()

print("Solution 1:")
print(solution.canCross_solution1(stones1))  # Expected output: True
print(solution.canCross_solution1(stones2))  # Expected output: False

print("\nSolution 2:")
print(solution.canCross_solution2(stones1))  # Expected output: True
print(solution.canCross_solution2(stones2))  # Expected output: False
