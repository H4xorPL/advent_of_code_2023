import sys

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0

    games = []

    extra = 0
    
    for _ in range(len(data)):
        games.append(1)

    for i, line in enumerate(data):
        extra = 0
        winning, have = line.split(': ')[1].split(' | ')

        for h in have.split():
            if h in winning.split():
                extra += 1
                games[i+extra] += 1*games[i]
    
    for game in games:
        ans += game

    print(ans) # 9236992

if __name__ == "__main__":
    main()