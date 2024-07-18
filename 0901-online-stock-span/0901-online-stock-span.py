class StockSpanner(object):

    def __init__(self):
        self.day = 0
        self.stack = [] # monotonic decreasing stack

    def next(self, price):
        self.day += 1
		# keep popping until the stack is either monotonically decreasing or empty
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
		# find the number of days satisfying the condition
        res = self.day if not self.stack else (self.day - self.stack[-1][0])
		# add current price to the stack
        self.stack.append((self.day, price))
        return res