with open("Day5/rules.txt", "r") as f:
    rules = [l.strip() for l in f.readlines()]
with open("Day5/pages.txt","r") as f:
    pages = [l.strip() for l in f.readlines()]

edges = {}
for line in rules:
    first, second = map(str.strip, line.split("|"))
    if second not in edges:
        edges[second] = [first]
    else:
        temp = edges[second] + [first]
        edges[second] = temp

def validity(pages):
    valid = []
    not_valid = []
    for page in pages:
        v = True
        pg = page.split(",")
        for a in range(0, len(pg)):
            entries = edges.get(pg[a])
            if entries != None:
                pg[a] = ""
                res = (set(entries)).intersection(set(pg))
                if res:
                    v = False
                    break
            pg[a] = ""
        if v:
            valid.append(page)
        else:
            not_valid.append(page)
    return valid, not_valid

valid, not_valid = validity(pages)
total = 0
for b in valid:
    b = b.split(",")
    mid = (len(b) - 1) // 2
    total += int(b[mid])

print(total)



# def rearrange_list(given_list, dependency_dict):
#     # Copy the given list to preserve the original order while rearranging
#     print(given_list)
#     result = given_list[:]
#     print(result)
    
#     # Iterate through the keys in the dictionary
#     for key, values in dependency_dict.items():
#         if key in result:
#             key_index = result.index(key)
#             for value in values:
#                 if value in result:
#                     value_index = result.index(value)
#                     # If value comes after the key, move it before
#                     if value_index > key_index:
#                         # Remove the value and reinsert it before the key
#                         result.pop(value_index)
#                         key_index = result.index(key)  # Update key_index after modification
#                         result.insert(key_index, value)
    
#     return result

temp = []
# for entry in not_valid:
#     entry = entry.split(",")
#     res = rearrange_list(entry, edges)
#     temp.append(res)


new_total = 0
for c in temp:
    mid = (len(c) - 1) // 2
    new_total += int(c[mid])

print(new_total)