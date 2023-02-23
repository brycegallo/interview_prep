// leetcode 0121 - Best Time to Buy And Sell Stock
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// You want to maximize your profit by choosing a single day to buy one stock
// and choosing a different day in the future to sell that stock.
//
// Return the maximum profit you can achieve from this transaction.
// If you cannot achieve any profit, return 0.

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let [left, right, maxprofit] = [0, 1, 0];

    while (right < prices.length) {
        let profit = (prices[right] - prices[left]);
        maxprofit = Math.max(maxprofit, profit);
        if (prices[right] < prices[left]) {
            left = right;
        }
        right ++;
    }
    return maxprofit
};