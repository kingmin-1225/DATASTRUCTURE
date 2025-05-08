# DATASTRUCTURE
2025년 한양대학교 ERICA 인공지능학과 자료구조 수업 코드 정리

#### 기본 클래스 선언 규칙



## Stack
LIFO(Last In First Out)의 구조로 마지막에 들어온 요소가 먼저 나옴
#### Methods
- `push(e)` : 데이터 삽입
- `pop()` : 데이터 제거
- `top()` : 가장 마지막에 삽입된 데이터 반환

## Queue
FIFO(First In First Out)의 구조로 처음에 들어온 요소가 먼저 나옴
#### Methods
- `enqueue(e)` : 데이터 삽입
- `dequeue()` : 데이터 제거
- `first()` : 처음에 삽입된 데이터 반환

## Doubly linked base
위의 일반 리스트와 달리 노드가 _prev, _next를 인스턴스로 갖음    
_header와 _trailer라는 element를 갖지 않는 가상 노드를 인스턴스로 갖음    
두 가상 노드를 서로 연결되어 있음
#### Methods
- `_insert_between(element, predecessor, successor)` : 연결되어 있는 두 노드(predecessor와 successor) 사이에 element를 갖는 노드를 삽입 후 삽입된 노드 반환
- `_delete_node(node)` : 입력된 노드를 제거

## Deque(Doubly linked base)
양쪽 끝에서 데이터를 삽입하고 제거할 수 있음
#### Methods
- `first()` : 덱의 첫 데이터 반환
- `last()` : 덱의 마지막 데이터 반환
- `insert_first(element)` : 덱의 첫 부분에 데이터 삽입
- `insert_last(element)` : 덱의 마지막 부분에 데이터 삽입
- `delete_first()` : 덱의 첫 데이터 삭제
- `delete_last()` : 덱의 마지막 데이터 삭제

## Positional List(Doubly linked base)
덱과 비슷하지만 노드의 위치를 저장하는 내부 클래스 Position을 활용하여 덱과 달리 노드의 위치를 기반으로 데이터의 삽입, 출력을 할 수 있는 자료구조

#### Methods
내부 메소드
- `_validate(position)` : 입력된 포지션이 우효한 포지션인지 확인 후 해당 포지션의 노드 반환
- `_make_position(node)` : 노드를 입력받아 해당 노드를 가리키는 포지션 반환
- `_insert_between(element, predecessor, successor)` : 두 개의 노드를 입력받아 element 원소 삽입 후 해당 노드의 위치 반환
외부 메소드
- `first()` : 리스트의 첫 번째 요소의 위치(Position) 반환
- `last()` : 리스트의 마지막 요소의 위치 반환
- `before(position)` : 입력된 위치의 다음 노드의 위치 반환
- `after(position)` : 입력된 위치의 이전 노드의 위치 반환
- `add_first(element)` : 리스트의 앞에 원소 삽입
- `add_last(element)` : 리스트의 마지막에 원소 삽입
- `add_before(position, element)` : 입력된 포지션 앞에 원소 삽입
- `add_after(position, element)` : 입력된 포지션 뒤에 원소 삽입
- `delete(position)` : 입력된 위치에 존재하는 노드 삭제
- `replace(position, element)` : 입력된 위치에 존재하는 노드의 값 수정



## Priority queue base
들어간 순서에 상관없이 우선순위가 높은 데이터를 먼저 반환
내부 클래스 `_Item` 을 사용해서 key와 value 쌍으로 데이터 구성
key를 기준으로 데이터의 우선순위 판단    

#### _Item's Method
- `__lt__(other)` : 우선순위 판정을 위한 매직 매소드(less than <)

## Unsorted priority queue(Priority queue base)
별도의 처리 업이 데이터를 입력받고 데이터를 제거할 때는 큐 전체를 탐색해 우선순위가 가장 높은 노드를 제거함    
- 빠른 삽입, 느린 삭제

