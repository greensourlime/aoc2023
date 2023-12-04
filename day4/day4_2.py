f = open('input.txt', 'r')

suma = 0
card_num = 0
card_count = {1:1}
for l in f.readlines():
    card_num += 1
    if card_num not in card_count.keys():
        card_count[card_num] = 1

    _, line = l.strip().split(": ")
    winning, owned = line.split("|")
    w = set([int(e.strip()) for e in winning.split()])
    o = set([int(e.strip()) for e in owned.split()])

    common = len(w.intersection(o))
    for i in range(card_num+1, card_num+1+common, 1):
        if i not in card_count:
            card_count[i] = 1 + card_count[card_num]
        else:
            card_count[i] += card_count[card_num]

suma = sum(card_count.values())
print(str(suma))
