memo = {}

def memoization_digits_sum(n):

    if n/10 < 1:
        return n
    else:
        n = n%10
        #print n

    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = n + memoization_digits_sum(n/10)

    return memo[n]

print memoization_digits_sum(4321)
