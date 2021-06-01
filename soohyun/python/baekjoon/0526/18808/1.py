import sys
input = sys.stdin.readline
class Axis():
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"({self.i}, {self.j})"

    def to_tuple(self):
        return (self.i, self.j)


class Sticker():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.sticker = list()
        self.sticker_length = 0

    def rotation(self):
        for idx in range(self.sticker_length):
            self.sticker[idx].i = self.row - self.sticker[idx].i - 1 
            temp = self.sticker[idx].i
            self.sticker[idx].i = self.sticker[idx].j
            self.sticker[idx].j = temp
        tmp = self.row
        self.row = self.col
        self.col = tmp

    def __str__(self):
        all_sticker = ''
        for axis in self.sticker:
            all_sticker += str(axis) +' '
        return all_sticker


def change_tuple_set(data):
    result_set = set()
    for i in data:
        result_set.add(i.to_tuple())
    return result_set


def is_fit(sticker, i, j, notebook, N, M):
    fit_set = set()
    for partial in sticker.sticker:
        row, col = partial.i, partial.j
        nr, nc = row + i, col + j
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            return {}
        elif (nr, nc) in notebook:
            return {}
        fit_set.add((nr, nc))
    return fit_set


def change_location(N, M, sticker, notebook):
    for i in range(N):
        for j in range(M):
            fit_set = is_fit(sticker, i, j, notebook, N, M)
            if len(fit_set) > 0:
                return fit_set
    return {}


def can_attach(notebook, sticker, N, M):
    rotation_count = 4
    sticker_set = set()
    if len(notebook) == 0 and sticker.row <= N and sticker.col <= M:
        sticker_set = sticker_set.union(change_tuple_set(sticker.sticker))
        return sticker_set

    while rotation_count > 0: 
        fit_set = change_location(N, M, sticker, notebook)
        if len(fit_set) == 0:
            rotation_count -= 1
            sticker.rotation()
        else:
            sticker_set = sticker_set.union(fit_set)
            break
    return sticker_set


def print_notebook(notebook_set, N, M):
    notebook = [[0]*M for _ in range(N)]
    print("===mid result====")
    for i, j in list(notebook_set):
        notebook[i][j] = 1

    for i in range(N):
        print(*notebook[i])
    print("===mid result ===")


def main():
    notebook = set()
    N, M, K = map(int, input().rstrip().split(" "))
    for _ in range(K):
        sticker_row, sticker_col = map(int, input().rstrip().split(" "))
        sticker = Sticker(sticker_row, sticker_col)
        sticker_set = list()

        for i in range(sticker_row):
            input_row = input().rstrip().split(" ")
            for j in range(sticker_col):
               if input_row[j] == '1':
                   sticker_set.append(Axis(i, j))

        sticker.sticker = sticker_set
        sticker.sticker_length = len(sticker_set)

        attached_set = can_attach(notebook, sticker, N, M)
        notebook = notebook.union(attached_set)
        del sticker
    return len(notebook)
        

if __name__ == "__main__":
    print(main())
    
        

