class Solution:
    def sortVowels(self, s: str) -> str:
        # Step 1: Collect vowels and sort them in descending order
        vowels_sorted = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)

        # Step 2: Construct the answer string by replacing vowels in sorted order
        result = []
        for char in s:
            if char.lower() in 'aeiou':
                result.append(vowels_sorted.pop())
            else:
                result.append(char)

        # Step 3: Join the characters to form the final string
        return ''.join(result)


def run_test():
    sol = Solution()

    # Test Case 1
    s1 = "lEetcOde"
    result1 = sol.sortVowels(s1)
    print(f'Test Case 1: "{s1}" -> "{result1}"')

    # Test Case 2
    s2 = "lYmpH"
    result2 = sol.sortVowels(s2)
    print(f'Test Case 2: "{s2}" -> "{result2}"')


if __name__ == "__main__":
    run_test()
