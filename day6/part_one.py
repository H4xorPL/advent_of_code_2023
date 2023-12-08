import sys

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 1 
    times, distances = data
    times = [int(x) for x in times.removeprefix('Time:').split()]
    distances = [int(x) for x in distances.removeprefix('Distance:').split()]

    for i, t in enumerate(times):
        ways = 0
        for x in range(0, t+1, 1):
            if (t-x)*x > distances[i]:
                ways+=1
        ans*=ways



    print(ans) # 293046

if __name__ == "__main__":
    main()