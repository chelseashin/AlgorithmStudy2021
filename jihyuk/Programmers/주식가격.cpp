/* 20:00 - 20:15
 * 알고리즘 및 자료구조 : 스택
 * 겪었던 문제
	- 처음 풀이시 2중 for loop를 사용하여 비효율적으로 풀었따.
	- 스택을 사용하면 될거 같았지만 잘 생각 나지 않음
 * 피드백
	- 스택 문제는 넣는 것보다 어느 타이밍에 값을 빼야하는지가 문제인듯 하다.
	- 자주 나오는 유형이라 그런지 비슷한 문제를 본 것 같다. 비슷한 문제를 풀어보자
 */
#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices)
{
	vector<int> answer(prices.size());
	stack<int> s;

	for (size_t i = 0; i < prices.size(); ++i)
	{
		while (!s.empty() && prices[i] < prices[s.top()])
		{
			answer[s.top()] = i - s.top();
			s.pop();
		}

		s.push(i);
	}

	int maxIndex = prices.size() - 1;
	while (!s.empty())
	{
		answer[s.top()] = maxIndex - s.top();
		s.pop();
	}

	return answer;
}