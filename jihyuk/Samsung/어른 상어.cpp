/*
 * 23:20 ~ 01:20 (2h)
 * 알고리즘 구분 : simulation
 * 겪었던 문제
	- 조건에 맞는 이동 처리하는데 시간이 좀 걸렸다.
 * 피드백
	- 문제 지문을 다시 보는 경우가 많다. 필요 조건이나 구현 사항을 구현 전에 미리 적어본다.
	- 머릿속으로만 생각하지말고 한 사이클 돌았을 때 배열의 상태가 어떤지 미리 출력하는 구문을 생각해본다.
 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 상어 정보
struct Shark
{
	int r, c, d;
	int p[4][4];
	bool alive = true;
};

// 냄새 정보
struct Scent
{
	int t, n; // (시간, 상어 번호)
};

struct Position
{
	int r, c;
};

// 상어가 이동한 위치 정보
struct MoveInfo
{
	int r, c, n; // 행, 열, 상어 번호
};

int N, M, k;
int board[20][20];
Scent scent[20][20]; // 냄새 정보 저장

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
int totalTime;

vector<Shark> sharks;
queue<Position> q;
queue<MoveInfo> mergeQ;

inline bool isIn(const int r, const int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

// 이동 로직
// moveEmptySpace 가 true이면 빈 공간으로 이동
// false이면 자신의 냄새 공간으로 이동
bool MoveTo(int r, int c, int& d, int n, bool moveEmptySpace)
{
	for (int idx = 0; idx < 4; idx++)
	{
		int dir = sharks[n].p[d][idx];
		int nr = r + dr[dir];
		int nc = c + dc[dir];

		if (moveEmptySpace) // 빈 공간 이동 가능한지 확인
		{
			if (!isIn(nr, nc) || totalTime <= scent[nr][nc].t)
			{
				continue;
			}
		}
		else // 자신의 냄새 공간으로 이동 가능한지 확인
		{
			if (!isIn(nr, nc) || (n != scent[nr][nc].n && totalTime <= scent[nr][nc].t))
			{
				continue;
			}
		}

		// 이동이 가능하다면 이동 정보를 merge 큐에 넣는다.
		d = dir;
		board[r][c] = 0;
		mergeQ.push({ nr, nc, n });

		return true;
	}

	return false;
}

int Solve()
{
	for (int i = 1; i <= M; i++)
		q.push({ sharks[i].r, sharks[i].c });

	int restCnt = M;

	while (1 < restCnt && totalTime < 1000)
	{
		// 냄새 남기기
		for (int i = 1; i <= M; i++)
		{
			if (sharks[i].alive)
			{
				int r = sharks[i].r;
				int c = sharks[i].c;

				scent[r][c].n = i;
				scent[r][c].t = totalTime + k; // 냄새가 사라지는 시간 기록
			}
		}

		totalTime++;

		// 큐에 담겨진(살아있는) 상어 이동 처리
		int qSize = q.size();
		for (int i = 0; i < qSize; i++)
		{
			int r = q.front().r;
			int c = q.front().c;
			int n = board[r][c];
			int& d = sharks[n].d;

			q.pop();

			if (false == MoveTo(r, c, d, n, true))
			{
				MoveTo(r, c, d, n, false);
			}
		}

		// 이동 후 merge 큐에 담겨진 상어들 병합 처리
		while (!mergeQ.empty())
		{
			int r = mergeQ.front().r;
			int c = mergeQ.front().c;
			int n = mergeQ.front().n;
			mergeQ.pop();

			sharks[n].r = r;
			sharks[n].c = c;

			if (0 == board[r][c]) // 아직 해당 행, 열에 상어를 놓지 않은 경우
			{
				board[r][c] = n;
				q.push({ r, c });
			}
			else if (n < board[r][c]) // 더 낮은 번호의 상어가 들어온 경우
			{
				sharks[board[r][c]].alive = false;
				restCnt--;
				board[r][c] = n;
			}
			else // 번호가 더 큰 상어인 경우
			{
				sharks[n].alive = false;
				restCnt--;
			}
		}
	}

	return restCnt;
}

void Input()
{
	cin >> N >> M >> k;
	sharks.resize(M + 1);

	int idx;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> idx;
			board[i][j] = idx;
			if (idx)
			{
				sharks[idx].r = i;
				sharks[idx].c = j;
			}
		}
	}

	for (int i = 1; i <= M; i++)
	{
		cin >> sharks[i].d;
		sharks[i].d--;
	}

	for (int i = 1; i <= M; i++)
	{
		Shark& s = sharks[i];
		for (int j = 0; j < 4; j++)
		{
			cin >> s.p[j][0] >> s.p[j][1] >> s.p[j][2] >> s.p[j][3];
			s.p[j][0]--, s.p[j][1]--, s.p[j][2]--, s.p[j][3]--;
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	Input();

	int restCnt = Solve();

	if (1 < restCnt)
	{
		cout << -1;
	}
	else
	{
		cout << totalTime;
	}

	return 0;
}