from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]
        time_to_city.sort()

        for i in range(len(time_to_city)):
            if time_to_city[i] <= i:
                return i

        return len(dist)

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1
    dist1 = [1, 3, 4]
    speed1 = [1, 1, 1]
    result1 = solution.eliminateMaximum(dist1, speed1)
    print("Result 1:", result1)

    # Test Case 2
    dist2 = [1, 1, 2, 3]
    speed2 = [1, 1, 1, 1]
    result2 = solution.eliminateMaximum(dist2, speed2)
    print("Result 2:", result2)

    # Test Case 3
    dist3 = [3, 2, 4]
    speed3 = [5, 3, 2]
    result3 = solution.eliminateMaximum(dist3, speed3)
    print("Result 3:", result3)
