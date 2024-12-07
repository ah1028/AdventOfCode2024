from urllib.request import Request, urlopen
import numpy as np

url = "https://adventofcode.com/2024/day/6/input"

# Create a request with the session cookie in the headers
request = Request(url)
request.add_header("Cookie", f"session={SESSION_COOKIE}")
request.add_header("User-Agent", "Python urllib for Advent of Code")

# Fetch the page
try:
    with urlopen(request) as response:
        html_bytes = response.read()
        html = html_bytes.decode("utf-8")
        data = html.splitlines()
except Exception as e:
    print(f"An error occurred: {e}")

x, y = 0, 0
not_found = True

while not_found:
    if "^" in data[y]:
        x = data[y].index("^")
        not_found = False
    else:
        y += 1


visited = [(x,y)]
dir = "N"

while x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
    print(x, y, dir)
    match dir:
        case "N":
            if y-1 < 0:
                y -= 1
            elif data[y-1][x] == ".":
                y -= 1
                if (x,y) not in visited:
                    visited.append((x,y))
            else:
                dir = "E"
        case "E":
            if x+1 >= len(data[0]):
                x += 1
            elif data[y][x+1] == ".":
                x += 1
                if (x,y) not in visited:
                    visited.append((x,y))
            else:
                dir = "S"
        case "S":
            if y+1 >= len(data):
                y += 1
            elif data[y+1][x] == ".":
                y += 1
                if (x,y) not in visited:
                    visited.append((x,y))
            else:
                dir = "W"
        case "W":
            if x-1 < 0:
                x -= 1
            elif data[y][x-1] == ".":
                x -= 1
                if (x,y) not in visited:
                    visited.append((x,y))
            else:
                dir = "N"


print(len(visited))