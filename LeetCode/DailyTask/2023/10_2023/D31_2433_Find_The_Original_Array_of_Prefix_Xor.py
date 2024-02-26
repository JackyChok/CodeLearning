class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]

if __name__ == "__main__":
    solution = Solution()
    input_array = [5, 2, 0, 3, 1]
    result_array = solution.findArray(input_array)
    print("Input Array 1:", input_array)
    print("Result Array 1:", result_array)

    input_array = [13]
    result_array = solution.findArray(input_array)
    print("Input Array 2:", input_array)
    print("Result Array 2:", result_array)