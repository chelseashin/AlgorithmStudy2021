/* 20:15 - 21:00 (45min)
 * 사용 알고리즘 및 자료구조 : 큐 (vector 컨테이너를 큐처럼 사용)
 * 겪었던 문제
	- 날짜 계산 후, 큐에서 꺼내야 하는 개수를 개산하는데 시간이 좀 걸렸다.
 * 피드백
	- 나머지가 있는 경우 +1을 해야 하는 상황에서, 원래 값에서 -1을 한 값을 나눈 몫에 1을 더하는 경우를 생각해보자.
 */
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
	vector<int> answer;

	answer.push_back(1);
	int needDay = (99 - progresses[0]) / speeds[0] + 1;
	int curDay = needDay;

	for (size_t i = 1; i < progresses.size(); ++i)
	{
		needDay = (99 - progresses[i]) / speeds[i] + 1;

		if (curDay < needDay)
		{
			curDay = needDay;
			answer.push_back(1);
		}
		else
		{
			++answer.back();
		}
	}

	return answer;
}