# 문제의 핵심
- greedy하게 문제푸는 방법
- 아이디어가 필요함

# 알고리즘 설명
- ex) ABCD + BCD = 1000A + 110B + 20C + 2D
- 숫자 계산(count alpha)
- 앞의 숫자가 큰순서대로 알파벳 정렬후 앞 숫자가 큰순서대로 9부터 차례로 숫자 배정
(decide_number)

# code snippet
1. count_alpha
```python
def count_alpha(alpha_list):
    alpha_dict = dict()
    for word in alpha_list:
        size = len(word)
        for idx, value in enumerate(word):
            if alpha_dict.get(value, -1) < 0:
                alpha_dict[value] = 10 ** (size-(idx+1))
            else:
                alpha_dict[value] += 10 ** (size-(idx+1))
    return alpha_dict
```

2. decide_number
```python
def decide_number(alpha_dict):
    alpha_num = dict()
    salpha = dict(sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True))
    number = 9
    for key in salpha.keys():
        alpha_num[key] = number
        number -= 1
    return alpha_num


```
# 복기할것
- 아이디어 싸움.. 처음에는 위치로만 했다가 틀림
- 첫번째는 ABBB+BBB*10 이 틀렸음..