/* 23:00 - 00:45 (1h 45m)
 * 사용 자료구조 : 해시 맵, 큐
 * 겪었던 문제
	- 처음에 우선순위 큐를 사용해서 풀어야 하는 문제인줄 알았다.
	- 우선 순위 큐를 사용하니 큐에서 순서가 꼬여 출력이 잘못되었다.
 * 피드백
	- 더 좋은 알고리즘을 먼저 찾기 보다, 시뮬레이션이 가능하다면 그 방법으로 먼저 풀어보기
 */

#include <string>
#include <vector>
#include <queue>
#include <map>

using namespace std;

int solution(vector<int> priorities, int location)
{
	// 순서대로 큐에 삽입
	queue<int> q;
	for (int i = 0; i < priorities.size(); i++)
	{
		q.push(i);
	}

	// key(우선순위), value(개수)
	map<int, int, greater<>> m;
	for (size_t i = 0; i < priorities.size(); i++)
	{
		m[priorities[i]]++;
	}

	int answer = 0;

	for (auto& pr : m)
	{
		int top = pr.first;		// 현재 우선순위가 가장 높은 값
		int& num = pr.second;	// 그것의 개수

		// 동일한 우선순위에에 대해 그 개수만큼 큐에서 꺼낸다.
		while (num)
		{
			int idx = q.front();
			int priority = priorities[idx];

			// 우선순위가 일치하는 경우 큐에서 빼낸다.
			if (top == priority)
			{
				answer++;
				if (location == idx) // 찾고자 하는 위치인 경우 해당 값 리턴
					return answer;

				q.pop(); // 동일 우선순위에 대해서는 그 값을 큐에서 빼낸다.
				num--;
			}
			else
			{
				// 우선순위가 더 낮은 경우 큐를 회전시킨다.
				auto value = move(q.front());
				q.pop();
				q.emplace(value);
			}
		}
	}

	return answer;
}