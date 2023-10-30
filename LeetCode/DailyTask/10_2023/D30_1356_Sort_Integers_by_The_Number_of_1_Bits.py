class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == "__main__":
    # Example 1
    arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    solution1 = Solution()
    sorted_arr1 = solution1.sortByBits(arr1)
    print("Sorted array for example 1:", sorted_arr1)

    # Example 2
    arr2 = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    solution2 = Solution()
    sorted_arr2 = solution2.sortByBits(arr2)
    print("Sorted array for example 2:", sorted_arr2)
