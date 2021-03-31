import sys
sys.setrecursionlimit(10**6)

def dfs(chosen, before, k):
    if len(chosen) == k-5:
        compare(chose)
        return
    for idx, v in enumerate(L[before+1:]):
        idx+=before
        if not visited[idx]:
            chosen.add(v)
            visited[idx] = True
            dfs(chosen, idx, k)
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

    
def main():
    n, k = map(int, input().split())
    default_word = {'a', 'n', 't', 'i', 'c'}
    if k < 5:
        return 0

    for _ in range(n):
        S, spell = input(), set()
        for i in S:
            if i in default_word:
                continue
            if i not in spell:
                spell.add(i)

            if not spell:
                always_know += 1
            elif len(spell) <= k-5:
                can_study.append(spell)
    visited = [False] * 21
    dfs(set(), -1)
    print(always_know+learn_know)

if __name__ == "__main__":
    print(main())