f = open('input.txt', 'r')

sum = 0

for l in f.readlines():
    first = -1
    second = -1
    line = l.strip()
    for i in range(len(line)):
        num = -1
        if line[i:].startswith("1") or line[i:].startswith("one"):
            num = 1
        elif line[i:].startswith("2") or line[i:].startswith("two"):
            num = 2
        elif line[i:].startswith("3") or line[i:].startswith("three"):
            num = 3
        elif line[i:].startswith("4") or line[i:].startswith("four"):
            num = 4
        elif line[i:].startswith("5") or line[i:].startswith("five"):
            num = 5
        elif line[i:].startswith("6") or line[i:].startswith("six"):
            num = 6
        elif line[i:].startswith("7") or line[i:].startswith("seven"):
            num = 7
        elif line[i:].startswith("8") or line[i:].startswith("eight"):
            num = 8
        elif line[i:].startswith("9") or line[i:].startswith("nine"):
            num = 9
        elif line[i:].startswith("0"):
            num = 0

        if num != -1:                
            if first == -1:
                first = 10*num
            second = num

    sum += first + second
                
print(sum)
