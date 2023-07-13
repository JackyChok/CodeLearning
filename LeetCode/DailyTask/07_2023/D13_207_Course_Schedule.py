import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for pair in prerequisites:
            course, pre = pair
            graph[course].append(pre)
        
        visit = [0] * numCourses

        def hasCycle(course):
            if visit[course] == 1: return True
            if visit[course] == 2: return False

            visit[course] = 1
            for pre in graph[course]:
                if hasCycle(pre):
                    return True
            
            visit[course] = 2
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        
        return True


# Create an instance of the Solution class
solution = Solution()

# Test case 1
numCourses = 2
prerequisites = [[1,0]]
print(solution.canFinish(numCourses, prerequisites))  # Output: True

# Test case 2
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(solution.canFinish(numCourses, prerequisites))  # Output: False
