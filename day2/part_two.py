lines = open('part_two_input.txt', 'r').readlines()

sum = 0

for line in lines:
    line = line.strip('\n')
    # `Game: ` 
    # and 
    # `3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green`
    items = line.split(':')


    # `3 blue, 4 red`
    # and
    # `1 red, 2 green, 6 blue`
    # and
    # `2 green`
    draws = items[1].split('; ')
    red = 0
    green = 0
    blue = 0
    for draw in draws:
        # `3 blue`
        # and
        # `4 red`
        cubes = draw.split(', ')
        for cube in cubes:
            cube = cube.removeprefix(' ')
            # `3`  splits[0]
            # and
            # `blue` splits[1]
            splits = cube.split(' ')

            if splits[1] == 'red':
                if int(splits[0]) > red:
                    red = int(splits[0])
            elif splits[1] == 'green':
                if int(splits[0]) > green:
                    green = int(splits[0])
            elif splits[1] == 'blue':
                if int(splits[0]) > blue:
                    blue = int(splits[0])
                
    sum = sum + ((red) * (blue) * (green))


print(sum)

# 66909
# python3 part_two.py  0.02s user 0.01s system 99% cpu 0.027 total