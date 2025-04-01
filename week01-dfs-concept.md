📅 Week 01 (Mar 31 - Apr 5, 2025)

# 1주차 DFS(Depth-First Search)

<br><br>


## 1️⃣ DFS를 구현하는 대표적인 두 가지 방법은 재귀호출을 이용하는 것과 명시적인 스택(Stack) 자료구조를 사용하는 것입니다. 각 구현 방식의 장단점을 비교 설명해주세요.

### 1. 재귀 호출 방식 (Recursive Approach)
재귀 호출 방식은 DFS를 구현할 때 가장 직관적이고 자연스러운 방법입니다. 각 노드를 방문할 때마다 해당 노드의 자식 노드로 재귀적으로 탐색을 진행하는 방식입니다. 이 방식은 함수 호출 스택을 사용하여 탐색을 구현하며, 스택 구조를 자동으로 처리합니다.

동작 원리:
- 각 노드(혹은 탐색할 노드)에서 시작합니다.
- 현재 노드를 방문했다고 표시합니다.
- 그 노드의 인접한 노드들을 재귀적으로 방문합니다.
- 자식 노드가 더 이상 없으면, 이전 노드로 돌아가서 탐색을 계속합니다.
- 재귀 호출은 탐색을 깊게 진행하며, 자식 노드가 없으면 다시 이전 단계로 돌아가며 탐색을 진행합니다.

예시 (재귀 호출 방식 DFS):

```python
def dfs_recursive(node, visited):
    # 현재 노드를 방문했다고 표시
    visited.add(node)
    print(node)  # 현재 노드를 처리
    
    # 현재 노드의 인접 노드를 재귀적으로 방문
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)
```

장점:
- 간단하고 직관적인 코드: 재귀를 사용하면 DFS 로직을 매우 간결하게 작성할 수 있습니다.
- 함수 호출 스택을 활용: 함수 호출 스택이 스택 역할을 하므로 명시적인 스택을 사용하지 않아도 됩니다.
- 백트래킹: 재귀의 특성상, 자식 노드를 탐색한 후 자동으로 이전 노드로 돌아가서 탐색을 이어갑니다.

단점:
- 스택 오버플로우: 그래프가 깊고 크기가 매우 큰 경우, 시스템의 재귀 호출 스택이 한계를 초과하여 스택 오버플로우가 발생할 수 있습니다.
- 재귀 깊이 제한: 시스템마다 재귀 깊이에 제한이 있어, 매우 깊은 트리나 그래프에서는 에러가 발생할 수 있습니다.


<br><br>

### 2. 명시적 스택 사용 (Explicit Stack Approach)
명시적 스택 사용 방식에서는 스택 자료구조를 직접 관리하며 DFS를 구현합니다. 재귀 호출을 대신하여, 노드를 스택에 넣고 꺼내면서 탐색을 진행합니다. 이 방법은 스택의 크기를 명확히 제어할 수 있어, 깊이가 깊어도 안정적으로 동작합니다.

동작 원리:
- 시작 노드를 스택에 넣습니다.
- 스택이 비지 않을 때까지 반복합니다:
- 스택에서 노드를 꺼냅니다.
- 그 노드가 아직 방문되지 않았다면, 방문했다고 표시하고 그 노드의 인접 노드를 스택에 넣습니다.
- 모든 인접 노드를 처리한 후, 스택에서 다시 노드를 꺼내며 계속 탐색을 진행합니다.

예시 (명시적 스택 방식 DFS):

```python
def dfs_stack(start_node):
    stack = [start_node]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)  # 현재 노드를 처리
            
            # 인접 노드를 스택에 추가
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
```

장점:
- 스택 오버플로우 방지: 재귀 호출을 사용하지 않으므로, 시스템의 호출 스택 한계에 영향을 받지 않습니다.
- 반복문으로 처리: 재귀를 사용하지 않고 명시적으로 스택을 관리하므로, 스택 크기를 직접 제어할 수 있습니다.
- 더 많은 제어: 스택을 명시적으로 관리하므로, 탐색 과정에서 더 많은 제어가 가능합니다.

단점:
- 구현 복잡도: 재귀 방식에 비해 코드가 길어지고 관리해야 할 스택이 추가되므로 코드가 다소 복잡해질 수 있습니다.
- 수동으로 스택 관리: 스택을 직접 관리해야 하기 때문에, 스택의 상태를 추적하고 방문 노드를 관리하는 추가적인 로직이 필요합니다.

<br><br>

### 3. 비교: 재귀 호출 방식 vs. 명시적 스택 사용 방식

