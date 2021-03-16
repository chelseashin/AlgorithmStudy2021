def solution(companies, applicants):
    result = []
    # print(companies)
    # print(applicants)
    compChoices = dict()    # 기업별 채용 인원 수
    compInfo = dict()       # 기업별 지원자 선호 순위
    for info in companies:
        compChoices[info[0]] = int(info[-1])
        for i, v in enumerate(info[2:-2]):
            if info[0] not in compInfo.keys():
                compInfo[info[0]] = [v]
                # compInfo[info[0]] = [(i, v)]
            else:
                compInfo[info[0]].append(v)
                # compInfo[info[0]].append((i, v))
    print("기업 정보")
    print(compChoices)
    print(compInfo)
    appChoices = dict()
    appInfo = dict()
    for info in applicants:
        appChoices[info[0]] = int(info[-1])
        for i, v in enumerate(info[2:-2]):
            if info[0] not in appInfo.keys():
                appInfo[info[0]] = [(i, v)]
            else:
                if i < appChoices[info[0]]:
                    appInfo[info[0]].append((i, v))
    print("지원자 정보")
    print(appChoices)
    print(appInfo)
    curMatching = {comp: [] for comp in compChoices.keys()}

    for idx, values in appInfo.items():
        if appChoices[idx]:
            for pt, comp in values:
                curMatching[comp].append((compInfo[comp].index(idx), idx))
                appChoices[idx] -= 1
                print(pt, comp)
                break
    rejected = []
    for idx, values in curMatching.items():
        curMatching[idx].sort()
        while len(values) > compChoices[idx]:
            rejected.append(curMatching[idx].pop()[1])
    print("현재 매칭 상태", curMatching, "거절", rejected)
    print(appChoices)

    while rejected:

    #     break
    return result

print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))
# print(solution(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"]))