import numpy as np

list1, list2 = [], []

# Read and process the file
try:
    with open("Day1/Day1_Inp.txt", "r") as file:
        for line in file:
            # Split each line into two numbers
            parts = line.strip().split()
            if len(parts) == 2:
                list1.append(parts[0])
                list2.append(parts[1])
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


list1 = sorted(list1)
list2 = sorted(list2)

l1 = np.array(list1, dtype=int)
l2 = np.array(list2, dtype=int)


res = np.sum(np.absolute(l1 - l2))
print(f"Stage 1 results: {res}")

total, i, prev = 0, 0, None

for row in l1:
    if row == prev:
        total += row * t
    t = 0
    while row > l2[i]:
        i += 1
    if row == l2[i]:
        t = 1
        i += 1
        while i < len(l2) and row == l2[i]:
            t += 1
            i += 1
        total += row * t

        if i >= len(l2):
            break

print(f"Stage 2 results: {total}")