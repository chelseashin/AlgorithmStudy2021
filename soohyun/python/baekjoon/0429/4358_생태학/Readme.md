# 문제의 핵심
- 문자열 처리
- 해시
# 알고리즘
- EOF까지 입력받는다.
    - 입력받은 문자열을 dict에 저장, 정렬을위하여 heappush사용
- 입력이 종료되면 heappop을 통해 정렬상태를 가져옴
# 사용 자료구조
- 원목개수를 저장하기위한 tree
- 원목이름을 저장하기위한 list (heaqq 용)
- 전체갯수를 저장하기위한 all_num
# 주요 Code Snippet
- EOF 까지 입력받기
```python
 while True:
        result = input().rstrip()
        if not result:
            break
```
- 4까지 반올림하여 출력
```python
while len(tree_name) > 0:
    cur_tree = heapq.heappop(tree_name)
    print('%s %.4f' %(cur_tree, tree[cur_tree]/all_num*100))
```
# 추정 시간복잡도
- 시간복잡도: O(nlogn)
    - 입력받기: 
        - n개 입력받음: O(n)
        - heapush * n개: O(nlogn)
    - 출력하기:
        - n개 출력: O(n)
        - heappop * n개: O(nlogn)
- 공간복잡도: O(2n)
    - tree: 최악의 경우 하나도 겹치지 않는경우: O(n)
    - tree_name: 하나도 겹치지 않는경우 O(n)
# 빠르게 푼사람 코드
- defaultdict + sorted
    - key가 없을경우미리 지정해놓은 초기값을 반환하는 dict
- Counter + sorted
    - 동일한 값의 자료가 몇개인지 파악하는 객체
- 입력받기
    ```python 
    ecology = Counter(sys.stdin.read().split('\n')[:-1]) 
    ```
# 복기
- 나는 heapq가 더 빠를줄 알고 풀었는데, 실상은 그게 아니였다.
    - 사실 계산하고보면 sort와 heappush 모두 O(nlogn)이었다. 실제로 시간도 동일하게 나왔다.
- 신기했던건, 입력받는 방식에따라 결과가 달라졌다.
    - 첫번째, input()으로만 받는경우 python3는 시간초과, pypy3는 EOF Error가 났다.
        - 시간초과가 아니라 내생각엔 입력을 받는것을 계속 기다리는문제가 있는것으로 추정된다.(근거는 찾아봐야함)
    - 두번째, readline과 read의 차이
        - 두개를 바꿔쓴것가지고 100 ms나 줄었다. 확실히 한번에 입력받는것과 한줄씩 입력받는 속도는 다른가보다. 
        - vscode등 IDE에서는 read의 속도차이를 확인할 수없다.
- 반올림 형식 지정하기
    - 학부수업때는 round로 배웠는데 틀렸다.
    - %.4f로 형태를 지정해주는것으로 맞을 수 있었다.
    ```python
     print('%s %.4f' %(cur_tree, tree[cur_tree]/all_num*100))
    ```

