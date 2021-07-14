def get_min(boxes):
    box_size = sorted(list(boxes.keys()), reverse=True)
    box_count = 0

    def recursive(area):
        count = 0
        while len(boxes) > 0:
            print(area)
            if area < 0:
                return -1
            elif area == 0:
                return count
            if boxes[box] > 0:
                boxes[box] -= 1
                count += 1
                area -= (box * box * box)
        return count
    return recursive

def main():
    boxes = dict()
    l, w, h = map(int, input().rstrip().split(" "))
    N = int(input().rstrip())
    for _ in range(N):
        pow, count = map(int, input().rstrip().split(" "))
        boxes[2**pow] = count
    result = get_min(boxes)
    print(result(l*w*h))

if __name__ == "__main__":
    main()