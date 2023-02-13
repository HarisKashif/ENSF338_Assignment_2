def func_optimized(n, memo={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = func_optimized(n-1) + func_optimized(n-2)
            return memo[n]