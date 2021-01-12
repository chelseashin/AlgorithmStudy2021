/* 21:00 - 22:00
 * 사용 알고리즘 : 투포인터
 * 사용 자료구조 : 큐
 * 겪었던 문제
	- 다리에 진입하는 시기, 다리에서 나가는 시기 두 위치에 대한 계산을 하는데 시간이 오래 걸림
 * 피드백
	- 시간에 따른 상태를 쭉 나열해보고, 코드로 구현한 것을 시뮬레이션 헀을 때 일치하는지 확인 필요
 */

#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
	queue<int> q;

	int time = 0;
	int start = 0;
	int end = 0;

	// 트럭이 다 지나갈 때까지 반복
	while (start < truck_weights.size())
	{
		// 다리에서 가장 앞쪽의 트럭이 빠져나갈 수 있는 경우
		if (!q.empty() && bridge_length + q.front() <= time)
		{
			q.pop();
			weight += truck_weights[start++];
		}

		// 다리에서 가장 뒤쪽의 트럭이 진입 가능한 경우
		if (end < truck_weights.size() && truck_weights[end] <= weight)
		{
			weight -= truck_weights[end];
			q.push(time);
			end++;
		}

		time++;
	}

	return time;
}