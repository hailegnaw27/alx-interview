#!/usr/bin/python3
"""
Module for making change problem.
"""

def makeChange(coins, total):
    if total < 0:
        return 0
    if total == 0:
        return 0
    if not coins or len(coins) == 0:
        return -1
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453)) 
