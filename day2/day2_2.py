f = open('input.txt', 'r')

sum = 0

for l in f.readlines():
    greens = 0
    blues = 0
    reds = 0
    line = l.strip().replace("Game ", "")
    game, sets = line.split(":")
    for set in sets.split(";"):
        for color in set.split(","):
            amount, type = color.strip().split(" ")
            if type == "green" and int(amount) > greens:
                greens = int(amount)
            if type == "blue" and int(amount) > blues:
                blues = int(amount)
            if type == "red" and int(amount) > reds:
                reds = int(amount)
    sum += greens * blues * reds
                
print(sum)

