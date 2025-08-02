def min_coins(coins, amount):
    coins.sort(reverse=True)  # Sort coins from largest to smallest
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
amount = 93
print("Coins used:", min_coins(coins, amount))