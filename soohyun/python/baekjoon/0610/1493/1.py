# 문제
import sys
sys.setrecursionlimit(100000000) 

def is_smaller_than_boxes(h_length, l_length, w_length, boxes):
    for box in boxes.keys():
        if h_length >= box and l_length >= box and w_length >= box:
            return False
    return True


def is_same(h_length, l_length, w_length, boxes):
    if h_length == l_length and l_length == w_length:
        if boxes.get(h_length, 0) > 0:
            return True
    return False


def divide_and_conquer(start_h, end_h, start_l, end_l, start_w, end_w, boxes):
    result = 0
    print(start_h-end_h, start_l-end_l, start_w-end_w, boxes)
    if is_smaller_than_boxes(end_h-start_h, end_l-start_l, end_w-start_w, boxes):
        return 0

    elif is_same(end_h-start_h, end_l-start_l, end_w-start_w, boxes):
        box = end_h-start_h
        boxes[box] -= 1
        if boxes[box] <= 0:
            boxes.pop(box)
        return 1

    else:
        mid_h = (start_h + end_h) // 2
        result += divide_and_conquer(start_h, mid_h, start_l, end_l, start_w, end_w, boxes)
        result += divide_and_conquer(mid_h+1, end_h, start_l, end_l, start_w, end_w, boxes)
        mid_l = (start_l + end_l) // 2
        result += divide_and_conquer(start_h, end_h, start_l, mid_l, start_w, end_w, boxes)
        result += divide_and_conquer(start_h, end_h, mid_l+1, end_l, start_w, end_w, boxes)
        mid_w = (start_w + end_w) // 2
        result += divide_and_conquer(start_h, end_h, start_l, end_l, start_w, mid_w, boxes)
        result += divide_and_conquer(start_h, end_h, start_l, end_l, mid_w+1, end_w, boxes)
        return result

    


def main():
    l, w, h = map(int, input().rstrip().split(" "))
    num_of_box = int(input())
    boxes = dict()
    for i in range(num_of_box):
        box, num = map(int, input().rstrip().split(" "))
        boxes[2**(box)] = num
    #print(boxes)
    print(divide_and_conquer(0, h, 0, l, 0, w, boxes))



if __name__ == "__main__":
    main()
