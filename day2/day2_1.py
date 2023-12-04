f = open('input.txt', 'r')

MAX_GREEN = 13
MAX_BLUE = 14
MAX_RED = 12

sum = 0

for l in f.readlines():
    imposible = False
    line = l.strip().replace("Game ", "")
    game, sets = line.split(":")
    for set in sets.split(";"):
        for color in set.split(","):
            amount, type = color.strip().split(" ")
            if type == "green" and int(amount) > MAX_GREEN:
                imposible = True
            if type == "blue" and int(amount) > MAX_BLUE:
                imposible = True
            if type == "red" and int(amount) > MAX_RED:
                imposible = True
    if not imposible:
        sum += int(game)
                
print(sum)
