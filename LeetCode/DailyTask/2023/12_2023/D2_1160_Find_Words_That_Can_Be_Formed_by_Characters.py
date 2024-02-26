from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = {}

        for c in chars:
            ch[c] = 1 + ch.get(c, 0)

        res = 0
        for word in words:
            copy = ch.copy()

            for c in word:
                if c in copy and copy[c] != 0:
                    copy[c] -= 1
                else:
                    res -= len(word)
                    break
            
            res += len(word)
        
        return res


def test():
    sol = Solution()

    # Test Case 1
    words1 = ["cat", "bt", "hat", "tree"]
    chars1 = "atach"
    result1 = sol.countCharacters(words1, chars1)
    print(f'Test Case 1: Input: {words1}, {chars1}, Output: {result1}')

    # Test Case 2
    words2 = ["hello", "world", "leetcode"]
    chars2 = "welldonehoneyr"
    result2 = sol.countCharacters(words2, chars2)
    print(f'Test Case 2: Input: {words2}, {chars2}, Output: {result2}')


if __name__ == "__main__":
    test()
