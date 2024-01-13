class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for cur in range(1, n+1):
            if cur%3 == 0 and cur%5 == 0:
                res.append("FizzBuzz")
            elif cur%3 == 0:
                res.append("Fizz")
            elif cur%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(cur))
        return res