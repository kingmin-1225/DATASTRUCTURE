# (2, 4) Tree

## 개요
1. Multi-Way Search Tree
2. (2, 4) Tree's Properties
3. Algorithms

## Multi-Way Search Tree
2개 이상의 자식을 갖는 노드로서 d-1개의 키를 갖고 d개의 자식을 갖는 노드(d-node)들로 이루어진 트리
- 잎은 자료를 저장하지 않고 빈칸으로 존재함

### Searching
binary search tree와 비슷함
- 첫 번째 키보다 작다면 첫번째 자식노드로 이동
- k번째 키와 k+1번째 키 사이에 있다면 k번째 자식노드로 이동
- 마지막 키보다 크다면 마지막 자식노드로 이동
- 최종 도착한 노드에 키가 없다면 트리에 해당 값 없음

## Properties
- Node-Size Property : 모든 내부노드들은 최대 4개의 자식노드(4-node)를 가짐
- Deapth Property : 모든 잎 노드들은 같은 깊이를 가짐

## Algorithms

### Insertion
- 키의 대소를 비교하여 삽입 가능한 곳에 삽입
- overflow(#키 > 3) 발생 시 split(3번 키를 부모노드에 삽입하고 3번 키를 기준으로 두 개의 노드로 분리)
- 부모노드가 없을 경우(루트 노드) 새로운 루트노드 생성

### Deletion
- 해당 노드보다 작은 값(왼쪽 자식 노드의 서브트리의 가장 큰 값)과 교체 후 제거
- 제거 과정에서 underflow(1-node w 발생) 문제 발생 시 w의 형제노드의 자식 수에 따라 처리가 달라짐
  - 2-node : 형제 노드와 w를 병합(형제노드와 w 사이에 있는 부모노드의 키를 병합노드의 키로 가져옴)
  - 3-node or 4-node : 형제노드와 w 사이에 있는 부모노드의 키를 w의 키로 가져오고 빈 부모노드의 키는 형제노드의 키 중 w와 가까운 키로 대체함
