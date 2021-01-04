/**
 1) 소요 시간 : 1시간 30분

 2) 사용 알고리즘 및 자료구조
	- 우선순위 큐
	- 정렬 (연산자 오버로딩을 통한 정렬)
 
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
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

struct Music
{
	// 노래의 인덱스 번호, 플레이 수
	int idx, cnt;

	// 플레이 수로 우선순위 큐에서 정렬된다.
	const bool operator<(const Music& rhs) const
	{
		return cnt < rhs.cnt;
	}
};

// 통계 : 해당 장르의 총 합을 나타냄
struct Statistics
{
	int tatoal = 0;
	priority_queue<Music> q; // 우선순위 큐 : 해당 장르에서 플레이수가 높은 것이 heap의 top에 배치된다.

	// 가장 플레이수가 높은 장르를 정렬하기 위한 연산자 오버로딩
	const bool operator<(const Statistics& rhs) const
	{
		return tatoal > rhs.tatoal;
	}
};

vector<int> solution(vector<string> genres, vector<int> plays)
{
	map<string, Statistics> m;

	for (int i = 0; i < genres.size(); i++)
	{
		m[genres[i]].tatoal += plays[i];		// 장르 총 플레이수 누적
		m[genres[i]].q.push({ i, plays[i] });	// 해당 장르에 음악(노래 인덱스, 플레이수)을 추가
	}

	vector<Statistics> v;
	v.reserve(m.size());

	for (auto& pr : m)
	{
		// 통계 데이터 저장
		v.emplace_back(std::move(pr.second));
	}

	// 장르별 총 누적 플레이수별로 내림차순 정렬
	sort(v.begin(), v.end());

	vector<int> answer;

	for (size_t i = 0; i < v.size(); i++)
	{
		auto& q = v[i].q;
		for (int j = 0; j < 2; j++)
		{
			if (!q.empty())
			{
				// 해당 장르에서 top2 음악을 push (1개만 있을 경우 1개만 push)
				answer.push_back(q.top().idx);
				q.pop();
			}
		}
	}

	return answer;
}