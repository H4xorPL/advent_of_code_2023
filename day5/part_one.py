import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0 
    seeds = data[0].removeprefix('seeds: ').split()

    changed = defaultdict(bool)

    for line in filter(None, data[1:]):
        if not line[0].isdigit():
            changed = defaultdict(bool)
            continue
        dest, src, range = line.split()
        for i, seed in enumerate(seeds):
            if int(seed) >= int(src) and int(seed) <int(src)+int(range) and not changed[i]:
                seed = int(seed)+ int(dest)-int(src)
                seeds[i] = seed
                changed[i]=True

    seeds.sort()
    ans = seeds[0]
    print(ans) # 525792406

if __name__ == "__main__":
    main()