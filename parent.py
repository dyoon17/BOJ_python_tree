#11725. 트리의 부모 찾기

N = int(input())    # N: 노드의 개수

tree = [[] for _ in range(N + 1)]    # 트리를 저장할 리스트 생성

for _ in range(N - 1):    # N-1개의 간선 정보 입력
    a, b = map(int, input().split())    # a, b 노드가 연결됨
    tree[a].append(b)    # a 노드에 b 연결
    tree[b].append(a)    # b 노드에 a 연결

parent = [0] * (N + 1)    # 부모 정보를 저장할 리스트 생성
# 부모를 아직 모르는 노드는 0으로 표시함

# 루트인 1번 노드부터 순서대로 시작해서 부모를 찾음
parent[1] = 1  # 루트 노드는 부모 없음 -> 자기 자신을 부모로 설정
queue = [1]  # 방문할 노드 리스트에 루트 노드 추가

while queue:    # 더 이상 방문할 노드가 없을 때까지 반복
    current = queue.pop()  # 탐색할 노드를 queue에서 꺼냄
    
    for next_node in tree[current]:
        if parent[next_node] == 0:  # 아직 부모가 없는 노드만 처리
            parent[next_node] = current  # 현재 노드를 부모로 설정
            queue.append(next_node)  # 이웃 노드를 다음에 탐색할 노드에 추가

for i in range(2, N + 1):    # 2번 노드부터 각 노드의 부모를 출력(N번 노드까지..)
    print(parent[i])
