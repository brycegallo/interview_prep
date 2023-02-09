# leetcode 0121 - Best Time to Buy And Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            maxProfit = max(maxProfit, (prices[r] - prices[l]))
            if prices[l] >= prices[r]:
                l = r
            r += 1
        return maxProfit
