import sys
from collections import defaultdict

def main() -> None:
    data = sys.stdin.read().strip().split('\n')
    ans=1 # start with one as a step

    instructions = data[0]

    class Node:
        def __init__(self,val, left, right) -> None:
            self.val = val
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return f'{self.val} = ({self.left}, {self.right})'
            

    nodes = defaultdict(Node)
    startingnodes = []
    for node in data[2:]:
        val,other = node.split(' = ')

        left, right = other.split(', ')

        nodes[val] = Node(val, left[1:], right[:3])
        if val[2] == "A":
            startingnodes.append(val)

    gotZ = defaultdict(int)
    D = False
    while not D:
        newNodes = []
        for instruction in instructions:
            for i, currentNode in enumerate(startingnodes):
                if instruction == "L":
                    newNodes.append(nodes[currentNode].left)
                    if nodes[currentNode].left[2] == 'Z' and not gotZ[i]:
                        gotZ[i] = ans
                else:
                    newNodes.append(nodes[currentNode].right)
                    if nodes[currentNode].right[2] == 'Z' and not gotZ[i]:
                        gotZ[i] = ans
            ans+=1
            startingnodes = newNodes.copy()
            newNodes = []
        if len(gotZ)==len(startingnodes):
          D =True
    # find greatest common denominator
    def findGCD(x,y):
        while x != y:
            if x > y:
                x, y  = x-y, y
            else:
                x,y = x, y-x
        return x
        
    # find least common multiplier
    def findLCM(x,y):
        return int((x*y)/findGCD(x,y))
    
    ans = findLCM(findLCM(findLCM(findLCM(findLCM(gotZ[0], gotZ[1]),gotZ[2]), gotZ[3]),gotZ[4]),gotZ[5])
    
    print(ans) # 10668805667831


if __name__ == "__main__":
    main()
