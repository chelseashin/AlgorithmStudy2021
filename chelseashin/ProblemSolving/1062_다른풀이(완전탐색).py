# 참고 링크 : https://dirmathfl.tistory.com/176

from sys import stdin
input = stdin.readline

def dfs(depth, pos):
    global answer
    if depth == K-5:    # 새로 배워야할 알파벳 수에 다다랐을 때
        readCnt = 0     # 읽을 수 있는 단어 갯수
        for word in wordsLst:
            for w in word:
                if not learn[ord(w)-ord('a')]:  # 배우지 않은 알파벳이라면
                    break
            else:
                readCnt += 1
        # print(readCnt)
        answer = max(answer, readCnt)   # 최댓값 갱신
        return
    
    for i in range(pos, 26):
        if learn[i]:
            continue
        learn[i] = 1        # 알파벳 배우기
        dfs(depth+1, i+1)
        learn[i] = 0        # 복원
        
# main
N, K = map(int, input().split())
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    wordsLst = [set(input().rstrip()) for _ in range(N)]
    learn = [0] * 26
    for s in 'acint':
        learn[ord(s)-ord('a')] = 1      # 배움 표시
    answer = 0
    dfs(0, 0)
    print(answer)