| 항목               | 재귀 호출 방식                              | 명시적 스택 사용 방식                        |
|--------------------|-------------------------------------------|--------------------------------------------|
| **구현 난이도**       | 간단하고 직관적                             | 비교적 복잡하고 코드가 길어짐                  |
| **스택 관리**        | 자동으로 처리 (호출 스택 사용)               | 명시적으로 스택을 관리해야 함                 |
| **스택 오버플로우**    | 깊이가 깊어지면 스택 오버플로우 발생 가능   | 스택 오버플로우 문제 없음                     |
| **메모리 효율성**     | 함수 호출에 의존하므로 메모리 소모가 클 수 있음 | 명시적 스택 사용으로 메모리 사용이 더 직관적이고 일정함 |
| **성능**             | 작은 그래프에서는 빠르지만, 깊이가 깊으면 성능 저하 가능 | 깊이가 깊어도 성능 저하가 적음                  |
| **적합한 경우**       | 간단하고 작은 그래프를 탐색할 때 좋음        | 큰 그래프나 깊이가 깊은 트리에서 좋음           |


<br><br>

### 4. 결론
- 재귀 호출 방식은 코드가 간결하고 이해하기 쉽지만, 깊이가 매우 깊거나 큰 그래프에서는 스택 오버플로우 문제가 발생할 수 있습니다.

- 명시적 스택 사용 방식은 스택 오버플로우 문제를 방지하고, 깊이가 깊은 그래프나 복잡한 탐색이 필요한 경우에 더 적합합니다. 하지만, 코드가 다소 복잡해질 수 있다는 점을 감안해야 합니다.

- 두 방식 모두 시간 복잡도는 **O(V + E)**로 동일하지만, 문제의 특성과 필요에 따라 적합한 방법을 선택해야 합니다.


<br><br>



## 2️⃣ 방향 그래프(Directed Graph)에서 사이클(Cycle) 존재 여부를 판별하기 위한 DFS를 어떻게 활용할 수 있는지 구체적인 알고리즘을 설명해주세요.

### 1. 핵심 개념
DFS를 활용한 사이클 판별 알고리즘은 각 노드의 방문 상태를 추적하여, 탐색 중 다시 방문하는 노드가 있는지를 확인하는 방식으로 동작합니다. 이를 위해 노드의 방문 상태를 다음 세 가지로 구분합니다:

- 방문하지 않음 (WHITE = 0) → 아직 방문하지 않은 노드
- 방문 중 (GRAY = 1) → 현재 DFS 탐색 경로에 있는 노드
- 방문 완료 (BLACK = 2) → DFS 탐색이 끝난 노드

DFS 탐색 중 방문 중(GRAY)인 노드를 다시 만나면, 해당 그래프에는 사이클이 존재합니다.


### 2. 알고리즘 동작 과정
- 모든 노드를 방문하지 않음 (WHITE) 상태로 초기화합니다.
- 그래프의 모든 노드에 대해 DFS를 수행하며, 방문 상태를 추적합니다.
- DFS 수행 중:
    - 현재 탐색 중인 노드를 방문 중(GRAY) 상태로 변경합니다.
    - 방문할 인접 노드가 방문 중(GRAY) 상태이면, 사이클이 존재합니다.
    - 탐색이 끝난 경우, 해당 노드를 방문 완료(BLACK) 상태로 변경합니다.
- 모든 노드에 대해 탐색이 완료되면, 사이클 여부를 출력합니다.


### 3. DFS를 이용한 방향 그래프 사이클 판별 코드
```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices  # 정점 개수
    
    def add_edge(self, u, v):
        """ 방향 그래프에서 u -> v 간선 추가 """
        self.graph[u].append(v)
    
    def is_cyclic_util(self, node, visited, recursion_stack):
        """
        DFS를 수행하며 사이클을 판별하는 보조 함수
        :param node: 현재 탐색 중인 노드
        :param visited: 방문 상태 배열 (0: 방문 안함, 1: 방문 중, 2: 방문 완료)
        :param recursion_stack: 현재 DFS 경로를 저장하는 집합
        :return: 사이클이 존재하면 True, 없으면 False
        """
        # 현재 노드를 방문 중(GRAY)으로 표시
        visited[node] = 1
        recursion_stack.add(node)

        # 현재 노드의 모든 인접 노드 탐색
        for neighbor in self.graph[node]:
            if visited[neighbor] == 0:  # 방문하지 않은 노드라면 DFS 수행
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:  # 방문 중(GRAY)인 노드를 다시 만나면 사이클 존재
                return True
        
        # DFS 탐색 완료 후, 현재 노드를 방문 완료(BLACK)으로 변경
        visited[node] = 2
        recursion_stack.remove(node)
        return False

    def is_cyclic(self):
        """
        방향 그래프의 사이클 여부 판별 함수
        :return: 사이클이 존재하면 True, 없으면 False
        """
        visited = [0] * self.V  # 모든 노드를 방문하지 않음(WHITE) 상태로 초기화
        recursion_stack = set()

        for node in range(self.V):
            if visited[node] == 0:  # 방문하지 않은 노드에서 DFS 시작
                if self.is_cyclic_util(node, visited, recursion_stack):
                    return True  # 사이클이 존재하면 True 반환
        return False

# 예제 실행
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # 0 -> 1 -> 2 -> 0 사이클 존재
g.add_edge(2, 3)

if g.is_cyclic():
    print("그래프에 사이클이 존재합니다.")
else:
    print("그래프에 사이클이 존재하지 않습니다.")

```

