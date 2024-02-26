from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)

        current_winner = arr[0]
        consecutive_wins = 0

        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                consecutive_wins += 1
            else:
                current_winner = arr[i]
                consecutive_wins = 1

            if consecutive_wins == k:
                return current_winner

        return current_winner

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    arr1 = [2, 1, 3, 5, 4, 6, 7]
    k1 = 2
    result1 = solution.getWinner(arr1, k1)
    print("Result 1:", result1)

    # Test Case 2
    arr2 = [3, 2, 1]
    k2 = 10
    result2 = solution.getWinner(arr2, k2)
    print("Result 2:", result2)
