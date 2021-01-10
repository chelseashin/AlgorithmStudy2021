/**
 1) 소요 시간 : 1시간 30분

 2) 사용 알고리즘
	- 조합
 
 3) 풀면서 겪었던 문제
	- 조합을 직접 구현했는데 1번 case에서 시간 초과남
	- 다른 블로그 사이트 참고해서 해결

 4) 피드백
	이러한 패턴의 조합 풀이법을 알아두면 좋을듯 하다.
	1. hash를 통해 counting
	2. counting한 수에 선택 안하는 선택지를 포함 시킨다. ( +1 )
 */

#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes)
{
	map<string, int> m;
	for (size_t i = 0; i < clothes.size(); ++i)
	{
		// 중복키 제거, 동일 키에 대해 counting
		m[clothes[i][1]]++;
	}

	int answer = 1;

	for (auto& pr : m)
	{
		// counting 한 수에 선택 안하는 선택지를 포함 시켜 곱한다.
		answer *= pr.second + 1;
	}

	return answer - 1;
}