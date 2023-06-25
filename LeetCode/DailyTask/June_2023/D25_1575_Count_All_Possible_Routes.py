class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        def dfs(curr_loc, rem_fuel):
            if rem_fuel < 0:
                return 0
            elif curr_loc == finish:
                res = 1
            else:
                res =  0

            for next_loc in range(len(locations)):
                if curr_loc != next_loc:
                    cost = abs(locations[curr_loc] - locations[next_loc])
                    res += dfs(next_loc, rem_fuel - cost)
            return res % 1000000007

        return dfs(start, fuel) 
    
# Test Case 1
locations = [2, 3, 6, 8, 4]
start = 1
finish = 3
fuel = 5
print(Solution().countRoutes(locations, start, finish, fuel))    

# Test Case 2
locations = [4, 3, 1]
start = 1
finish = 0
fuel = 6
print(Solution().countRoutes(locations, start, finish, fuel))

# Test Case 2
locations = [1,2,3]
start = 0
finish = 2
fuel = 40
print(Solution().countRoutes(locations, start, finish, fuel)) 