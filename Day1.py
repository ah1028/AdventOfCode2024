from urllib.request import Request, urlopen
import numpy as np

url = "https://adventofcode.com/2024/day/1/input"
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
        data = (html.replace("\n", " ")).split(" ")
        list1, list2 = [], []
        for a in range(0, len(data)-1, 4):
            list1.append(data[a])
            list2.append(data[a+3])
except Exception as e:
    print(f"An error occurred: {e}")

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