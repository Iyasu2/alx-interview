#!/usr/bin/python3
'''
this is the module
'''


def makeChange(coins, total):
    '''
    Initialize a table to store the minimum number of coins for each amount
    '''
    if total <= 0:
        return 0

    remaining_amount = total
    coin_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1
        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            coin_count += 1
        else:
            coin_index += 1

    return coin_count
