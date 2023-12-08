import sys

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0
    times, distances = data
    t = int(times.removeprefix('Time:').replace(' ', ''))
    d = int(distances.removeprefix('Distance:').replace(' ', ''))

    for x in range(0, t+1, 1):
        if (t-x)*x > d:
            ans+=1

    print(ans) # 35150181

if __name__ == "__main__":
    main()