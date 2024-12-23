try:
    with open("Day8/Day8_Inp.txt", "r") as file:
        data = file.read().splitlines()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

antinodes = []

for row in range(0, len(data)):
    for col in range(0, len(data[0])):
        if data[row][col] != ".":
            freq = data[row][col]
            instances = [(i, j) for i, r in enumerate(data) for j, element in enumerate(r) if element == freq]
            instances.remove((row, col))
            for a, b in instances:
                x = col + 2*(b-col)
                y = row + 2*(a-row)
                if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data) and (y, x) not in antinodes:
                    antinodes.append((y, x))
        
print(f"{len(antinodes)} Unique anti-node locations")