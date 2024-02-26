import collections

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1
        
        itemGraph = collections.defaultdict(list)
        itemIndegree = [0] * n
        groupGraph = collections.defaultdict(list)  # Initialize groupGraph
        groupIndegree = [0] * groupId
        
        for i in range(n):
            for prev in beforeItems[i]:
                itemGraph[prev].append(i)
                itemIndegree[i] += 1
                if group[i] != group[prev]:
                    groupGraph[group[prev]].append(group[i])
                    groupIndegree[group[i]] += 1
        
        itemOrder = self.topologicalSort(itemGraph, itemIndegree)
        groupOrder = self.topologicalSort(groupGraph, groupIndegree)
        
        if not itemOrder or not groupOrder:
            return []
        
        orderedGroups = collections.defaultdict(list)
        for item in itemOrder:
            orderedGroups[group[item]].append(item)
        
        answerList = []
        for groupIndex in groupOrder:
            answerList.extend(orderedGroups[groupIndex])
        
        return answerList
    
    def topologicalSort(self, graph, indegree):
        visited = []
        stk = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stk.append(i)
        
        while stk:
            curr = stk.pop()
            visited.append(curr)
            
            for n in graph[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    stk.append(n)
        
        return visited if len(visited) == len(graph) else []


# Test cases
if __name__ == "__main__":
    solution = Solution()

    n1 = 8
    m1 = 2
    group1 = [-1,-1,1,0,0,1,0,-1]
    beforeItems1 = [[],[6],[5],[6],[3,6],[],[],[]]
    result1 = solution.sortItems(n1, m1, group1, beforeItems1)
    print("Test Case 1:", result1)

    n2 = 8
    m2 = 2
    group2 = [-1,-1,1,0,0,1,0,-1]
    beforeItems2 = [[],[6],[5],[6],[3],[],[4],[]]
    result2 = solution.sortItems(n2, m2, group2, beforeItems2)
    print("Test Case 2:", result2)