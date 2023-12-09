import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans=0

    instructions = data[0]

    class Node:
        def __init__(self,val, left, right) -> None:
            self.val = val
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return f'{self.val} = ({self.left}, {self.right})'
            

    nodes = defaultdict(Node)
    for node in data[2:]:
        val,other = node.split(' = ')

        left, right = other.split(', ')

        print(f'{left[1:]},{right[:3]}')
        nodes[val] = Node(val, left[1:], right[:3])
        print(nodes[val])

    next = "AAA"
    while next != "ZZZ":
        print('once?')
        for instruction in instructions:
            if instruction == "L":
                print('L')
                next = nodes[next].left
            else:
                print('R')
                next = nodes[next].right
            ans+=1
        print(f'next {next}')

    print(ans) # 16697

if __name__ == "__main__":
    main()