#### Methods
- `_find_min()` : 우선순위가 높은 요소를 탐색(큐 전체를 탐색하기에 O(n)의 시간이 걸림)
- `add(key, value)` : 큐 마지막에 key와 value를 갖는 `_Item` 삽입
- `min()` : 우선순위가 높은 `_Item의` key와 value 반환
- `remove_min()` : 우선순위가 높은 `_Item` 탐색 후 제거 및 key, vlaue 반환

## Sorted priority queue(Priority queue base)
원소 삽입 시 정렬 상태를 유지함    
- 느린 삽입, 빠른 삭제

#### Methods
- `min()` : 우선순위가 높은 요소 반환(리스트가 정렬되어 있기 때문에 첫번째 요소 반환)
- `remove_min()` : 우선순위가 가장 높은 요소 제거 및 key, value 반환
- `add(key, value)` : key와 value를 갖는 `_Item` 삽입(정렬 상태를 유지해야 함)

## Heap priority queue(Priority queue base)
이진 트리인 힙(부모노드의 값이 자식노드의 값보다 항상 큼)을 이용하여 구현한 우선순위 큐    
위의 sorted priority queue와 unsorted priority queue보다 더 효율적임    
배열 기반으로 구현(j인덱스의 자식 노드 = j*2+1, j*2+2)    
- 빠른 삽입, 빠른 삭제
#### Methods
- `_parent(j)` : 부모 노드 인덱스 반환
- `_left(j)` : 왼쪽 자식 노드 인덱스 반환
- `_right(j)` : 오른쪽 자식 노드 인덱스 반환
- `_has_left(j)` : 왼쪽 자식 노드의 존재 유무 반환
- `_has_right(j)` : 오른쪽 자식 노드의 존재 유무 반환
- `_swap(i, j)` : 두 노드 교체
- `_upheap(j)` : j 위치의 노드가 부모 노드의 값보다 클 때까지 부모 노드와 `_swap`
- `_downheap(j)` : j 위치의 노드가 자식 노드의 값보다 작을 때까지 자식 노드와 `_swap`
- `add(key, value)` : `_Item(key, value)`를 큐에 삽입 이때 힙의 구조는 유지됨
- `min()` : 루트노드(배열의 첫 번째 요소) 반환
- `remove_min()` : 루트노드와 배열의 마지막 요소를 스왑한 후 마지막 요소 제거 및 반환, 바꾼 배열의 마지막 요소 `_downheap`

## Tree
루트 노드로부터 가지처럼 뻗어나가는 구조를 띄는 자료구조    
#### 용어정리
- 루트노드 : 최상위 노드
- 부모노드 : 상위 노드
- 자식노드 : 하위 노드
- 깊이 : 자신을 제외한 조상 노드의 수
- 높이 : 해당 노드의 자식의 높이 중 가장 큰 값 + 1

## Adaptable PQ(Heap priority queue)



## Binary tree(Tree, Positional list)
자식 노드가 최대 2개인 트리    
하나의 노드에 저장되는 element와 parent, left, right 3개의 노드의 위치정보가 저장됨
#### Methods
- `sibling(position)` : 해당 위치의 형제 노드 반환
- `children(position)` : 자식 노드 출력
- `_add_root(element)` : 루트노드 추가
- `_add_left(element)` : 왼쪽 자식 노드 추가한 후 자식 노드의 위치 반환
- `_add_right(element)` : 오른쪽 자식 노드 추가한 후 자식 노드의 위치 반환
- `_replace(position, element)` : 해당 위치에 존재하는 노드의 요소 교체
- `_delete(position)` : 해당 위치에 존재하는 노드 제거

## Map
key와 value 한 쌍으로 이루어진 자료형    
고유한 값을 가지는 key와 중복 가능한 value로 이루어짐




## Heap
완전 이진 트리 형태의 자료구조



---
## Binary Search Tree
이진 탐색 트리
- left_child < parent < right_child








left child height - right child height <= 1 

splay Tree - 가장 최근 접근한 노드를 루트노드로 변경
최근에 접근한 데이터 검색 O(1)








