class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)

        return stack

def test_asteroidCollision():
    sol = Solution()

    asteroids1 = [5, 10, -5]
    print(sol.asteroidCollision(asteroids1))
    assert sol.asteroidCollision(asteroids1) == [5, 10]

    asteroids2 = [8, -8]
    print(sol.asteroidCollision(asteroids2))
    assert sol.asteroidCollision(asteroids2) == []

    asteroids3 = [10, 2, -5]
    print(sol.asteroidCollision(asteroids3))
    assert sol.asteroidCollision(asteroids3) == [10]

    print("All test cases passed!")

test_asteroidCollision()
