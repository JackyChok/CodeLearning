class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # check same length
        if len(s) != len(goal): return False
        
        # if strings are equal - check if there is a double to swap
        if s == goal:
            return True if len(s) - len(set(s)) >= 1 else False
        
        # count differences between strings
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2: return False
                
        # not exactly two differences
        if len(diff) != 2: return False
        
        # check if can be swapped
        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
        
        return False



solution = Solution()

# Test case 1: Strings "ab" and "ba" can be transformed into each other by swapping two characters
s1 = "ab"
goal1 = "ba"
print(solution.buddyStrings(s1, goal1))  # Output: True

# Test case 2: Strings "ab" and "ab" are the same, but there are no duplicate characters to swap
s2 = "ab"
goal2 = "ab"
print(solution.buddyStrings(s2, goal2))  # Output: False

# Test case 3: Strings "aa" and "aa" are the same, and there is a duplicate character 'a' to swap
s3 = "aa"
goal3 = "aa"
print(solution.buddyStrings(s3, goal3))  # Output: True

# Test case 4: Strings "ab" and "ba" have more than two differences
s4 = "acb"
goal4 = "cba"
print(solution.buddyStrings(s4, goal4))  # Output: False

# Test case 5: Strings "abc" and "def" have different characters at all positions
s5 = "abc"
goal5 = "def"
print(solution.buddyStrings(s5, goal5))  # Output: False
