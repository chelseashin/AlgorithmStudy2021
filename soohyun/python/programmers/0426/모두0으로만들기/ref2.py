import collections
# 출처:  programmers id a1029
def check(a):
    if sum(a)==0:
        return True
    return False

def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    indegree = [0]*(len(a))
    for i,j in edges:
        tree[i].append(j)
        tree[j].append(i)
        indegree[i] += 1
        indegree[j] += 1

    leaf = collections.deque()
    for i in range(len(indegree)):
        if indegree[i]==1:
            leaf.append(i)
    visit = set()
    res = 0
    while leaf:
        now = leaf.popleft()
        visit.add(now)
        for nxt in tree[now]:
            if nxt not in visit:
                t = a[now]
                a[now] -= t
                a[nxt] += t
                res += abs(t)
                indegree[nxt] -= 1
                if indegree[nxt]==1:
                    leaf.append(nxt)
    if check(a):
        return res
    else:
        return -1