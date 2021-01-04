/**
 1) 소요 시간 : 1시간 15분

 2) 사용 알고리즘 및 자료구조
	- 2차원 배열 회전
	- BFS 탐색

 3) 풀면서 겪었던 문제
	- 배열을 회전 시키는데 생각보다 시간이 좀 걸림

 4) 피드백
	- 몰랐던 알고리즘은 없었는데, 계산 시간이 좀 소요된다. (배열 인덱스 계산)
	  실전에서 빠르게 계산할 수 있도록 연습이 필요
 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, Q;
int iceCount, largeCount;		// 정답
int board[2][64][64];			// 2개의 판을 번갈아가면서 사용
int curIdx;						// 현재 사용하고 있는 board 인덱스
int nextIdx = 1;				// 다음 사용할(회전시킬) 보드판 인덱스
int numOfSlice[7];				// L 값에 따라 달라지는 가로 또는 세로 블록의 갯수 (offset과 반비례 관계)
int offset[7];					// L 값에 따라 건너 뛰어야 할 offset 값
int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };
bool visit[64][64];				// 방문 표시(가장 큰 얼음 덩어리를 찾을 때 사용)

// board index 스왑 함수
void swap(int& a, int& b)
{
	int tmp = a;
	a = b;
	b = tmp;
}

int Max(int a, int b) { return a > b ? a : b; }

// 경계값 검사
inline bool isIn(int r, int c)
{
	return 0 <= r && r < offset[N] && 0 <= c && c < offset[N];
}

// sr, sc : 회전시킬 시작 행과 열
// len : 회전시킬 가로(또는 세로) 길이
void rotate(const int sr, const int sc, const int len)
{
	for (int i = 0; i < len; ++i)
	{
		for (int j = 0; j < len; ++j)
		{
			board[nextIdx][sr + j][sc + len - i - 1] = board[curIdx][sr + i][sc + j];
		}
	}
}

// 얼음 녹이기
void meltProcess()
{
	vector<pair<int, int>> v;

	for (int i = 0; i < offset[N]; i++)
	{
		for (int j = 0; j < offset[N]; j++)
		{
			// 얼음이 있을 경우
			if (0 < board[curIdx][i][j])
			{
				int cnt = 0;

				// 4방향 탐색을 통해 인접 얼음 갯수 확인
				for (int k = 0; k < 4; k++)
				{
					int r = i + dr[k];
					int c = j + dc[k];

					if (isIn(r, c) && board[curIdx][r][c])
					{
						cnt++;
					}
				}

				// 인접 얼음 갯수가 3미만인 경우 얼음이 녹는다.
				if (cnt < 3)
				{
					// 녹일 얼음을 리스트에 넣는다. (미리 녹이면 값이 이상해짐)
					v.push_back({ i, j });
				}
			}
		}
	}

	// 리스트에 있는 얼음을 1만큼 녹인다.
	for (auto& pr : v)
	{
		int r = pr.first;
		int c = pr.second;

		board[curIdx][r][c]--;
	}
}

// 시뮬레이션 (회전 -> 보드판 변경 -> 얼음 녹이기)
void simulate(const int L)
{
	for (int i = 0; i < numOfSlice[L]; ++i)
	{
		for (int j = 0; j < numOfSlice[L]; ++j)
		{
			int sr = i * offset[L];
			int sc = j * offset[L];
			rotate(sr, sc, offset[L]);
		}
	}

	swap(curIdx, nextIdx);
	meltProcess();
}

void input()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> Q;

	offset[0] = numOfSlice[N] = 1;

	for (int i = 1; i <= N; i++)
	{
		offset[i] = 2 * offset[i - 1];
		numOfSlice[N - i] = offset[i];
	}

	for (int i = 0; i < offset[N]; i++)
	{
		for (int j = 0; j < offset[N]; j++)
		{
			cin >> board[curIdx][i][j];
		}
	}
}

// 가장 큰 얼음 덩어리를 찾기 위해 탐색 (BFS 탐색)
int bfs(int sr, int sc)
{
	int cnt = 1;
	queue<pair<int, int>> q;
	q.push({ sr, sc });
	visit[sr][sc] = true;

	while (!q.empty())
	{
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nr = r + dr[i];
			int nc = c + dc[i];

			// 방문 안한 인접 노드 중, 얼음 덩어리가 있으면 큐에 넣음
			if (isIn(nr, nc) && false == visit[nr][nc] && board[curIdx][nr][nc])
			{
				q.push({ nr, nc });
				visit[nr][nc] = true;
				cnt++;
			}
		}
	}

	// 인접해 있는 총 얼음 덩어리 수
	return cnt;
}

// 최종 답 계산
void calculateAnswer()
{
	for (int i = 0; i < offset[N]; i++)
	{
		for (int j = 0; j < offset[N]; j++)
		{
			// 총 합 계산
			iceCount += board[curIdx][i][j];

			if (0 == board[curIdx][i][j])
			{
				// 얼음 덩어리 없을 경우 방문 표시
				visit[i][j] = true;
			}
			else
			{
				// 얼음 덩어리 있을 경우, 방문 안했으면 탐색
				if (false == visit[i][j])
				{
					// 가장 큰 얼음 덩어리 갱신
					largeCount = Max(largeCount, bfs(i, j));
				}
			}
		}
	}
}

int main()
{
	input();

	int L;
	for (int i = 0; i < Q; i++)
	{
		cin >> L;
		simulate(L);
	}

	calculateAnswer();

	cout << iceCount << '\n' << largeCount;

	return 0;
}