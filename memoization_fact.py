
memo = {}

def memoization_fact(n):

    if n < 2:
        return 1

    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = n * memoization_fact(n-1)

    return memo[n]

print memoization_fact(7)
