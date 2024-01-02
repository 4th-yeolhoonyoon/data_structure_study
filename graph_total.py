class Graph:
    def __init__(self):
        self.graph = {}
        self.cost = {}  # 탐색 비용을 저장
        self.node_from = {}  # 탐색 경로를 저장

    ...

    # dfs는 기존에 만든 코드와 완전히 같다.
    # 2023.7.15 마킹한 코드는 bfs와 dijkstra 메서드처럼 탐색 비용과 탐색 경로를 저장하기 위해 추가한 것이다.
    def dfs(self, node):
        res = []
        visited = set()

        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        def _dfs(u):
            visited.add(u)
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    self.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    _dfs(v)

        _dfs(node)
        return res

    def bfs(self, node):
        # 리스트보다 성능이 우수한 deque를 사용한다.
        from collections import deque

        res = []
        queue = deque([node])
        visited = set(queue)

        # 비용과 노드 정보를 저장하는 사전을 초기화한다.
        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        while queue:
            u = queue.popleft()
            res.append(u)
            # 현재 노드(u)와 간선으로 연결된 노드(v)를 가져온다.
            # 사전을 그냥 순회할 때는 키(key)만 가져온다.
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    # 노드 v로 가는 비용과 경로 정보를 저장한다.
                    # self.graph[u][v]는 노드 u와 v를 연결하는 간선의 가중치다.
                    elf.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    queue.append(v)

        return res

    def dijkstra(self, start):
        import math, heapq

        # 비용과 노드 정보를 저장하는 사전을 초기화한다.
        self.cost = {node: math.inf for node in self.graph}
        self.node_from = {node: None for node in self.graph}
        self.cost[start] = 0

        res = []
        visited = set()

        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            prev_time, u = heapq.heappop(heap)
            if u in visited:
                continue
            res.append(u)
            visited.add(u)
            # 현재 노드(u)와 간선으로 연결된 노드(v)를 가져온다.
            for v in self.graph[u]:
                # 가중치 정보를 가져와서 인접노드로 가는 비용을 계산하고 갱신한다.
                if (new_time := prev_time + self.graph[u][v]) < self.cost[v]:
                    self.cost[v] = new_time
                    self.node_from[v] = u
                    heapq.heappush(heap, (self.cost[v], v))
        return res

    def get_path(self, end):
        path = ""
        node = end
        while self.node_from[node]:
            path = " → " + str(node) + path
            node = self.node_from[node]

        # 기존 코드에서 수정한 부분
        # 한 노드에서 다른 노드로 가는 경로가 없을 때도 처리
        if path:
            path = str(node) + path
            return f"{path} (cost = {str(self.cost[end])})"
        else:
            return f"There is no path."
