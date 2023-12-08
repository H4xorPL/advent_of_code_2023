import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans = 0

    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    cards.reverse()

    def cardindex(item):
        hand = item.split()[0]
        cardval = 0
        jokers = 0
        seen = defaultdict(int)
        for i, cardinhand in enumerate(hand):
            cardval += cards.index(cardinhand)*(10**(2*(5-i)))
            if cardinhand == 'J':
                jokers+=1
            else:
                seen[cardinhand] += 1
        seen = {k: v for k, v in sorted(seen.items(), key=lambda item: item[1], reverse=True)}
        # if all jokers, treat them as 5-match
        if jokers == 5:
            seen['J']=0
        for i, x in enumerate(seen):
            val = seen[x]
            if i == 0:
                val+=jokers
            cardval += 10000000000000 * (val**2)
        return cardval


    data.sort(key=cardindex)

    for i, x in enumerate(data):
        bid = x.split()[1]
        ans += int(bid)*(i+1)

    print(ans) # 248909434

if __name__ == "__main__":
    main()