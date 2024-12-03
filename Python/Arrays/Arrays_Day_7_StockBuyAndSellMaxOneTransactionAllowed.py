# Stock Buy and Sell – Max one Transaction Allowed
# Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
# Output: 8
# # Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.

class Solution:
    def maximumProfit(self, prices):
        min_num = prices[0]  # Initialize minimum price to the first element
        max_num = float('-inf')  # Initialize maximum profit to the smallest possible value
        
        for price in prices:
            # Update the minimum price encountered so far
            min_num = min(min_num, price)
            # Calculate the profit by selling at the current price
            profit = price - min_num
            # Update the maximum profit if the current profit is higher
            max_num = max(max_num, profit)
        
        return max_num

# Example usage
solution = Solution()
prices = [7, 1, 5, 3, 6, 4]

result = solution.maximumProfit(prices)
print(f"Maximum Profit: {result}")
