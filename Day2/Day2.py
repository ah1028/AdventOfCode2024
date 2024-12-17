import numpy as np

# Read and process the file
try:
    with open("Day2/Day2_Inp.txt", "r") as file:
        data = [list(map(int, line.split())) for line in file.readlines() if line.strip()]
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

count = 0
unsafe = []

for report in data:
    sign = False
    prev = None
    for a in range(0, len(report)-1):
        diff = report[a] - report[a+1]
        if abs(diff) < 1 or abs(diff) > 3:
            sign = True
        elif a != 0 and np.sign(diff) != prev:
            sign = True
        else:
            prev = np.sign(diff)
    if sign:
        unsafe.append(report)
        continue
    else:
        count += 1

print(f"Safe reports: {count} - part 1")

# Part 2
newCount = 0
def is_safe_array(arr):
    def is_valid(arr):
        # Check if the differences between adjacent items are between 1 and 3
        diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        return all(1 <= abs(diff) <= 3 for diff in diffs) and all(np.sign(diffs[0]) == np.sign(d) for d in diffs)
    
    # Check the full array
    if is_valid(arr):
        return True

    # Check if removing one item makes the array valid
    for i in range(len(arr)):
        modified_arr = arr[:i] + arr[i+1:]
        if is_valid(modified_arr):
            return True

    # If neither the original nor any modified version is valid
    return False

def count_safe_arrays(arrays):
    safe_count = 0
    for arr in arrays:
        if is_safe_array(arr):
            safe_count += 1
    return safe_count

newCount = count_safe_arrays(unsafe)

print(f"Total safe arrays: {newCount + count}")