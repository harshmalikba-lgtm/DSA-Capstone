# Experiment 3: Recursive Factorial + Call Stack Trace

def factorial(n):
    # Reject invalid input
    if n < 0:
        return "Invalid input! Factorial not defined for negative numbers."

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)



n = int(input("Enter a number (n ≥ 0): "))

result = factorial(n)
print("Factorial =", result)