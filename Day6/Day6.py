try:
    with open("Day6/Day6_Inp.txt", "r") as file:
        data = file.read().splitlines()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


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


print(f"Number of distinct positions: {len(visited)}")