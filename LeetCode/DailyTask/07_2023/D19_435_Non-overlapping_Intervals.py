class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        ans = 0
        endTime = float("-inf")
        for interval in intervals:
            if interval[0] < endTime:
                ans += 1
            else:
                endTime = interval[1]
        return ans

def test_eraseOverlapIntervals():
    sol = Solution()

    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(sol.eraseOverlapIntervals(intervals1))
    assert sol.eraseOverlapIntervals(intervals1) == 1

    intervals2 = [[1, 2], [1, 2], [1, 2]]
    print(sol.eraseOverlapIntervals(intervals2))
    assert sol.eraseOverlapIntervals(intervals2) == 2

    intervals3 = [[1, 2], [2, 3]]
    print(sol.eraseOverlapIntervals(intervals3))
    assert sol.eraseOverlapIntervals(intervals3) == 0

    print("All test cases passed!")

test_eraseOverlapIntervals()
