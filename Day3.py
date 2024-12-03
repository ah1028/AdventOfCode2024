from urllib.request import Request, urlopen
import numpy as np
import re

url = "https://adventofcode.com/2024/day/3/input"
SESSION_COOKIE = ""

# Create a request with the session cookie in the headers
request = Request(url)
request.add_header("Cookie", f"session={SESSION_COOKIE}")
request.add_header("User-Agent", "Python urllib for Advent of Code")

# Fetch the page
try:
    with urlopen(request) as response:
        html_bytes = response.read()
        html = html_bytes.decode("utf-8")
except Exception as e:
    print(f"An error occurred: {e}")

regex = "mul\(\d+,\d+\)"
ops = re.findall(regex, html)
total = 0
for op in ops:
    num1, num2 = re.findall("\d+", op)
    total += int(num1) * int(num2)

print(f"Total {total}")

new_regex = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
ops = re.findall(new_regex, html)
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