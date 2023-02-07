import sys
h = {
        "A": 9,
        "B": 7,
        "C": 5,
        "D": 0,
        "E": 4,
        "F": 5
}

G = {
        "A": {"B": 2, "C": 2},
        "B": {"A": 2, "D": 2, "E": 2},
        "C": {"A": 2, "F": 2},
        "D": {"B": 2},
        "E": {"B": 2, "F": 2},
        "F": {"C": 2, "E": 2},
    }


start = "A"
goal = "D"

curr = start
closed = []
path = [start]
pathCostTillNow = 0
def f(node,neighbor,pathCostTillNow):
    return pathCostTillNow+G[node][neighbor] + h[neighbor]
def a_star(start,goal,pathCostTillNow):
    if start == goal:
        return [start]
    while start!=None:
        nodeToCheck = start
        minCost = sys.maxsize
        minNode = None
        for node in G[nodeToCheck]:
            if node not in closed:
                cost = f(nodeToCheck,node,pathCostTillNow)
                if cost < minCost:
                    minCost = cost
                    minNode = node
        if minNode:
            start = minNode 
            path.append(minNode)
            pathCostTillNow += G[nodeToCheck][minNode]
            if minNode == goal:
                return path
        else:
            start = None
        closed.append(nodeToCheck)

    return None

print(a_star(start,goal,pathCostTillNow))