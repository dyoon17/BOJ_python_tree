#1967. 트리의 지름

from collections import deque

n = int(input())  # n: 노드의 개수
tree = [[] for _ in range(n + 1)]  # n+1 크기의 빈 리스트 생성

for _ in range(n - 1):
    p, c, w = map(int, input().split())  # 입력 <- p는 부모, c는 자식, w는 가중치
    tree[p].append((c, w))  # 부모에 자식을 연결 / 가중치는 그 사이 연결된 거리를 뜻함
    tree[c].append((p, w))  # 자식에 부모를 연결

def bfs(start):    # 너비 우선 탐색 함수 정의
    # 큐를 사용해 BFS 탐색을 진행
    queue = deque([(start, 0)])  # 큐에 (노드, 거리)를 저장
    visited = [False] * (n + 1)  # 방문한 기록을 저장할(아직 방문 X) 리스트 생성
    visited[start] = True  # 시작 노드를 방문 처리
    f_node, max_dist = start, 0  # 가장 멀리 있는 노드와 최대 거리를 저장하는 변수

    while queue:
        node, dist = queue.popleft()  # 큐에서 (노드, 거리) 꺼내서 탐색
        if dist > max_dist:    # 현재 노드까지의 거리가 지금까지 저장된 최대 거리보다 클 경우
            max_dist = dist  # 최대 거리를 갱신함
            f_node = node  # 가장 멀리 있는 노드를 갱신함
        
        # 현재 노드와 연결된 노드들 탐색
        for neighbor, weight in tree[node]:
            if not visited[neighbor]:  # 방문하지 않은 노드만 탐색
                visited[neighbor] = True  # 방문 처리
                queue.append((neighbor, dist + weight))  # 큐에 추가(노드까지의 거리를 업데이트)

    return f_node, max_dist  # 가장 멀리 떨어진 노드와 그 노드까지의 최대 거리

f_node, _ = bfs(1)  # 첫 번째 BFS 수행 -> 1번 노드에서 출발하여 가장 멀리 떨어진 노드를 찾음

_, max_dist = bfs(f_node)  # 두 번째 BFS 수행 -> 첫 번째 BFS에서 찾은 가장 멀리 있는 노드를 출발점으로 하여 다시 가장 멀리 떨어진 노드를 찾음

print(max_dist)    # 지름 출력
