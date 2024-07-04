#!/usr/bin/python3
def sieve(n):
    """ Generate list of primes up to n using Sieve of Eratosthenes """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    return [p for p in range(n + 1) if is_prime[p]]

def prime_game(n, primes):
    """ Play the game for a given number n using the list of primes """
    multiples_removed = [False] * (n + 1)
    turn = 0  # 0 for Maria's turn, 1 for Ben's turn
    
    for p in primes:
        if p > n:
            break
        if not multiples_removed[p]:
            turn += 1
            for multiple in range(p, n + 1, p):
                multiples_removed[multiple] = True
    
    # Maria starts first, so if turn is odd, Maria wins, otherwise Ben wins
    return turn % 2 == 1

def isWinner(x, nums):
    """ Determine the overall winner after x rounds """
    if not nums or x <= 0:
        return None
    
    max_num = max(nums)
    primes = sieve(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example Usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

