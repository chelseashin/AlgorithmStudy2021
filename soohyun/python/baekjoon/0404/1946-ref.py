import sys
input = sys.stdin.readline
def solution():
    case = int(input())
    answers = []
    for _ in range(case):
        n = int(input())
        scores = [0]*(n+1)
        for _ in range(n):
            s1, s2 = map(int, input().split())
            scores[s1] = s2
        answer = 1
        min = scores[1]
        for score in scores[2:]:
            if(score<min):
                answer += 1
                min = score
        answers.append(str(answer))
    print('\n'.join(answers))
solution()