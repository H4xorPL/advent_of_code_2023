input_one = open('part_two_input.txt', 'r')
lines = input_one.readlines()

sum = 0

def word_to_number(word):
    if word == 'one':
        return '1'
    elif word == 'two':
        return '2'
    elif word == 'three':
        return '3'
    elif word == 'four':
        return '4'
    elif word == 'five':
        return '5'
    elif word == 'six':
        return '6'
    elif word == 'seven':
        return '7'
    elif word == 'eight':
        return '8'
    elif word == 'nine':
        return '9'
    else:
        return ''
    
def digit_in_word(s, i):
    if s.startswith('one',i):
        return '1'
    elif s.startswith('two',i):
        return '2'
    elif s.startswith('three',i):
        return '3'
    elif s.startswith('four',i):
        return '4'
    elif s.startswith('five',i):
        return '5'
    elif s.startswith('six',i):
        return '6'
    elif s.startswith('seven',i):
        return '7'
    elif s.startswith('eight',i):
        return '8'
    elif s.startswith('nine',i):
        return '9'
    else:
        return ''

def digit_in_word_reverse(s, i):
    if s.endswith('one',None,i):
        return '1'
    elif s.endswith('two',None,i):
        return '2'
    elif s.endswith('three',None,i):
        return '3'
    elif s.endswith('four',None,i):
        return '4'
    elif s.endswith('five',None,i):
        return '5'
    elif s.endswith('six',None,i):
        return '6'
    elif s.endswith('seven',None,i):
        return '7'
    elif s.endswith('eight',None,i):
        return '8'
    elif s.endswith('nine',None,i):
        return '9'
    else:
        return ''

for line in lines:
    line = line.replace('\n', '')
    first=''
    last=''
    for i in range(0, len(line), 1):
        char = line[i]
        if char.isdigit():
            first=char
            break
        digit = digit_in_word(line, i)
        if digit != '':
            first = digit
            break

    for i in range(len(line), 0, -1):
        char2 = line[i-1]
        if char2.isdigit():
            last=char2
            break
        digit2 = digit_in_word_reverse(line, i)
        if digit2 != '':
            last=digit2
            break

    sum = int(first+last) + sum


print(sum)


# 55343
# python3 part_two.py  0.03s user 0.01s system 99% cpu 0.038 total