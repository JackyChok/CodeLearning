class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = {src: [] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    result1 = solution.findItinerary(tickets1)
    print(result1)  # Output should be ["JFK", "MUC", "LHR", "SFO", "SJC"]

    # Test case 2
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    result2 = solution.findItinerary(tickets2)
    print(result2)  # Output should be ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
