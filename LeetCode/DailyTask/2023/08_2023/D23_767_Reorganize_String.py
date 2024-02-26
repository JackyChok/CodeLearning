import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_count = Counter(s)

        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        res = []
        prev_count, prev_char = 0, ""

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            prev_count, prev_char = count + 1, char
        
        return "".join(res) if len(res) == len(s) else ""

if __name__ == "__main__":
    solution = Solution()

    test_case1 = "aab"
    result1 = solution.reorganizeString(test_case1)
    print("Test Case 1:", result1)

    test_case2 = "aaab"
    result2 = solution.reorganizeString(test_case2)
    print("Test Case 2:", result2)
