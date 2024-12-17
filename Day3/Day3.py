import re

# Read and process the file
try:
    with open("Day3/Day3_Inp.txt", "r") as file:
        data = file.read()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

regex = "mul\(\d+,\d+\)"
ops = re.findall(regex, data)
total = 0
for op in ops:
    num1, num2 = re.findall("\d+", op)
    total += int(num1) * int(num2)

print(f"Total {total}")

new_regex = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
ops = re.findall(new_regex, data)
flag = True
new_total = 0
for op in ops:
    if op == "do()":
        flag = True
    elif op == "don't()":
        flag = False
    elif flag:
        num1, num2 = re.findall("\d+", op)
        new_total += int(num1) * int(num2)

print(f"Total {new_total}")