# leetcode 0309 - Best Time to Buy and Sell Stock with Cooldown
# Medium - 2D-DP
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
#     After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Time: O(n) Memory: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, looking_to_buy) val=max_profit

        def dfs(i, looking_to_buy):
            if i >= len(prices):
                return 0
            if (i, looking_to_buy) not in dp:
                cooldown = dfs(i + 1, looking_to_buy)
                if looking_to_buy:
                    transaction = dfs(i + 1, not looking_to_buy) - prices[i]  # buying
                else:
                    transaction = dfs(i + 2, not looking_to_buy) + prices[i]  # selling
                dp[(i, looking_to_buy)] = max(transaction, cooldown)
            return dp[(i, looking_to_buy)]

        return dfs(0, True)
