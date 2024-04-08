from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining  

# Test cases
solution = Solution()
students1 = [1, 1, 0, 0]
sandwiches1 = [0, 1, 0, 1]
print(solution.countStudents(students1, sandwiches1))  # Output: 0

students2 = [1, 1, 1, 0, 0, 1]
sandwiches2 = [1, 0, 0, 0, 1, 1]
print(solution.countStudents(students2, sandwiches2))  # Output: 1
