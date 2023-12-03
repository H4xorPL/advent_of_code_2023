lines = open('input.txt', 'r').readlines()

gear_part_number=0

all_symbols = []

adjacent = dict()

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjacent(self, x, y):
        if x >= self.x-1 and x <= self.x+1 and y >= self.y-1 and y <= self.y+1:
            return True
        return False
    
    def __str__(self) -> str:
        return f'y: {self.y+1}, x: {self.x+1}'

for l, line in enumerate(lines):
    line = line.strip('\n')
    symbols = []
    for i, char in enumerate(line):
        if char == '*':
            all_symbols.append(Coords(i, l))

for l, line in enumerate(lines):
    line = line.strip('\n')
    number = ''
    indexes = []
    for i, char in enumerate(line):
        if char.isdigit():
            number += char
            indexes.append(i)
            if i != len(line)-1:
                continue
        if number != '':
            found = False
            for x in range(indexes[0], indexes[len(indexes)-1]+1, 1):
                for coord in all_symbols:
                    if coord.adjacent(x,l):
                        found = True
                        if adjacent.get(coord) != None:
                            gear_part_number+=(int(number)*adjacent.get(coord))
                        else:
                            adjacent[coord] = int(number)

                if found:
                    break

            if not char.isdigit():
                number=''
                indexes=[]

print(gear_part_number)

# 87449461
# python3 part_two.py  0.18s user 0.01s system 99% cpu 0.193 total
