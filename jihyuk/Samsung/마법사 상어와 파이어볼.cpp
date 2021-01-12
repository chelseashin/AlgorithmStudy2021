/**
 1) 소요 시간 : 3시간

 2) 알고리즘 및 자료구조
	- 8방향 이동 처리, 단순 구현
	- 겹쳐지는 파이어볼을 담을 수 있는 자료구조 필요(vector사용)

 3) 풀면서 겪었던 문제
	- 제한 사항이 그렇게 빡빡한 문제가 아닌데, '최적화', '짧은 코드' 이런 것을 신경 쓰면서 구현 하려고 해서 더 오래걸렸다.
	- 경계 값을 벗어난 경우, 단순히 N을 더하고 빼줘서 문제가 됐음. 속도가 N의 2배가 넘어가면 문제가 됨

 4) 피드백
	- 시간을 고려하지 않고, 처음 시작부터 너무 최적화, 짧은 코드에 신경써서 생각하는 시간이 길어진다.
	- 몰랐던 알고리즘, 자료구조가 없었음에도 생각보다 오래 걸렸다.
	  제한 조건이 빡빡하지 않다면 일단 빠르게 구현할 수 있는 연습을 하자.
	  우선순위 : (구현 시간 단축 > 최적화)
 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Fireball
{
	// 행, 열, 질량, 속도, 방향
	int r, c, m, s, d;
};

int N, M, K;

// 8 방향 (행, 열)
int dr[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dc[8] = { 0 , 1, 1, 1, 0, -1, -1, -1 };

int even[4] = { 0,2,4,6 };		// 모두 홀수 또는 짝수인 경우
int odd[4] = { 1,3,5,7 };		// 하나라도 방향이 다른 경우

vector<Fireball> board[50][50]; // 전체 맵(보드판)
queue<Fireball> q;				// 현재 이동할 수 있는 파이어볼을 담는 큐

inline void adjust(int& r, int& c) // 경계 값 벗어난 경우 조정
{
	while (r < 0)
		r += N;

	while (N <= r)
		r -= N;

	while (c < 0)
		c += N;

	while (N <= c)
		c -= N;
}

// 이동 명령
void Move()
{
	while (!q.empty())
	{
		auto fb = q.front();
		q.pop();

		int dir = fb.d;
		int speed = fb.s;

		int& r = fb.r;
		int& c = fb.c;

		r += dr[dir] * speed;
		c += dc[dir] * speed;

		adjust(r, c);

		board[r][c].push_back(fb);
	}
}

// 합치는 연산
void merge(vector<Fireball>& v, const int count)
{
	int r = v[0].r;
	int c = v[0].c;
	int m = 0;
	int s = 0;
	int d = v[0].d % 2; // 첫번째 파이볼이 홀수인지 짝수인지 일단 체크

	bool isSame = true; // 모두 같은 방향인지 체크

	for (int i = 0; i < count; i++)
	{
		m += v[i].m;
		s += v[i].s;

		// 모두 같은 방향(짝수, 홀수)인지 체크 (한번이라도 다른 경우가 있는지 체크)
		if (isSame && d != (v[i].d % 2))
		{
			isSame = false;
		}
	}

	m /= 5;
	if (m == 0) // 질량이 0인 경우 파이어볼이 나눠지지 않으므로, early return 처리
		return;

	s /= count; // 속도 / 파이어볼 개수

	if (isSame)
	{
		// 모두 같은 방향인 경우 (0, 2, 4, 8) 방향으로 4개의 파이어볼 생성
		for (int i = 0; i < 4; i++)
		{
			q.push({ r, c, m, s, even[i] });
		}
	}
	else
	{
		// 다른 방향이 있는 경우 (1, 3, 5 7) 방향으로 4개의 파이어볼 생성
		for (int i = 0; i < 4; i++)
		{
			q.push({ r, c, m, s, odd[i] });
		}
	}
}

// 이동 후 합칠 수 있는지 체크
void CheckAndMerge()
{
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			int count = board[i][j].size();
			auto& v = board[i][j]; // 파이어볼 리스트를 담고있는 vector 컨테이너

			if (1 < count)
			{
				merge(v, count); // 2개 이상인 경우 합침 (합친 후 나눠진 파이어볼을 큐에 넣는다.)
			}
			else if (1 == count)
			{
				q.push(v[0]); // 1개만 있는 경우 그대로 큐에 넣음
			}
			v.clear();
		}
	}
}

void input()
{
	cin >> N >> M >> K;

	int r, c, m, s, d;
	for (int i = 0; i < M; ++i)
	{
		cin >> r >> c >> m >> s >> d;
		r--, c--;
		q.push({ r, c, m, s, d });
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	input();

	for (int i = 0; i < K; ++i)
	{
		Move();
		CheckAndMerge();
	}

	int result = 0;

	// K번의 명령 이후, 마지막에 큐에 남아있는 파이어볼의 질량을 합산한다.
	while (!q.empty())
	{
		result += q.front().m;
		q.pop();
	}

	cout << result;

	return 0;
}