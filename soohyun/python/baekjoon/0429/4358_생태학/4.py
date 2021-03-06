    # 시작 8시 35분
    # 끝 9시 6분
import sys
import heapq
input = sys.stdin.read
def main():
    tree = dict()
    all_num = 0
    trees = input().split('\n')
    for result in trees[:-1]:
        tree[result] = tree.get(result, 0) + 1
        all_num += 1
    sorted_dic = sorted(tree.keys())
    for cur_tree in sorted_dic:
        print('%s %.4f' %(cur_tree, tree[cur_tree]/all_num*100))

if __name__ == "__main__":
    main()