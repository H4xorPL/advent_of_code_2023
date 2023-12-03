lines = open('input.txt', 'r').readlines()

engine_part_number=0

all_symbols = []

for l, line in enumerate(lines):
    line = line.strip('\n')
    symbols = []
    for i, char in enumerate(line):
        if char.isdigit():
            continue
        elif char == '.':
            continue
        else:
            symbols.append(i)

    all_symbols.append(symbols)

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
            for x in range(indexes[0]-1, indexes[len(indexes)-1]+2, 1):
                if x>-1 and x<len(line):
                    if l-1>-1 and x in all_symbols[l-1]:    
                        engine_part_number+=int(number)

                    if x in all_symbols[l]:    
                        engine_part_number+=int(number)

                    if l+1<len(all_symbols) and x in all_symbols[l+1]:
                        engine_part_number+=int(number)
            if not char.isdigit():
                number=''
                indexes=[]

print(engine_part_number)

# 546312
# python3 part_one.py  0.03s user 0.00s system 98% cpu 0.033 total