### 4. 알고리즘 설명
- 그래프를 인접 리스트로 표현 → defaultdict(list) 사용
- DFS 수행 (is_cyclic_util)
    - 방문하지 않은 노드(WHITE)에서 시작
    - 방문 중(GRAY) 상태인 노드를 다시 만나면 사이클이 존재
    - 탐색이 완료되면 방문 완료(BLACK) 상태로 변경
- 모든 노드에 대해 DFS 실행 (is_cyclic)
    - 모든 노드를 확인하며, DFS 탐색이 필요한 경우 is_cyclic_util 호출
    - 탐색 중 사이클이 발견되면 True 반환


### 5. 시간 복잡도 분석
- DFS 탐색이 모든 노드와 간선을 한 번씩 방문하므로, 시간 복잡도는 O(V + E) 입니다.
    - V = 노드 개수
    - E = 간선 개수


### 6. 예제 실행 결과
위 코드에서 g.add_edge(2, 0)이 존재하여 0 → 1 → 2 → 0 사이클이 발생합니다.
- 출력 결과:
    ```
    그래프에 사이클이 존재합니다.
    ```

- 만약 사이클이 없는 경우:
    ``` python
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    그래프에 사이클이 존재하지 않습니다.
    ```

### 7. 결론
- 방향 그래프의 사이클 판별은 DFS와 방문 상태(GRAY 체크)를 활용하면 효율적으로 해결할 수 있습니다.
- 재귀 호출을 사용하여 탐색 경로를 추적하고, 방문 중인 노드(GRAY)를 다시 만나면 사이클이 존재함을 판별할 수 있습니다.
- **시간 복잡도는 O(V + E)**로, 그래프 탐색과 동일한 수준의 성능을 가집니다.

이 알고리즘은 위상 정렬(Topological Sort), 데드락 검사, 그래프 기반 문제 해결 등 다양한 곳에서 활용될 수 있습니다. 🚀 


<br><br>

## 3️⃣ 재귀를 활용한 DFS에서 가장 최근의 노드로 돌아가는 백트랙킹 동작이 어떤 방식으로 동작 하는지 하나의 예를 들어 설명해주세요.

백트래킹은 DFS 탐색 중 더 이상 진행할 수 없는 경우(또는 특정 조건을 충족하지 않는 경우), 가장 최근 방문한 노드로 되돌아가는 과정입니다.

### 1. 그래프 표현 (Python 딕셔너리)
- 각 키(Key)는 노드 번호이며, 값(Value)은 해당 노드에서 갈 수 있는 이웃 노드들의 리스트입니다.

    ```python
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    ```


### 2. DFS 탐색 및 백트래킹 과정
DFS 탐색 과정에서 스택(Stack) 구조를 활용하여 백트래킹이 자동으로 이루어집니다.
여기서 재귀 호출이 끝나면서(함수가 종료되면서) 자연스럽게 이전 노드로 돌아가는 것이 백트래킹입니다.

```python
def dfs(node, graph, visited):
    print(f"Visiting {node}")  # 방문한 노드 출력
    visited.add(node)          # 방문한 노드 기록

    for neighbor in graph[node]:  
        if neighbor not in visited:  # 아직 방문하지 않은 경우
            dfs(neighbor, graph, visited)

    print(f"Backtracking from {node}")  # 백트래킹 발생 (재귀 호출 종료)

# 방문한 노드를 저장할 집합(Set)
visited = set()

# DFS 시작
dfs(1, graph, visited)
```

### 3. 실행 과정 및 백트래킹 발생 순간
DFS는 가장 깊은 노드까지 탐색한 후 더 이상 갈 곳이 없을 때 백트래킹합니다.
DFS 호출 순서와 백트래킹 과정은 다음과 같습니다.

1️⃣ dfs(1) → dfs(2) → dfs(4) → 백트래킹 (4번 노드에서 더 이상 진행 불가 → 2번으로 이동)
2️⃣ dfs(2) → dfs(5) → 백트래킹 (5번 노드에서 더 이상 진행 불가 → 2번으로 이동 → 1번으로 이동)
3️⃣ dfs(1) → dfs(3) → 백트래킹 (3번 노드에서 더 이상 진행 불가 → 1번으로 이동 → 종료)


### 4. 실행 결과 (백트래킹 동작 확인)
```
Visiting 1
Visiting 2
Visiting 4
Backtracking from 4
Visiting 5
Backtracking from 5
Backtracking from 2
Visiting 3
Backtracking from 3
Backtracking from 1
```

### 5. 핵심 요약
- DFS는 재귀 호출을 통해 가장 깊은 곳까지 탐색
- 더 이상 탐색할 노드가 없으면 재귀 호출이 종료되면서 백트래킹 발생
- 백트래킹은 "현재 노드의 모든 자식 탐색 완료 → 이전 노드로 돌아감" 과정
- 최종적으로 모든 노드가 백트래킹되면 DFS 탐색 종료 🚀