import math
import heapq

graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}


def dijkstra(graph, node):
    lead_time = {node: math.inf for node in graph}
    node_from = {node: None for node in graph}
    print(lead_time)
    print(node_from)

    lead_time[node] = 0

    heap = []
    heapq.heappush(heap, (0, node))
    print(heap)

    while heap:
        print('heap :', heap)
        prev_time, u = heapq.heappop(heap)
        print(prev_time, u)

        # 현재 노드에 인접한 노드와 가중치(소요 시간)를 가져와서 반복한다.
        for v, weight in graph[u]:
            # 인접한 노드로 가는 소요 시간을 계산하여 기본 값보다 작으면,
            # 시간 정보를 갱신하고, 이전 노드를 기록한다. 그리고 힙에 넣는다.
            if (new_time := prev_time + weight) < lead_time[v]:
                lead_time[v] = new_time
                node_from[v] = u
                heapq.heappush(heap, (lead_time[v], v))
                print('after heap :', heap)

    # 소요 시간과 이전 노드를 기록한 사전을 반환한다.
    return lead_time, node_from


def shortest_path(node_from, lead_time, start, end):
    path = ""
    node = end
    while node_from[node]:
        path = " → " + str(node) + path
        node = node_from[node]
    return f"{str(node) + path} (cost = {str(lead_time[end])})"


lead_time, node_from = dijkstra(graph, "A")

print("A에서 다익스트라 탐색 후의 node_from과 lead_time의 상태")
print(node_from)
print(lead_time)

print()
print("A에서 F로 가는 최단 경로:", end = " ")
print(shortest_path(node_from, lead_time, "A", "F"))