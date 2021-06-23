import itertools
def solution(orders, course):
        answer = []

        for size_of_course in course: # course
            order_dict = {}
            order_combinations = []
            for order in orders:
                # 코스크기만큼 order을 조합한다.
                # combinations('ABCD', 2) --> AB AB AD BC BD CD
                comb = list(itertools.combinations(sorted(order), size_of_course))
                order_combinations.extend(comb)

            # 공통된것 숫자세기
            for order_combination in order_combinations:
                order_str = ''.join(order_combination)
                if order_str in order_dict:
                    order_dict[order_str] += 1
                else:
                    order_dict[order_str] = 1

            
            for order in order_dict:
                # 뽑혀진것중에 최대값 찾기
                if order_dict[order] == max([order_dict[order] for order in order_dict]):
                    if order_dict[order] > 1:
                        answer.append(order)


        return sorted(answer) # 오름차순으로 반환해야 하기 때문에, sorted로 정렬 해준다.
        