import sys
WORDS = dict()


def dfs(start, words_set, K):
    global WORDS
    print(start, len(words_set))
    if len(words_set) > K:
        return 0
    else:
        result = list()
        answer = 0
        for _ in range(start, len(WORDS)-1):
            #print(start+1, words_set, len(words_set))
            data = WORDS[start].union(words_set)
            print("data", len(data), start)
            result.append(dfs(start+1, data.union(WORDS[start+1]), K))
            answer = max(result)
            if len(data) <= K:
                print("after", len(data), data)
                answer = answer + 1
        return answer


def main():
    # input
    global WORDS
    N, K = map(int, sys.stdin.readline().strip().split(" "))
    for i in range(N):
        WORDS[i] = set(map(str, sys.stdin.readline().strip()))
    # dfs
    default_word_set = {'a', 't', 'i', 'c', 'n'}
    result = list()
    result = dfs(0, default_word_set, K)
    return result


if __name__ == "__main__":
    print(main())
