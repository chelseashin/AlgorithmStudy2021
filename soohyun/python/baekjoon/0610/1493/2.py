def divide_and_conquer(l, w, h, boxes, box_list):
    result = 0
    print(l, w, h, boxes, box_list)
    if l <= 0 or w <= 0 or h <= 0:
        return 0
    elif l==w and w==h and boxes.get(l, 0) > 0:
        boxes[l] -= 1
        return 1
    else:
        for idx in range(len(box_list)-1, -1, -1):
            if boxes.get(box_list[idx], 0) > 0:
                print("IDX", idx)
                box = box_list[idx]
                result += divide_and_conquer(l-box, w, h, boxes, box_list)
                print("reduce length", result)
                result += divide_and_conquer(l, w-box, h, boxes, box_list)
                print("reduce width", result)
                result += divide_and_conquer(l, w, h-box, boxes, box_list)
                print("result height", result)
        return result



def main():
    l, w, h = map(int, input().rstrip().split(" "))
    num_of_box = int(input())
    boxes = dict()
    box_list = list()
    for i in range(num_of_box):
        box, num = map(int, input().rstrip().split(" "))
        boxes[2**(box)] = num
        box_list.append((2**box))
    box_list.sort()
    #print(boxes)
    print(divide_and_conquer(l, w, h, boxes, box_list))

if __name__ == "__main__":
    main()