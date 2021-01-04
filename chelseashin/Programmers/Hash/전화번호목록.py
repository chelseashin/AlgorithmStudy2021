# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123", "456", "789"]
phone_book = ["12", "123", "1235", "567", "88"]

# def solution(phone_book):
#     phone_book.sort(key=lambda x: len(x))
#     print(phone_book)
#     p = phone_book[0]
#     plen = len(p)
#     for num in phone_book[1:]:
#         if p == num[:plen]:
#             return False
#     return True

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#     print(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1, p2)
#         if p2.startswith(p1):
#             return False
#     return True

def solution(phone_book):
    # hashmap = {}
    # for num in phone_book:
    #     hashmap[num] = 1
    # print(hashmap)
    for num in phone_book:
        temp = ""
        for n in num:
            temp += n
            if temp in phone_book and temp != num:
                return False
    return True

print(solution(phone_book))
