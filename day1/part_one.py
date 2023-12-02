input_one = open('part_one_input.txt', 'r')
lines = input_one.readlines()

sum = 0

def isnumber(char):
    if char == '0':
        print('zero')

for line in lines:
    line = line.replace('\n', '')
    first=''
    last=''
    for char in line:
        if char.isdigit():
            first=char
            break
    for i in range(len(line),0, -1):
        char2 = line[i-1]
        if char2.isdigit():
            last=char2
            break
    sum = int(first+last) + sum


print(sum)

# 54239
# python3 part_one.py  0.03s user 0.01s system 99% cpu 0.034 total