
def solution(preorder, N):
    visited = [False for _ in range(N)]
    def make_tree(start, end, count):
        if start <= end:
            node = None
            for i in range(N):#in enumerate(preorder[0][count:]):
                if not visited[i]:
                    visited[i] = True
                    node = preorder[0][i]
                    break
            postorder_idx = preorder[1][i]
            make_tree(start, postorder_idx-1, count+1)
            make_tree(postorder_idx+1, end, postorder_idx+1)
            print(node, end=" ")
            return node
        return None
        
    return make_tree


def post_order(tree):
    if tree.left is not None:
        post_order(tree.left)
    if tree.right is not None:
        post_order(tree.right)
    print(tree.value, end=" ")


def main():
    for _ in range(int(input().rstrip())):
        N = int(input().rstrip())
        preorder = list()
        preorder.append(list(map(int, input().rstrip().split(" "))))
        inorder = list(map(int, input().rstrip().split(" ")))
        preorder.append([inorder.index(value) for value in preorder[0]])
        make_tree = solution(preorder, N)
        #tree = make_tree(0, N-1, 0)
        make_tree(0, N-1, 0)
        #post_order(tree)
        print("")



if __name__ == "__main__":
    main()
