try:
    with open("Day8/Day8_Inp.txt", "r") as file:
        data = file.read().splitlines()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

global antinodes
antinodes = []

def propagate_antis(instances, row, col):
    for a, b in instances:
        x = col + 2*(b-col)
        y = row + 2*(a-row)
        if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data) and (y, x) not in antinodes:
            antinodes.append((y, x))

def propagate_antis_pt2(a, b, row, col, multi):
    x = col + multi*(b-col)
    y = row + multi*(a-row)
    if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
        if (y, x) not in antinodes:
            antinodes.append((y, x))
            propagate_antis_pt2(a, b, row, col, multi+1)
        else:
            propagate_antis_pt2(a, b, row, col, multi+2)

for row in range(0, len(data)):
    for col in range(0, len(data[0])):
        if data[row][col] != "." and data[row][col] != "#":
            freq = data[row][col]
            instances = [(i, j) for i, r in enumerate(data) for j, element in enumerate(r) if element == freq]
            instances.remove((row, col))
            if (row, col) not in antinodes:
                antinodes.append((row, col))
            for a, b in instances:
                if (a, b) not in antinodes:
                    antinodes.append((a, b))
                propagate_antis_pt2(a, b, row, col, 2)

print(f"{len(antinodes)} Unique anti-node locations")