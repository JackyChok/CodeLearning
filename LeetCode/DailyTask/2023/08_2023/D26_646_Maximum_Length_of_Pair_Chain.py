class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        curr_len = 1
        curr_end = pairs[0][1]

        for pair in pairs[1:]:
            if pair[0] > curr_end:
                curr_len += 1
                curr_end = pair[1]

        return curr_len

if __name__ == "__main__":
    solution = Solution()

    test_case_1 = [[1, 2], [2, 3], [3, 4]]
    print("Test case 1:", solution.findLongestChain(test_case_1))

    test_case_2 = [[1, 2], [7, 8], [4, 5]]
    print("Test case 2:", solution.findLongestChain(test_case_2))
