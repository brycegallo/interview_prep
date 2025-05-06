// Leetcode 0121 - Best Time to Buy and Sell Stock
// Easy - Sliding Window
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
//
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
// Sliding Window Solution
// Time Complexity: O(n) Memory O(1)

int maxProfit(int* prices, int pricesSize) {
    int left = 0;
    int right = 1;
    int max_profit = 0;

    while (right < pricesSize) {
	int todays_profit = prices[right] - prices[left];
	if (prices[left] > prices[right]) {
	    left = right;
	}
	if (max_profit < todays_profit) {
	    max_profit = todays_profit;
	}
	right++;
    }
    return max_profit;
}
