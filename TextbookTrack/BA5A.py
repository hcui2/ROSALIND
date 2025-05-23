def dp_coinchange(coins, amount):
    """
    Dynamic programming solution to the coin change problem.
    :param coins: List of coin denominations
    :param amount: Total amount to make change for
    :return: Minimum number of coins needed to make change for the amount
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make change for 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1]

with open('TestData/rosalind_ba5a.txt') as f:
    lines = f.readlines()
    amount = int(lines[0].strip())
    coins = list(map(int, lines[1].strip().split(',')))

result = dp_coinchange(coins, amount)
print(result)
