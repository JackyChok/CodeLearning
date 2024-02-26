from collections import defaultdict

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = []
        groups = defaultdict(list)

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            
            if len(groups[size]) == size:
                res.append(groups.pop(size))
        
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    groupSizes1 = [3, 3, 3, 3, 3, 1, 3]
    result1 = solution.groupThePeople(groupSizes1)
    print(result1)  # Output should be [[0, 1, 2], [3, 4, 6], [5]]

    # Test case 2
    groupSizes2 = [2, 1, 3, 3, 3, 2]
    result2 = solution.groupThePeople(groupSizes2)
    print(result2)  # Output should be [[0, 5], [2, 3, 4], [5]]
