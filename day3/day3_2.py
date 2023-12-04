import re

class Number:
    def __init__(self, value, start_position, end_position, line_number):
        self.value = value
        self.start_position = start_position
        self.end_position = end_position
        self.line_number = line_number

class Symbol:
    def __init__(self, character, position, line_number):
        self.character = character
        self.position = position
        self.line_number = line_number


f = open('input.txt', 'r')

numbers = []
symbols = []

line_count = 0
for l in f.readlines():
    line = l.strip()
    line_count += 1

    matches = re.finditer(r'\d+', line)
    for match in matches:
        number = int(match.group())
        start_position = match.start()
        end_position = match.end() - 1        
        numbers.append(Number(number, start_position, end_position, line_count))

    re.compile(r'[^.\d]').finditer(line)

    matches = re.finditer(r'[^.\d]', line)
    for match in matches:
        character = match.group()
        position = match.start()
        symbols.append(Symbol(character, position, line_count))

sum = 0
for symbol in symbols:
    if symbol.character == "*":
        numbers_around = 0
        ratio = 1
        for number in numbers:
           if abs(symbol.line_number - number.line_number) <= 1:
               if symbol.position >= number.start_position-1 and symbol.position <= number.end_position+1:
                   if numbers_around < 2:
                       ratio *= number.value
                       numbers_around += 1
        if numbers_around == 2:
            sum += ratio 

print(sum)
