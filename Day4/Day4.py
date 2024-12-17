global data

# Read and process the file
try:
    with open("Day4/Day4_Inp.txt", "r") as file:
        data = file.read().splitlines()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

total = 0

def check(x, y, i, dir="E"):
    word = "XMAS"
    if i == 4:
        return True
    elif x >= len(data[0]) or y >= len(data) or x < 0 or y < 0:
        return False
    
    match dir:
        case "E":
            if word[i] == data[y][x]:
                return check(x+1, y, i+1, "E")
            else:
                return False
        case "W":
            if word[i] == data[y][x]:
                return check(x-1, y, i+1, "W")
            else:
                return False
        case "N":
            if word[i] == data[y][x]:
                return check(x, y-1, i+1, "N")
            else:
                return False
        case "S":
            if word[i] == data[y][x]:
                return check(x, y+1, i+1, "S")
            else:
                return False
        case "NE":
            if word[i] == data[y][x]:
                return check(x+1, y-1, i+1, "NE")
            else:
                return False
        case "SE":
            if word[i] == data[y][x]:
                return check(x+1, y+1, i+1, "SE")
            else:
                return False
        case "NW":
            if word[i] == data[y][x]:
                return check(x-1, y-1, i+1, "NW")
            else:
                return False
        case "SW":
            if word[i] == data[y][x]:
                return check(x-1, y+1, i+1, "SW")
            else:
                return False
        case _:    
            return False

dirs = ["N", "NE","E","SE","S","SW","W","NW"]

for a in range(0, len(data)):
    for b in range(0, len(data[a])):
        for dir in dirs:
            if check(b, a, 0, dir):
                total +=1

print(total)

new_total = 0

for c in range(1, len(data)-1):
    for d in range(1, len(data[c])-1):
        if data[c][d] == "A":
            if data[c-1][d-1] == "M" and data[c+1][d+1] == "S":
                if data[c-1][d+1] == "M" and data[c+1][d-1] == "S":
                    new_total += 1
                elif data[c-1][d+1] == "S" and data[c+1][d-1] == "M":
                    new_total += 1
            if data[c-1][d-1] == "S" and data[c+1][d+1] == "M":
                if data[c-1][d+1] == "M" and data[c+1][d-1] == "S":
                    new_total += 1
                elif data[c-1][d+1] == "S" and data[c+1][d-1] == "M":
                    new_total += 1

print(new_total)
