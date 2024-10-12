tree = {}	# 딕셔너리 생성(각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드를 저장)

def preorder(n) :		# 전위 순회
    if n is not None :  
        print(n, end='') 
        preorder(tree[n][0]) 
        preorder(tree[n][1])  

def inorder(n) :			# 중위 순회
    if n is not None :  
        inorder(tree[n][0])  
        print(n, end='')  
        inorder(tree[n][1])  

def postorder(n) :		# 후위 순회
    if n is not None :  
        postorder(tree[n][0]) 
        postorder(tree[n][1]) 
        print(n, end='')  

# 입력 받기
N = int(input())  # N: 이진 트리의 노드 개수
for _ in range(N):
    n, left, right = input().split()  # 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드를 입력받음
    
    left = None if left == '.' else left	# 자식 노드가 없는 경우에는 .으로 표현
    right = None if right == '.' else right
    tree[n] = (left, right)  # 딕셔너리에 노드와 자식 정보를 저장

# 각 순회의 결과를 출력
preorder('A')  
print()  # 줄 바꿈
inorder('A')
print()  # 줄 바꿈
postorder('A')
