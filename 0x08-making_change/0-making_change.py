def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet 'total'.
    If 'total' is 0 or less, returns 0.
    If 'total' cannot be met by any combination of 'coins', returns -1.
    """

    # Input validation
    if not coins or total < 0:
        return -1

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize variables
    num_coins = 0
    current_total = total
    i = 0

    # Iterate through coins
    while current_total > 0 and i < len(coins):
        coin = coins[i]
        if coin <= current_total:
            num_coins += current_total // coin
            current_total %= coin
        i += 1

    # If current_total is 0, return num_coins, else return -1
    return num_coins if current_total == 0 else -1

