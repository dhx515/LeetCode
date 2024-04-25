class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for a in asteroids:
            while ans and ans[-1] > 0 and a < 0:
                if ans[-1]+a < 0:
                    ans.pop()
                elif ans[-1]+a > 0:
                    break
                else:
                    ans.pop()
                    break

            else:
                ans.append(a)

        return ans