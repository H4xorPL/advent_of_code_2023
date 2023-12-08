import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0

    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards.reverse()

    def cardindex(item):
        hand = item.split()[0]
        cardval = 0
        seen = defaultdict(int)
        for i, cardinhand in enumerate(hand):
            cardval += cards.index(cardinhand)*(10**(2*(5-i)))
            seen[cardinhand] += 1
        
        for x in seen:
            cardval += 10000000000000 * (seen[x]**2)
        return cardval


    data.sort(key=cardindex)

    for i, x in enumerate(data):
        seen2 = defaultdict(int)
        for cardinhand in x.split()[0]:
            seen2[cardinhand] += 1
        seen2= {k: v for k, v in sorted(seen2.items(), key=lambda item: item[1], reverse=True)}
        print(x[:5], seen2)
        bid = x.split()[1]
        ans += int(bid)*(i+1)

    print(ans) # 250474325

if __name__ == "__main__":
    main()