"""
	@Project: leetcode
	@file: BestTimeToBuyAndSellStock.py
	@author: AC
	@time: 2016/5/6 12:48
	@Description: Say you have an array for which the ith element is the price of a given stock on day i.
                  If you were only permitted to complete at most one transaction
                  (ie, buy one and sell one share of the stock), design an algorithm to find
                  the maximum profit.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            profit = 0
        elif len(prices) == 2:
            profit = prices[1]-prices[0]
        else:
            min_val = min(prices[:2])
            profit = prices[1]-prices[0]
            i = 2
            while i < len(prices):
                profit = max(profit, prices[i]-min_val)
                if prices[i] < min_val:
                    min_val = prices[i]
                i += 1
        if profit < 0:
            profit = 0
        return profit