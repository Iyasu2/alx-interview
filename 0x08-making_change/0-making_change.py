#!/usr/bin/python3
'''
this is the module
'''


def makeChange(coins, total):
    '''
    Initialize a table to store the minimum number of coins for each amount
    '''
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each amount
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total amount cannot be met by any number of coins, return -1
    if dp[total] == float('inf'):
        return -1

    # Return the fewest number of coins needed to meet the total amount
    return dp[total]
