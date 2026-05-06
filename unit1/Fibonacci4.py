# Experiment 4: Fibonacci (Naive vs Memoized) + Call Counter


naive_calls = 0
memo_calls = 0



# Naive Recursive Fibonacci

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)



# Memoized Fibonacci

memo = {}

def fib_memo(n):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)

    return memo[n]


# Driver Code

tests = [10, 20, 30]

for n in tests:
    naive_calls = 0
    memo_calls = 0
    memo.clear()

    result1 = fib_naive(n)
    result2 = fib_memo(n)

    print("\nValue of n =", n)
    print("Fibonacci =", result1)
    print("Naive Calls =", naive_calls)
    print("Memoized Calls =", memo_calls)

    print("Explanation:")
    print("Naive recursion recomputes same subproblems many times.")
    print("Memoization stores previous results and avoids recomputation.")