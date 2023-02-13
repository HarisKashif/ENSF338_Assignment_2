import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def func_optimized(n, memo={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = func_optimized(n-1) + func_optimized(n-2)
            return memo[n]

n_values = range(36)

Original_times = []
Optimized_times = []

for n in n_values:
    start = time.time()
    func(n)
    end = time.time()
    Original_times.append(end-start)

    start = time.time()
    func_optimized(n)
    end = time.time()
    Optimized_times.append(end-start)

plt.plot(n_values, Original_times)
plt.plot(n_values, Optimized_times)
plt.xlabel("Input (n)")
plt.ylabel("Time (s)")
plt.legend(["func","func_optimized"])
plt.show()
