import networkx as nx
import matplotlib.pyplot as plt

with open("rules.txt", "r") as f:
    rules = [l.strip() for l in f.readlines()]
with open("pages.txt","r") as f:
    pages = [l.strip() for l in f.readlines()]

edges = {}
for line in rules:
    first, second = map(str.strip, line.split("|"))
    if second not in edges:
        edges[second] = [first]
    else:
        temp = edges[second] + [first]
        edges[second] = temp


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

total = 0
for b in valid:
    b = b.split(",")
    mid = (len(b) - 1) // 2
    total += int(b[mid])

print(total)

for entry in not_valid:
    entry = entry.split(",")
    for a in range(0, len(entry)):
        entries = edges.get(entry[a])
        if entries != None:
            res = (set(entries)).intersection(set(pg))
             
            