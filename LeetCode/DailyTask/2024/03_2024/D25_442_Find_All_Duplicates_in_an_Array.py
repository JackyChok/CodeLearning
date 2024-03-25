from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        lst=[]
        for i,j in c.items():
            if j>=2:
                lst.append(i)
        return lst

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print(solution.findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2, 3]
    print(solution.findDuplicates([1,1,2]))  # Output: [1]
    print(solution.findDuplicates([1]))  # Output: []
