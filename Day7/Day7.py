import operator
try:
    with open("Day7/Day7_Inp.txt", "r") as file:
        data = file.read().splitlines()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

total = 0

def dfs(numbers, ops, current_expression, index, current_result, results, target):
    if index == len(numbers):
        # If the last operation gives the target, save the result and return
        if current_result == target:
            results.append(current_expression)
            return True
        return False

    # Recur for all operators
    for op in ops:
        next_number = numbers[index]
        
        # Calculate the result of the operation
        if op == '+':
            new_result = current_result + next_number
        elif op == '*':
            new_result = current_result * next_number
        else:
            continue

        # Create the new expression
        new_expression = f"{current_expression}{op}{next_number}"

        # Recursively evaluate the next step
        if dfs(numbers, ops, new_expression, index + 1, new_result, results, target):
            return True  # Stop as soon as a solution is found

    return False

def brute_force_operators(numbers, target):
    operators = ['+', '*']
    results = []

    # Start DFS with the first number as the initial result
    dfs(numbers, operators, str(numbers[0]), 1, numbers[0], results, target)

    # Return results if any, else 0
    return target if results else 0

for line in data:
    line_nums = line.split(" ")
    t = line_nums[0].split(":")
    target = int(t[0])
    nums = list(map(int, line_nums[1:])) 
    results = brute_force_operators(nums, target)
    total += results
    

print(f"Part 1 total: {total}")