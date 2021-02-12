"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo

2시간 56분 소요

1시간 디버깅(시간초과)

문제
1. 원자들이 주어지고 원자들이 매초마다 동시에 (상,하,좌,우) 이동한다.
2. 원자들이 충돌하면 에너지를 방출한다.
3. 방출하는 에너지의 총합을 구하여라.

풀이
1. dictionary를 사용하였다. 3개 사용. energy_info, del_atom, new_atom
2. 좌표를 1씩 이동시킨 것이 아니라 0.5씩 이동시켰다.

시행착오
1. 시간초과 -> 리스트를 딕셔너리로 변경(효과 조금)
2. 충돌을 했는 지 체크를 통해서 충돌했을 경우에만 코드 실행(에너지 계산) -63번째 줄
3. 원자 개수를 바로 더하고 빼줌. len(atom) 사용한 부분 수정
4. 문제의 조건에 따르면 -1000 미만, 1000 초과하는 부분에서는 절대 원자가 충돌할 수 없다.
   이 원자들은 무시해주어 시간 초과 해결(핵심)
"""

def solve(atom):
    # 각 좌표는 0.5씩 이동
    dx = [0.0,0.0,-0.5,0.5]
    dy = [0.5,-0.5,0.0,0.0]

    time = 0
    answer = 0

    while time<=4000:

        time += 0.5
        energy_info=dict([])
        del_atom = dict([])
        new_atom = dict([]) # 삭제할 거 삭제되고 좌표,방향,에너지 담긴 원자배열

        total_cnt = 0 # 새로운 위치로 이동했을 때 원자의 개수
        tag = False # 충돌 했는지 판단

        for position,dir_energy in atom.items(): # x좌표, y좌표, 방향, 에너지
            # 새로운 위치로 이동시켰을 때
            x,y = position[0],position[1]
            dir, k =dir_energy[0],dir_energy[1]
            nx = x+dx[dir]
            ny = y+dy[dir]

            if nx<-1000 or ny<-1000 or nx>1000 or ny>1000: # -1000 , 1000 범위 넘어가면 충돌할 수가 없음
                continue # 이부분 추가해줘서 맞음
            find=energy_info.get((nx,ny))

            if find == None: # 해당 좌표에 원자가 없으면
                energy_info[(nx, ny)] = k # 해당 좌표에 에너지 쌓기
                new_atom[(nx,ny)] = (dir,k)
                total_cnt +=1 # 원자개수 증가

            else: # 다른 원자가 이미 있으면
                # 에너지 충돌 여러개가 동시에 할 수 있음
                energy_info[(nx,ny)] = find + k # 에너지 더함
                del_atom.setdefault((nx,ny),0)  # 삭제할 원자 좌표
                tag = True

        if tag == True: # 충돌을 했으면

            for ener_x,ener_y in del_atom.keys(): # 충돌 한 부분 에너지 계산해주기
                xy_energy =energy_info.get((ener_x,ener_y))
                answer += xy_energy
                energy_info.pop((ener_x,ener_y))

                # new_atom에 있는 부분 중 삭제해야 될 것 삭제해주기
                new_atom.pop((ener_x,ener_y))
                total_cnt -= 1 # 전체 원자개수에서 충돌한 부분은 삭제

        # 현재 원자 몇개 있는지
        if total_cnt == 0 or total_cnt == 1:
            return answer

        atom = new_atom

    return answer


import sys
sys.stdin =open('5648(원자 소멸 시뮬레이션).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 원자들의 수
    # x,y, 이동방향, 보유 에너지 K
    atom = dict([]) # 원자 위치, 이동방향, 보유 에너지 기록

    for _ in range(N):
        x,y,direction,energy = map(int,input().split())
        atom.setdefault((x,y),(direction,energy))


    print('#{0} {1}'.format(tc,solve(atom)))



