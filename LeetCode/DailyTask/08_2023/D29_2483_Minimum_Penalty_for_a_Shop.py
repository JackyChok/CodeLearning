class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        res = 0
        curr = final = customers.count('Y')

        for i, val in enumerate(customers):
            curr += (-1 if val == 'Y' else 1)
            if final > curr:
                res, final = i+1, curr
        
        return res

def test_solution():
    solution = Solution()
    assert solution.bestClosingTime("YYNY") == 2
    print(solution.bestClosingTime("YYNY"))
    assert solution.bestClosingTime("NNNNN") == 0
    print(solution.bestClosingTime("NNNNN"))
    assert solution.bestClosingTime("YYYY") == 4
    print(solution.bestClosingTime("YYYY"))

if __name__ == "__main__":
    test_solution()
    print("All test cases passed.")
