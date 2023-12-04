f = open('input.txt', 'r')

sum = 0
for l in f.readlines():
    _, line = l.strip().split(": ")
    winning, owned = line.split("|")
    w = set([int(e.strip()) for e in winning.split()])
    o = set([int(e.strip()) for e in owned.split()])
    common = len(w.intersection(o))
    if (common > 0):
        sum += pow(2, common-1)

print(sum)
