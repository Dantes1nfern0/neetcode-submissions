class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatest_profit = 0
        stack = prices
        while len(stack) > 1:
            for x in stack:
                if x - stack[0] > greatest_profit:
                    greatest_profit = x - stack[0]
            stack.pop(0)
        return greatest_profit
        
        