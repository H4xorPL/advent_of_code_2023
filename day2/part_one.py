input = open('part_one_input.txt', 'r')
lines = input.readlines()

sum = 0
red = 12
green = 13
blue = 14

for line in lines:
    ok = True
    line = line.strip('\n')
    items = line.split(':')

    draws = items[1].split('; ')

    for draw in draws:
        cubes = draw.split(', ')
        for cube in cubes:
            cube = cube.removeprefix(' ')
            splits = cube.split(' ')
            max_cubes = 0
            if splits[1] == 'red':
                max_cubes=red
            elif splits[1] == 'green':
                max_cubes=green
            elif splits[1] == 'blue':
                max_cubes=blue
            if int(splits[0]) > max_cubes:
                ok = False
                break
        if not ok:
            break

                
    if ok:
        sum = sum + int(items[0].removeprefix('Game '))


print(sum)

# 2156
# python3 part_one.py  0.02s user 0.00s system 98% cpu 0.021 total