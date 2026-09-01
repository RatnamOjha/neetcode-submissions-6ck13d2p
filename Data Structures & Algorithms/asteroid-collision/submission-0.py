class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(top) < abs(a):
                    stack.pop()
                elif abs(top) > abs(a):
                    break
                elif abs(top) == abs(a):
                    stack.pop()
                    break
            else:
                stack.append(a)
        return stack