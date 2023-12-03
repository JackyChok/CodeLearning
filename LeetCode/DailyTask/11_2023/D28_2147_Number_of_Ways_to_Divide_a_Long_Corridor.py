class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        mod = 10**9 + 7  # Define the modulo value for the final result
        res = 1  # Initialize the result variable to 1 (will be updated during iteration)
        prev_seat = 0  # Initialize the variable to track the index of the previous seat
        num_seats = 0  # Initialize the variable to count the number of seats encountered

        for i, c in enumerate(corridor):
            if c == 'S':
                num_seats += 1  # Increment the seat count when 'S' is encountered
                # Check if there are more than 2 consecutive seats and an odd number of seats
                if num_seats > 2 and num_seats % 2 == 1:
                    # Update the answer using the distance between the current seat and the previous seat
                    res *= i - prev_seat
                prev_seat = i  # Update the previous seat index to the current index

        # Return the answer only if there are more than 1 seat and an even number of seats
        return res % mod if num_seats > 1 and num_seats % 2 == 0 else 0


def test():
    sol = Solution()

    # Test Case 1
    corridor1 = "SSPPSPS"
    result1 = sol.numberOfWays(corridor1)
    print(f'Test Case 1: Input: {corridor1}, Output: {result1}')

    # Test Case 2
    corridor2 = "PPSPSP"
    result2 = sol.numberOfWays(corridor2)
    print(f'Test Case 2: Input: {corridor2}, Output: {result2}')

    # Test Case 3
    corridor3 = "S"
    result3 = sol.numberOfWays(corridor3)
    print(f'Test Case 3: Input: {corridor3}, Output: {result3}')


if __name__ == "__main__":
    test()
