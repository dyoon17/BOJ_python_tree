#2250. 트리의 높이와 너비

N = int(input())  # N: 노드의 개수
tree = {}  # 딕셔너리 생성
parent = [False] * (N + 1)  # 루트 노드를 찾기 위한 리스트 생성(부모가 있는지 확인)

for _ in range(N):
    node, left, right = map(int, input().split())  # 각 노드의 번호, 왼쪽 자식, 오른쪽 자식을 입력
    tree[node] = (left, right)  # 각 노드의 자식 노드 정보를 트리에 저장
    if left != -1:      # 왼쪽에 자식 노드가 있을 경우
        parent[left] = True      # 부모가 있다고 표시
    if right != -1:     # 오른쪽 자식 노드가 있을 경우
        parent[right] = True     # 부모가 있다고 표시

root = parent.index(False, 1)  # 1번 노드부터 시작.. parent 리스트에서 부모가 없는 노드를 루트로 설정

col = 1  # 중위 순회 -> 노드가 위치한 열 번호를 기록
left_most = [0] * (N + 1)  # 각 레벨에서 가장 왼쪽에 있는 노드의 열 번호
right_most = [0] * (N + 1)  # 각 레벨에서 가장 오른쪽에 있는 노드의 열 번호

def inorder(node, level):
    global col  # col(열 번호) 변수는 전역 변수로 설정
    if node == -1:  # 현재 노드가 없으면 함수 종료 (-1: 자식 노드가 없다는 의미)
        return
    inorder(tree[node][0], level + 1)  # 왼쪽 자식 먼저 중위 순회로..(왼쪽 자식 → 부모 → 오른쪽 자식)
    
    if left_most[level] == 0:  # 아직 해당 레벨의 노드를 방문한 적이 없는 경우
        left_most[level] = col  # 현재 열 번호를 그 레벨의 가장 왼쪽 위치로 저장
    right_most[level] = col  # 마지막에 방문한 노드는 가장 오른쪽 위치로 저장
    col += 1  # 열 번호 갱신
    
    inorder(tree[node][1], level + 1)  # 오른쪽 자식도 중위 순회..

inorder(root, 1)    # 중위 순회 시작; 루트 노드부터 시작 ~ 각 노드가 위치한 열 번호를 계산

best_level = 0    # 너비가 가장 넓은 레벨 번호 
max_width = 0     # 가장 넓은 레벨의 너비

for i in range(1, N + 1):  # 각 레벨을 순차적으로 확인 (레벨 1~N까지)
    if left_most[i] is not None :
        width = right_most[i] - left_most[i] + 1  # 해당 레벨의 오른쪽 열 번호 - 왼쪽 열 번호 + 1
        if width > max_width:  # 현재까지의 최대 너비보다 클 경우
            max_width = width  # 최대 너비 갱신
            best_level = i  # 그리고 너비가 가장 넓은 레벨 번호를 저장

print(best_level, max_width)
