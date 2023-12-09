import sys

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0

    for line in data:
        numbers = [int(x) for x in line.split()]

        allzero = False
        predicted=0
        while not allzero:
            allzero=True
            newnumbers = []
            for i in range(0, len(numbers)-1, 1):
                diff = numbers[i+1]-numbers[i]
                if diff != 0:
                    allzero = False

                newnumbers.append(diff) # work on new set

                if i == len(numbers)-2: # precticted number is a sum of last item in each iteration
                    predicted+=numbers[i+1]
                    
            numbers = newnumbers.copy()
            newnumbers = []

        ans += predicted

    print(ans) # 1842168671

if __name__ == "__main__":
    main()