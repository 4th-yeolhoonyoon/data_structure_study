graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]}
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}
graph3 = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}
node_from = {node: "" for node in graph3}
print(node_from)


def bfs(graph, node):
    res = []
    queue = [node]
    visited = set(queue)
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v, w in graph[u]:
            if v not in visited:
                node_from[v] = u
                visited.add(v)
                queue.append(v)
    return res


print("탐색 전의 node_from의 상태")
print(node_from)
print()
print("너비 우선 탐색 결과: ", bfs(graph3, "A"))
print()
print("탐색 후의 node_from의 상태")
print(node_from)