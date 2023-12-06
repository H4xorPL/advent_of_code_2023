import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0 
    seeds = data[0].removeprefix('seeds: ').split()
        
    items = []
    for i in range(1,len(seeds),2):
        items.append([int(seeds[i-1]), int(seeds[i-1])+int(seeds[i])])

    next_mapping = []
    new_items = []
    for line in filter(None, data[1:]):
        if not line[0].isdigit():
            if next_mapping != []:
                for new_item in new_items:
                    next_mapping.append(new_item)
                print(f'items {items} next_mapping {next_mapping}')
                items = next_mapping.copy()
                next_mapping = []
                new_items=[]
            continue
        dest, src, range_len = line.split()
        
        if new_items != []:
            items = new_items.copy()
            new_items=[]
        for item in items:
            op = int(dest)-int(src)
            src_min = int(src)
            src_max = src_min + int(range_len)

            lower = int(item[0])
            upper = int(item[1])

            if src_min <= lower and src_max >= upper:
                print('take whole')
                print(src_min, src_max, lower,upper)
                next_mapping.append([lower+op, upper+op])
                print(f'for numbers {lower}->{upper} and boundary {src_min}->{src_max}')
                print(f'I am taking {lower}->{upper} to next_mapping as {lower+op}->{upper+op} as diff={op}')
                print(f'and nothing to new_items')
                print(40*"=")
            elif src_min > lower and src_min <= upper and src_max <= upper and src_max >= lower:
                print('cut out part')
                print(src_min, src_max, lower,upper)
                next_mapping.append([max(lower,src_min)+op, min(upper, src_max)+op])
                new_items.append([lower, max(lower,src_min)])
                new_items.append([min(upper, src_max), upper])
                print(f'for numbers {lower}->{upper} and boundary {src_min}->{src_max}')
                print(f'I am taking {max(lower,src_min)}->{min(upper, src_max)} to next_mapping as {max(lower,src_min)+op}->{min(upper, src_max)+op} as diff={op}')
                print(f'and {lower}->{max(lower,src_min)} and {min(upper, src_max)}->{upper} to new_items')
                print(40*"=")
            elif src_min <= lower and src_max >= lower and src_max < upper:
                print('just beginning')
                print(src_min, src_max, lower,upper)
                next_mapping.append([lower+op, src_max+op])
                new_items.append([src_max, upper])
                print(f'for numbers {lower}->{upper} and boundary {src_min}->{src_max}')
                print(f'I am taking {lower}->{src_max} to next_mapping as {lower+op}->{src_max+op} as diff={op}')
                print(f'and {src_max}->{upper} to new_items')
                print(40*"=")
            elif src_min > lower and src_min <= upper and src_max >= upper:
                print('just end')
                print(src_min, src_max, lower,upper)
                next_mapping.append([src_min+op, upper+op])
                new_items.append([lower, src_min])
                print(f'for numbers {lower}->{upper} and boundary {src_min}->{src_max}')
                print(f'I am taking {src_min}->{upper} to next_mapping as {src_min+op}->{upper+op} as diff={op}')
                print(f'and {lower}->{src_min} to new_items')
                print(40*"=")
            else:
                print('ignoring')
                print(src_min, src_max, lower,upper)
                new_items.append([lower,upper])
                print(f'for numbers {lower}->{upper} and boundary {src_min}->{src_max}')
                print(f'I am taking nothing to next_mapping')
                print(f'and {lower}->{upper} to new_items')
                print(40*"=")

    print(f'THE END')
    for i in new_items:
        next_mapping.append(i)
    next_mapping.sort()
    print(f'new_items {new_items} next_mapping {next_mapping}')
    ans = next_mapping[0][0]
    print(ans) # 79004094

if __name__ == "__main__":
    main()