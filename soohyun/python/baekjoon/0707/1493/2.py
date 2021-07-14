import sys
input = sys.stdin.readline
class Box():
    def __init__(self, size, count):
        self.size = size
        self.count = count
    def __str__(self):
        return f'{self.size} {self.count}'

def count_box(box_dict):
    global counts
    counts = 0
    def recursive(velocity, l, w, h):
        global counts
        result = False
        if velocity == 0:
            return True
        elif velocity < 0:
            return False
        else:
            box_sizes = list(box_dict)
            for i in range(0, len(box_sizes)):
                box_size = box_sizes[i].size
                if l >= box_size and w >= box_size and h >= box_size:
                    result = recursive(velocity-(box_size**3), l, w, h)
                    if result:
                        if box_sizes[i].count > 0:
                            box_dict[i].count -= 1
                            counts += 1
                        else:
                            box_dict.pop(0)
                else:
                    box_dict.pop(0)
            return result
    return recursive 



def main():
    l, w, h = map(int, input().rstrip().split(" "))
    box_dict = []
    for _ in range(int(input())):
        size, count = map(int, input().rstrip().split(" "))
        box_dict.append(Box(2**size, count))
    box_dict = sorted(box_dict, key=lambda x: x.size, reverse=True)
    print(*box_dict)
    #result = count_box(box_dict)
    #result(l*w*h, l, w, h)
    #print(counts)


if __name__ == "__main__":
    main()