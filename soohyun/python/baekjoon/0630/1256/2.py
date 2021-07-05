from itertools import permutations
def main():
    N, M, K = map(int, input().rstrip().split(" "))
    words = ['a' for _ in range(N)]
    count = 0
    data = set()
    for _ in range(M):
        words.append('z')
    for word in permutations(''.join(words), len(words)):
        if word in data:
            continue
        else:
            if count == K-1:
                print(count+1, ''.join(word))
                break
            data.add(word)
            count += 1
        #if count == K:
        #    print(''.join(word))
        #    break
        #count += 1


if __name__ == "__main__":
    main()