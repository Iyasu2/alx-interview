#!/usr/bin/python3
'''
this is the module
'''


def makeChange(coins, total):
    '''
    Initialize a table to store the minimum number of coins for each amount
    '''
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the minimum number of coins needed for each amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the final value remains unchanged, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
