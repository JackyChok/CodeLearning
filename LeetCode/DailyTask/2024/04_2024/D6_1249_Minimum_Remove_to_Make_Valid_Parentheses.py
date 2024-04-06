class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        split_str=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                # if current char is '(' then push it to stack
                stack.append(i)
            elif s[i]==')':
                # if current char is ')' then pop top of the stack
                if len(stack) !=0:
                    stack.pop()
                else:
                    # if our stack is empty then we can't pop so make  current char as ''
                    split_str[i]=""
        for i in stack:
            split_str[i]=""
        return '' .join(split_str)

# Test cases
def test_solution():
    solution = Solution()
    assert solution.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert solution.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert solution.minRemoveToMakeValid("))((") == ""
    assert solution.minRemoveToMakeValid("") == ""

if __name__ == "__main__":
    test_solution()
    print("All test cases pass")
