memo = {}

def memoization_sum(n):

    if n == 1:
        return 1

    if n == 0:
        return 0

    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = n + memoization_sum(n-1)

    return memo[n]

print memoization_sum(4)
