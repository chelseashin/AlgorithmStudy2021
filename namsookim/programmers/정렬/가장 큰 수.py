# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
# 10:18 시작
# 11:21 끝
# 1시간 소요
"""
https://wooaoe.tistory.com/82 참고.

풀이

1. 문자열 정렬을 하면 ASCII 값으로 치환되어 정렬된다. 666,101010 등의 첫번째 인덱스 값으로 비교함.

2. map을 활용해 int형을 string 형태의 리스트로 변환

3. 333,101010,308308308 등 길이를 맞추어 비교할 수 있도록 람다식을 활용해 *3을 함.
  - 문제의 제한은 값이 1000 이하이기 때문에 3배해서 비교해도 됨.

4. 0과 같은 예외 케이스 처리위해 str(int(''.join(num))) 사용 int()로 감싸기
"""

def solution(numbers):

    num = list(map(str,numbers))
    num.sort(key= lambda x: x*3,reverse= True) # 핵심. 문자열마다 길이가 달라 크기비교하기 위해 3번 반복시킨 값으로 비교
    return str(int(''.join(num))) # int로 감싸는 이유. 0값을 처리해주기 위해 안해주면 000이렇게 나옴

print(solution([0,0, 0, 0, 0]))
