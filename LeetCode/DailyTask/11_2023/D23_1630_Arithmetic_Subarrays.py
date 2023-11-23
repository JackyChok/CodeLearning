from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
                
            return True
        
        ans = []
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            ans.append(check(arr))
        
        return ans


def test():
    sol = Solution()

    # Test Case 1
    nums1 = [4, 6, 5, 9, 3, 7]
    l1 = [0, 0, 2]
    r1 = [2, 3, 5]
    result1 = sol.checkArithmeticSubarrays(nums1, l1, r1)
    print(f'Test Case 1: Input: {nums1}, {l1}, {r1}, Output: {result1}')

    # Test Case 2
    nums2 = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l2 = [0, 1, 6, 4, 8, 7]
    r2 = [4, 4, 9, 7, 9, 10]
    result2 = sol.checkArithmeticSubarrays(nums2, l2, r2)
    print(f'Test Case 2: Input: {nums2}, {l2}, {r2}, Output: {result2}')


if __name__ == "__main__":
    test()
