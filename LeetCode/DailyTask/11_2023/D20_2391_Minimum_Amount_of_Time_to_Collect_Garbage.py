from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        
        for g in garbage:
            res += len(g)

        m, p, g = False, False, False

        for i in range(len(travel), 0, -1):
            m = m or 'M' in garbage[i-1]
            p = p or 'P' in garbage[i-1]
            g = g or 'G' in garbage[i-1]

            res += travel[i-1] * (m + p + g)
        
        return res


def test():
    sol = Solution()

    # Test Case 1
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    result = sol.garbageCollection(garbage, travel)
    print(f'Test Case 1: Garbage: {garbage}, Travel: {travel}, Output: {result}')

    # Test Case 2
    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    result = sol.garbageCollection(garbage, travel)
    print(f'Test Case 2: Garbage: {garbage}, Travel: {travel}, Output: {result}')


if __name__ == "__main__":
    test()
