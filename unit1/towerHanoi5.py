# Experiment 5: Tower of Hanoi

move_count = 0

def hanoi(n, src, aux, dst):
    global move_count

    # Base Case
    if n == 1:
        print(f"Move disk 1 from {src} -> {dst}")
        move_count += 1
        return

    # Recursive Case
    hanoi(n-1, src, dst, aux)     # Move n-1 disks to auxiliary
    print(f"Move disk {n} from {src} -> {dst}")
    move_count += 1
    hanoi(n-1, aux, src, dst)     # Move n-1 disks to destination


# -----------------------------
# Move sequence for n = 3
# -----------------------------
print("Move sequence for n = 3:\n")
move_count = 0
hanoi(3, 'A', 'B', 'C')
print("\nTotal moves for n=3:", move_count)


# -----------------------------
# Move count for n = 4
# -----------------------------
move_count = 0
hanoi(4, 'A', 'B', 'C')
print("\nTotal moves for n=4:", move_count)