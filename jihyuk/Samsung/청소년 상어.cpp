/*
 * 20:20 ~ 22:50 (1h 30m)
 * 알고리즘 구분 : simulation
 * 겪었던 문제
	- 상어 번호와 마지막 물고기 번호를 동일한 값을 설정해서 값이 이상해짐
	- 결과 값을 누적 계산 해서 값이 크게 나옴.
 * 피드백
	- 배열의 인덱스나 상수 값을 +1, -1 했을 때 다른 연산 결과를 유발하는 경우를 잘 생각하자
	- 재귀적인 구조일 경우, 1~2 깊이까지 들어가는 입력값을 주어 값을 확인해보자.
	- 문제 지문을 다시 보는 경우가 많다. 글을 읽으면서 메모장을 열어두고 제한 조건이나, 구현 사항을 조각 조각 적어본다.
 */

#include <iostream>
#include <memory.h>

using namespace std;

constexpr int SHARK = 17;

int max(int a, int b) { return a > b ? a : b; }

struct Fish
{
	int r, c, dir;
	bool isAlive = true;
};

struct Shark
{
	int r, c, dir;
};

int dr[8] = { -1, -1, 0, 1, 1, 1,0 , -1 };
int dc[8] = { 0, -1, -1, -1, 0, 1, 1, 1 };
int board[4][4];

Fish fish[17];
Shark shark;

inline bool isIn(const int r, const int c)
{
	return 0 <= r && r < 4 && 0 <= c && c < 4;
}

// 물고기 이동 처리
void MoveFish()
{
	for (int idx = 1; idx <= 16; idx++)
	{
		if (fish[idx].isAlive) // 살아 있는 경우 이동 처리
		{
			int& dir = fish[idx].dir;
			int r = fish[idx].r;
			int c = fish[idx].c;

			// 8방향을 확인하면서 이동 가능한지 체크
			for (int i = 0; i < 8; i++)
			{
				int nr = r + dr[dir];
				int nc = c + dc[dir];

				// 현재 방향으로 이동 불가능한 경우 다음 방향 확인
				if (!isIn(nr, nc) || board[nr][nc] == SHARK)
				{
					dir = dir == 7 ? 0 : dir + 1;
					continue;
				}

				// 이동 가능한 경우
				int swapIdx = board[nr][nc];

				// 물고기가 있는 공간으로 이동하는 경우 스왑
				if (0 != swapIdx && fish[swapIdx].isAlive)
				{
					board[r][c] = swapIdx;
					board[nr][nc] = idx;

					fish[idx].r = fish[swapIdx].r;
					fish[idx].c = fish[swapIdx].c;
					fish[swapIdx].r = r;
					fish[swapIdx].c = c;
				}
				// 빈 공간으로 이동하는 경우 위치만 이동
				else
				{
					board[nr][nc] = idx;
					board[r][c] = 0;

					fish[idx].r = nr;
					fish[idx].c = nc;
				}

				break;
			}
		}
	}
}

// 물고기를 먹고 상어를 해당 위치로 이동시킨다.
int EatFish(int r, int c)
{
	int idx = board[r][c];
	fish[idx].isAlive = false;
	board[r][c] = SHARK;

	return idx;
}

// 반복을 위한 재귀함수
int solve(int r, int c, int cnt)
{
	int dir = fish[board[r][c]].dir; // 먹을 물고기 위치 방향으로 설정

	cnt += EatFish(r, c); // 먹은 물고기 번호만큼 누적
	MoveFish(); // 물고기 이동 처리

	// 이전 상태로 되돌리기 위해 값 복사
	Fish tempFish[17];
	memcpy(tempFish, fish, sizeof(fish));

	int tempBoard[4][4];
	memcpy(&tempBoard[0][0], &board[0][0], sizeof(board));

	int ret = cnt;

	// 상어 이동 처리
	for (int dist = 1; dist < 4; dist++)
	{
		int nr = r + dist * dr[dir];
		int nc = c + dist * dc[dir];

		// 경계를 벗어난 경우 더이상 검사할 필요가 없다.
		if (!isIn(nr, nc))
			break;

		// 물고기가 없는 경우 건너 뛴다.
		if (0 == board[nr][nc])
		{
			continue;
		}

		board[r][c] = 0;
		ret = max(ret, solve(nr, nc, cnt)); // 다음 위치로 이동시킨다. 리턴 값이 더 크다면 갱신
		memcpy(fish, tempFish, sizeof(fish)); // 복원
		memcpy(&board[0][0], &tempBoard[0][0], sizeof(board));
		board[r][c] = SHARK;
	}

	return ret;
}

void Input()
{
	int dir, idx;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> idx >> dir;

			board[i][j] = idx;

			fish[idx].r = i;
			fish[idx].c = j;
			fish[idx].dir = dir - 1;
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	Input();

	cout << solve(0, 0, 0);

	return 0;
}