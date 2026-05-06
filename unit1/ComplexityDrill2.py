# Experiment 2: Complexity Drill (Operation Counting)

n = int(input("Enter value of n: "))

print("\n---- Complexity Analysis ----")


# 1. Single Loop

count1 = 0
for i in range(n):
    count1 += 1

print("\n1. Single Loop")
print("Estimated Operations:", count1)
print("Complexity: O(n)")
print("Justification: Loop runs n times.")
print("Each iteration performs constant work.\n")


# 2. Nested Loop

count2 = 0
for i in range(n):
    for j in range(n):
        count2 += 1

print("2. Nested Loop")
print("Estimated Operations:", count2)
print("Complexity: O(n^2)")
print("Justification: Outer loop runs n times and inner loop")
print("runs n times for each iteration → n × n operations.\n")

# 3. Triangular Loop

count3 = 0
for i in range(n):
    for j in range(i + 1):
        count3 += 1

print("3. Triangular Loop")
print("Estimated Operations:", count3)
print("Complexity: O(n^2)")
print("Justification: Total iterations = n(n+1)/2.")
print("Quadratic growth dominates for large n.\n")


# 4. Halving Loop

count4 = 0
k = n
while k > 0:
    count4 += 1
    k //= 2

print("4. Halving Loop")
print("Estimated Operations:", count4)
print("Complexity: O(log n)")
print("Justification: Problem size halves each iteration.")
print("Number of steps ≈ log2(n).\n")