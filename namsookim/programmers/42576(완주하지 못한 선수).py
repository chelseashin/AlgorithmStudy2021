# https://programmers.co.kr/learn/courses/30/lessons/42576
"""
1. 처음에는 단순히 participant 리스트를 기준으로 .remove() 를 했었는데 효율성에서 실패했다.
   remove 내장함수는 내부에서 반복문을 돌리기 때문이다.
2. 각각 정렬해주어 인덱스를 기준으로 처리했다. 참여자와 완주자의 인덱스가 같으면 완주했다는 뜻이고, 다르면 참여자 배열에서
   해당 인덱스 위치에 있는 사람을 리턴해주고 모든 반복문을 거쳤을 때도 안나오면 participant의 마지막 원소를 반환

"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant) - 1):
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]
    else:
        return participant[-1]

#print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))