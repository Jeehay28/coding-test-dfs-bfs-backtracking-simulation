# 1주차 DFS

### 개념문제
1.	DFS를 구현하는 대표적인 두 가지 방법은 재귀호출을 이용하는 것과 명시적인 스택(Stack) 자료구조를 사용하는 것입니다. 각 구현 방식의 장단점을 비교 설명해주세요.
2.	방향 그래프(Directed Graph)에서 사이클(Cycle) 존재 여부를 판별하기 위한 DFS를 어떻게 활용할 수 있는지 구체적인 알고리즘을 설명해주세요.
3.	재귀를 활용한 DFS에서 가장 최근의 노드로 돌아가는 백트랙킹 동작이 어떤 방식으로 동작 하는지 하나의 예를 들어 설명해주세요.

<br>

### 개념 정리
- [DFS](week01-dfs-concept.md)

### 풀어볼 문제
- 깊이 우선 탐색 순회(몸풀기 문제)
- [네트워크(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/43162)
    - [풀이](dfs-43162-network.py)
- [양과 늑대(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/92343)
    - [풀이](dfs_92343_wolf_and_sheep.py)
- [전력망을 둘로 나누기(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/86971) 
- [양궁대회(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/92342) 

<br><br>


# 2주차 BFS
### 개념문제
1.	BFS(너비 우선 탐색) 알고리즘 작동 원리를 설명하고, 어떤 자료구조를 사용하는지, 그리고 그 이유는 무엇인지 설명해주세요.
2.	BFS와 DFS(깊이 우선 탐색)의 차이점은 무엇이며, 각각 어떤 종류의 문제에 더 적합한지 예시를 들어 설명해주세요.
3.	BFS 알고리즘의 시간 복잡도는 O(V + E)인데, 그래프의 형태(예: 밀집 그래프 vs 희소 그래프)가 실제 수행 시간에 어떤 영향을 미칠 수 있을지 설명해주세요.

<br>

### 개념 정리
- [BFS](week02-bfs-concept.md)

### 풀어볼 문제
- 너비 우선 탐색 순회(몰풀기 문제 39번)
- [게임 맵 최단거리(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/1844)
    <!-- - [풀이](dfs-43162-network.py) -->
- [경주로 건설(프로그래머스)](https://school.programmers.co.kr/learn/courses/30/lessons/67259)
    <!-- - [풀이](dfs_92343_wolf_and_sheep.py) -->