participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    temp = 0
    D = {}
    for part in participant:
        D[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= int(hash(com))
    return D[temp]

print(solution(participant, completion))