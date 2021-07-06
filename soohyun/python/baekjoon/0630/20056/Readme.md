# 문제의 핵심
- 구현
# 실수했던것과 헷갈렸던것
 - 좌표 순환: ```(node.row + \
            N + (DIRECTION[node.direction][0] * node.speed) % N ) % N ```
 - speed계산 실수: ```total_speed // len(node_list) + 1``` => ```total_speed // len(node_list)```
 - 새로 생성되지 않았을경우(두개이상 없는경우)는 그대로 저장해야함
 ```python
  if len(new_node_list) > 1:
                new_node_list, mass = add(new_node_list)
                mass_result += mass
            else:
                mass_result += new_node_list[0].mass
            node_list.extend(new_node_list)
```


