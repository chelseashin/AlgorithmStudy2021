#시작: 03 15 1시 10분
#끝: 1시 36분
def solution(boxes):
    pair_box = dict()
    box_num = len(boxes)
    for box in boxes:
        for gift_num in box:
            if pair_box.get(gift_num) != None:
                pair_box.pop(gift_num)
            else:
                pair_box[gift_num] = 0
    return len(pair_box.keys() ) // 2

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))