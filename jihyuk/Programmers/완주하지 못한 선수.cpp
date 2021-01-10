/**
 1) 소요 시간 : 10분

 2) 사용 알고리즘 및 자료구조
	- map 자료구조 사용
 
 3) 풀면서 겪었던 문제
	
 */

#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion)
{
	map<string, int> m;

	// 이름 별로 참가자 수 계산
	for (int i = 0; i < participant.size(); i++)
		m[participant[i]]++;

	// 완주자 이름별로 개수 감소
	for (int i = 0; i < completion.size(); i++)
		m[completion[i]]--;

	string answer = "";

	for (auto& pr : m)
	{
		// 완주하지 않은 사람이 있을 경우
		if (0 < pr.second)
		{
			// 완주 못한 사람 이름 저장
			answer = pr.first;
			break;
		}
	}

	return answer;
}