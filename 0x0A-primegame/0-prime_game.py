#!/usr/bin/python3

def isWinner(x, nums):
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n, primes):
        game_set = list(range(1, n + 1))
        turn = 0  # Maria starts
        
        while True:
            move_made = False
            for p in primes:
                if p > n:
                    break
                if game_set[p - 1] != 0:
                    # Maria or Ben picks p
                    for multiple in range(p, n + 1, p):
                        game_set[multiple - 1] = 0
                    move_made = True
                    break
            
            if not move_made:
                break
            
            turn = 1 - turn  # Switch turn
        
        return "Maria" if turn == 1 else "Ben"
    
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    primes = sieve(max_num)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n, primes)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

