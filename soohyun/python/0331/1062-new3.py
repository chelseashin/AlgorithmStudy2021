import sys
sys.setrecursionlimit(10**6)


def combination_generate(chosen, before):
    if len(chosen)==k-5:
        compare(chosen)
        return

    for idx, v in enumerate(L[before+1:]):
        idx+=before
        if not visited[idx]:
            chosen.add(v)
            visited[idx] = True
            combination_generate(chosen, idx)
            visited[idx] = False
            chosen.remove(v)


def compare(learn):
    global learn_know
    now_class_know = 0

    for member in can_study:
        understand = True
        for word in member:
            if word not in learn:
                understand = False
                break
        if understand:
            now_class_know += 1

    learn_know = max(now_class_know, learn_know)


n, k = map(int, input().split())
if k<5:
    print(0)
else:
    less = {'a', 'n', 't', 'i', 'c'}

    can_study, always_know, learn_know = [], 0, 0
    for _ in range(n):
        S, spell = input(), set()
        for s in S:
            if s in less:
                continue
            if s not in spell:
                spell.add(s)

        if not spell:
            always_know += 1
        elif len(spell) <= k-5:
            can_study.append(spell)

    L = []
    for i in range(97, 123):
        alpha = chr(i)
        if alpha not in less:
            L.append(alpha)

    visited = [False]*21
    combination_generate(set(), -1)
    print(always_know+learn_know)