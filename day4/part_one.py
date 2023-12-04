import sys

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0 

    for line in data:
        winning, have = line.split(': ')[1].split(' | ')

        start = 0.5

        for h in have.split():
            if h in winning.split():
                start *= 2
        
        if start > 0.5:
            ans += int(start)


    print(ans) # 23028

if __name__ == "__main__":
    main()