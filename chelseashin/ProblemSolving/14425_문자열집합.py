# 참고 링크 : https://youseop.github.io/2020-11-09-BAEKJOON-14425_%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A7%91%ED%95%A9/
# 
# Trie 자료구조 - 파이썬 딕셔너리로 구현 가능

from sys import stdin
input = stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curNode = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curNode.children:
                curNode.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curNode = curNode.children[char]
        curNode.data = string

    # 문자열이 존재하는지 탐색
    def search(self, string):
        curNode = self.head

        for char in string:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
        
        if curNode.data != None:
            return True

# main
N, M = map(int, input().split())

# 방법 1 - Trie 자료구조 구현(5908ms)
wordTrie = Trie()           # 주어진 단어의 정보를 저장할 Trie 객체 생성
lenWord = [False] * 501     # 주어진 문자열과 길이가 같은 문자열에 대해서만 탐색 진행

for _ in range(N):
    word = input().strip()
    wordTrie.insert(word)   # 트라이에 단어 삽입
    lenWord[len(word)] = True
# print("wordTrie 객체로 존재", wordTrie)

result = 0      # 단어 찾은 갯수
for _ in range(M):
    word = input().strip()
    if not lenWord[len(word)]:   # 문자열 길이 다르면 탐색 X
        continue
    if wordTrie.search(word):    # 문자열 길이 같으면 탐색 O
        result += 1
print(result)

# 방법 2 - 그냥 Set 사용(320ms)
# wordSet = {input().strip() for _ in range(N)}

# find = 0
# for _ in range(M):
#     word = input().strip()
#     if word in wordSet:
#         find += 1
# print(find)

# 방법 3 - 그냥 딕셔너리 사용(300ms)
# wordDict = {input().strip(): 1 for _ in range(N)}

# find = 0
# for _ in range(M):
#     word = input().strip()
#     if word in wordDict.keys():
#         find += 1
# print(find)