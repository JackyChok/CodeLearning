class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                # Line complete
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, length = [], 0  # Reset line and length
            
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # Handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)

        return res

if __name__ == "__main__":
    solution = Solution()

    test_case1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    result1 = solution.fullJustify(test_case1, maxWidth1)
    print("Test Case 1:", result1)

    test_case2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    result2 = solution.fullJustify(test_case2, maxWidth2)
    print("Test Case 2:", result2)

    test_case3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    result3 = solution.fullJustify(test_case3, maxWidth3)
    print("Test Case 3:", result3)
