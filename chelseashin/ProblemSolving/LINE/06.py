# 21:50 start
# 24:41 finish
# 3시간 정도 소요
# 아마 문제 읽은 시간부터 하면 더 오래 걸렸을 듯..
# 진짜 직관 그대로 풀어서 비효율적인 코드

def solution(companies, applicants):
    result = []
    compChoices = dict()    # 기업별 채용 인원 수
    compInfo = dict()       # 기업별 지원자 선호 순위
    for info in companies:
        compChoices[info[0]] = int(info[-1])
        for i, v in enumerate(info[2:-2]):
            if info[0] not in compInfo.keys():
                compInfo[info[0]] = [v]
            else:
                compInfo[info[0]].append(v)
    # print("기업 정보")
    # print(compChoices)
    # print(compInfo)

    appChoices = dict()     # 지원자별 남은 기회
    appInfo = dict()        # 지원자별 기업 선호도 순위
    for info in applicants:
        appChoices[info[0]] = int(info[-1])
        for i, v in enumerate(info[2:-2]):
            if info[0] not in appInfo.keys():
                appInfo[info[0]] = [(i, v)]
            else:
                if i < appChoices[info[0]]:
                    appInfo[info[0]].append((i, v))
                else:
                    break
    # print("지원자 정보")
    print(appChoices)
    print(appInfo)
    
    # 첫 라운드
    curMatching = {comp: [] for comp in compChoices.keys()}
    for idx, values in appInfo.items():     # 지원자별로 1순위 기업에 지원
        for i, n in values:
            curMatching[n].append((compInfo[n].index(idx), idx))    # (기업 내 지원자의 선호도, 지원자) 정보 저장
            appChoices[idx] -= 1    # 지원 기회 -1
            break

    rejected = []   # 매 라운드별로 거절당한 지원자 리스트
    for idx, values in curMatching.items():
        curMatching[idx].sort()                 # 기업별 지원자 선호도 순으로 정렬
        while len(values) > compChoices[idx]:   # 채용 인원 이외 인원들은 pop 하면서 rejected에 넣기
            i, n = curMatching[idx].pop()
            rejected.append(n)
    # print("현재 매칭 상태", curMatching, "거절", rejected)
    # print("지원자별 남은 기회", appChoices)

    # 거절당한 사람이 없을 때까지 매칭
    while rejected:
        temp = []   # 라운드별 거절당한 지원자 리스트(갱신용)
        for app in rejected:
            if not appChoices[app]:     # 기회 X
                continue
            # 기회 있다면 이미 떨어진 기업 제외하고 차순으로 기업 지원
            for i, n in appInfo[app][len(appInfo[app]) - appChoices[app]:]:
                curMatching[n].append((compInfo[n].index(app), app))    # (기업 내 지원자의 선호도, 지원자) 정보 저장
                appChoices[app] -= 1    # 지원 기회 -1
                break
        
        # 위와 같은 흐름
        for idx, values in curMatching.items():
            curMatching[idx].sort()                 # 기업별 지원자 선호도 순으로 정렬
            while len(values) > compChoices[idx]:   # 채용 인원 이외 인원들은 pop 하면서 temp에 넣기
                i, n = curMatching[idx].pop()
                temp.append(n)
        rejected = temp     # 탈락자 갱신
    # print("현재 매칭 상태", curMatching)

    # 최종 매칭상태 형식 맞추어 출력
    for idx, values in curMatching.items():
        temp = []
        for i, n in curMatching[idx]:
            temp.append(n)
        temp.sort()
        result.append(idx + "_" + ''.join(temp))

    return result

print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))
print(solution(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"]))