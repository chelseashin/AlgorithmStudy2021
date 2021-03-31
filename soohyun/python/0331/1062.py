#시작 3시 30분
#끝 
import sys
WORDS = dict()


def dfs(index_set, start, words_set, K): 
    #print("start", index_set, len(words_set))
    max_num = 0
    if len(words_set) > K:
        return 0
    count = 0
    for i in range(start, len(WORDS.keys())):
        word_set = WORDS[i]
        store_words_set = words_set 
        new_set = words_set.union(word_set)
        index_set.add(i)
        count = dfs(index_set, i+1, new_set, K)
        if len(words_set) <= K:
            count += 1
        index_set.remove(i)
        words_set = store_words_set
        if max_num <= count:
            max_num = count
    return max_num
  
def main():
    '''
    input: N, K word
    output: max word
    풀이전략: dfs
    '''
    global WORDS
    N, K = map(int, sys.stdin.readline().strip().split(" "))
    for i in range(N):
        WORDS[i] = set(map(str, sys.stdin.readline().strip()))
    max_count = 0
    #print(WORDS)
    #for i in range(N):
    i = 0
    count = dfs(set(), 0, set(), K)
        #if max_count <= count:
        #    max_count = count
    return count
    

if __name__ == "__main__":
    print(main())