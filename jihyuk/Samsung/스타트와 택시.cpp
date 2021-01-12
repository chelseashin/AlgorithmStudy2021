/* 13:15 - 14:45 (1h 30m)
 * 사용 알고리즘 : BFS
 * 겪었던 문제
	- 우선 순위 비교, 최단 거리, 남은 연료 계산 등 고려해야 할 사항이 많아서 디버깅 시간이 오래걸림
 * 피드백
	- 로직 처리 뿐만 아니라, 디버깅을 위해 출력 구문을 중간 중간 삽입 하는게 좋을듯 하다.
 */

#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
#include<memory.h>

using namespace std;

const int MAX = 20;

int N, M, fuel;
int board[MAX][MAX];
bool visit[MAX][MAX];
int dr[] = { 0, 0, 1, -1 };
int dc[] = { 1, -1, 0, 0 };

struct Position
{
	int r, c;
};
struct Customer
{
	Position startPos, endPos;
};
struct DistInfo
{
	int r, c, dist;
};
struct PriorityInfo
{
	int r, c, dist, num;
};
Position taxiPos;
Customer customer[MAX * MAX + 1];

void input()
{
	scanf("%d%d%d", &N, &M, &fuel);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &board[i][j]);
			if (board[i][j])
			{
				board[i][j] = -board[i][j];
			}
		}
	}

	scanf("%d%d", &taxiPos.r, &taxiPos.c);
	taxiPos.r--;
	taxiPos.c--;

	for (int i = 1; i <= M; i++)
	{
		Position& s = customer[i].startPos;
		Position& e = customer[i].endPos;

		scanf("%d%d%d%d", &s.r, &s.c, &e.r, &e.c);
		s.r--, s.c--, e.r--, e.c--;
		board[s.r][s.c] = i;
	}
}

bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

// 우선순위 비교 함수 (거리, 행, 열 순으로 비교)
bool comp(const PriorityInfo& a, const PriorityInfo& b)
{
	if (a.dist == b.dist)
	{
		if (a.r == b.r)
		{
			return a.c < b.c;
		}
		return a.r < b.r;
	}

	return a.dist < b.dist;
}

// 다음 태울 승객을 찾는다.
int findCustomer()
{
	memset(visit, false, sizeof(visit));

	queue<DistInfo> q;
	q.push({ taxiPos.r, taxiPos.c, 0 });
	visit[taxiPos.r][taxiPos.c] = true;

	vector<PriorityInfo> v; // 태울 승객 정보를 저장(마지막에 우선순위에 따라 정렬된다.)

	while (!q.empty())
	{
		int qSize = q.size();
		for (int loopCnt = 0; loopCnt < qSize; loopCnt++)
		{
			int r = q.front().r;
			int c = q.front().c;
			int dist = q.front().dist;
			int restFuel = fuel - dist; // 남은 연료
			q.pop();

			// 승객이 있으면 태운다.
			if (0 < board[r][c])
			{
				v.push_back({ r, c, dist, board[r][c] });
			}

			// 남은 연료가 없는 경우
			if (0 == restFuel)
			{
				continue;
			}

			// 현재 위치에서 이동 가능한 4방향을 탐색해서 큐에 삽입
			for (int i = 0; i < 4; i++)
			{
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (isIn(nr, nc))
				{
					if (-1 != board[nr][nc] && false == visit[nr][nc])
					{
						visit[nr][nc] = true;
						q.push({ nr, nc, dist + 1 });
					}
				}
			}
		}

		// 태울 승객을 찾은 경우
		if (0 < v.size())
		{
			break;
		}
	}

	// 승객을 못찾은 경우
	if (v.size() == 0)
		return 0;

	sort(v.begin(), v.end(), comp);
	board[v[0].r][v[0].c] = 0;
	fuel -= v[0].dist;
	return v[0].num;
}

// 승객을 이동시킨다.
bool bfs(int num)
{
	memset(visit, false, sizeof(visit));

	Position& startPos = customer[num].startPos;
	Position& endPos = customer[num].endPos;

	queue<DistInfo> q;
	q.push({ startPos.r, startPos.c, 0 });
	visit[startPos.r][startPos.c] = true;

	vector<PriorityInfo> v;

	while (!q.empty())
	{
		int r = q.front().r;
		int c = q.front().c;
		int dist = q.front().dist;
		int restFuel = fuel - dist;
		q.pop();

		if (r == endPos.r && c == endPos.c) // 목적지에 도착한 경우
		{
			fuel += dist;
			taxiPos = { r, c };
			return true;
		}
		else if (restFuel == 0) // 목적지에 도착 못하고 연료가 바닥난 경우
		{
			return false;
		}

		for (int i = 0; i < 4; i++)
		{
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (isIn(nr, nc))
			{
				if (-1 != board[nr][nc] && false == visit[nr][nc])
				{
					visit[nr][nc] = true;
					q.push({ nr, nc, dist + 1 });
				}
			}
		}
	}
	return false;
}

void solve()
{
	for (int i = 0; i < M; i++)
	{
		int idx = findCustomer();
		if (0 == idx)
		{
			printf("-1");
			return;
		}

		if (false == bfs(idx))
		{
			printf("-1");
			return;
		}
	}

	printf("%d", fuel);
}

int main()
{
	input();
	solve();
}
