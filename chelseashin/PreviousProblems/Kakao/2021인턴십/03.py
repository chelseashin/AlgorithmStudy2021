def solution(n, k, cmd):
    check = [1] * n     # 1: 존재, 0 : 삭제
    stack = []
    for command in cmd:
        print(command, "명령 후 stack", stack, "check", check, "현 위치", k)
        if len(command) > 2:
            x, cnt = command.split()
            if x == "U":    # 위로 n만큼 이동
                num = 0
                for i in range(k-1, -1, -1):
                    if check[i]:
                        num += 1
                        if num == int(cnt):
                            k = i
                            break
            else:           # 아래로 n만큼 이동
                num = 0
                for i in range(k+1, len(check)):
                    if check[i]:
                        num += 1
                        if num == int(cnt):
                            k = i
                            break
        else:
            if command == "C":      # 현재 선택 행 지우기
                stack.append(k)     # 몇 번째 행이 지워졌는지
                check[k] = 0
                if k == n-1:
                    for nk in range(k-1, -1, -1):
                        if check[nk]:
                            k = nk
                            break
                else:
                    for nk in range(k+1, n):
                        if check[nk]:
                            k = nk
                            break
                    else:
                        for nk in range(k-1, -1, -1):
                            if check[nk]:
                                k = nk
                                break
            else:   # 최근 삭제 행 복원
                x = stack.pop()
                check[x] = 1        # 복원
                if x < k:
                    for nk in range(k, n):
                        if check[nk]:
                            k = nk
                            break
                    else:
                        for nk in range(k-1, -1, -1):
                            if check[nk]:
                                k = nk
                                break
        print(command, "명령 후 stack", stack, "check", check, "현 위치", k)
        print("------------------------------------------------------------------------")

    answer = ''
    for chk in check:
        if chk: answer += "O"
        else: answer += "X"
    return answer

# 처음 표의 행 개수를 나타내는 정수 n
# 처음에 선택된 행의 위치를 나타내는 정수 k
# 수행한 명령어들이 담긴 문자열 배열 cmd
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))