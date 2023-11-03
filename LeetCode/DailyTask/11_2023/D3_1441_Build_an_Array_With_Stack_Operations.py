class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        target_set = set(target)
        result = []

        for i in range(1, target[-1] + 1):
            if i in target_set:
                result.append("Push")
            else:
                result.append("Push")
                result.append("Pop")

        return result

if __name__ == '__main__':
    solution = Solution()

    target = [1, 3]
    n = 3
    expected_result = ["Push", "Push", "Pop", "Push"]
    result = solution.buildArray(target, n)
    print("Result 1:", result)

    target = [1, 2, 3]
    n = 3
    expected_result = ["Push", "Push", "Push"]
    result = solution.buildArray(target, n)
    print("Result 2:", result)

    target = [1, 2]
    n = 4
    expected_result = ["Push", "Push", "Pop", "Push"]
    result = solution.buildArray(target, n)
    print("Result 3:", result)
