f = open('input.txt', 'r')

sum = 0
for l in f.readlines():
    first = -1
    second = -1
    for c in l.strip():
        if c.isdigit():
            if first == -1:
                first = 10 * int(c)
            second = int(c)
    sum += first + second                
print(sum)
