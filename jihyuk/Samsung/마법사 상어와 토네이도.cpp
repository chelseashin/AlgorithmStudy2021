/**
 1) 소요 시간 : 1시간 30분

 2) 사용 알고리즘
	- (상, 하, 좌, 우) 이동 처리
	- offset 전처리 - 미리 계산된 offset을 통해 탐색 범위를 줄임

 3) 풀면서 겪었던 문제
	- 제한 사항이 그렇게 빡빡한 문제가 아닌데, '최적화', '짧은 코드' 이런 것을 신경 쓰면서 구현 하려고 해서 더 오래걸렸다.
	- 남은 모래를 이동시킬 때, 기존에 있었던 모래에 더해줘야 하는데 대입해줘서 값이 이상하게 나옴

 4) 피드백
	- 문제 제한 사항을 꼼꼼히 확인하고, 빡빡하게 제한 사항을 지킬 필요가 없으면 그냥 빨리 구현할 수 있는 연습을 하자. (구현 시간 단축!)
	- 문제의 크기를 축소 시켜 알고리즘을 생각해본다.
	- 그림을 그렸을 때 직관적으로 이해할 수 있으면 펜과 노트를 옆에 두고 그림을 그려본다.
 */

#include <iostream>

using namespace std;

int board[500][500];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { -1, 0, 1, 0 };
int N;
int r, c;		// 위치
int dir;		// 진행 방향
int len;		// 이동 길이
int ans;

// 토네이도 방향에 따라 달라지는 비율 위치 offset 정보
int rowOffset[4][9] =
{
	{ -2, -1, -1, -1, 0, 1, 1, 1, 2 },
	{1, 2, 1, 0, 3, 2, 1, 0, 1},
	{2, 1, 1, 1, 0, -1, -1, -1, -2},
	{-1, -2, -1, 0, -3, -2, -1, 0, -1}
};

int colOffset[4][9] =
{
	{ -1, -2, -1, 0, -3, -2, -1, 0, -1 },
	{ -2, -1, -1, -1, 0, 1, 1, 1, 2},
	{1, 2, 1, 0, 3, 2, 1, 0, 1},
	{-2, -1, -1, -1, 0, 1, 1, 1, 2}
};

// 비율 정보
int ratio[9] = { 2, 10, 7, 1, 5, 10, 7, 1, 2 };

// 경계 체크
inline bool isIn(int r, int c)
{
	return 0 <= r && r < N && 0 <= c && c < N;
}

// 모래 이동 처리
void move()
{
	int nr = r + dr[dir]; // 다음 이동할 행
	int nc = c + dc[dir]; // 다음 이동할 열

	int amount = board[nr][nc]; // 이동할 위치에 있는 모래의 양
	int moveAmount = 0;			// 비율에 따라 이동할 모래의 양

	// 비율에 따라 모래 이동
	for (int i = 0; i < 9; i++)
	{
		moveAmount = (amount * ratio[i]) / 100; // 모래 이동량 계산

		if (0 == moveAmount) // 이동할게 없으면 넘김
			continue;

		int moveRow = r + rowOffset[dir][i];
		int moveCol = c + colOffset[dir][i];

		// 해당 비율이 있는 위치로 이동 가능한지 확인
		if (isIn(moveRow, moveCol))
		{
			board[moveRow][moveCol] += moveAmount; // 가능하면 남은 모래 이동
		}
		else
		{
			ans += moveAmount; // 경계 밖을 나간 경우
		}

		board[nr][nc] -= moveAmount; // 이동한 만큼 모래 감소
	}

	// 알파 위치로 모래 이동이 가능한지 확인
	if (isIn(nr + dr[dir], nc + dc[dir]))
	{
		board[nr + dr[dir]][nc + dc[dir]] += board[nr][nc]; // 남은 모래 이동
	}
	else
	{
		ans += board[nr][nc]; // 경계 밖을 나간 경우
	}

	r = nr, c = nc; // 현재 위치 갱신
	board[r][c] = 0; // 이동 후 현재 위치에는 모래가 남아있지 않게됨
}

void input()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			cin >> board[i][j];
		}
	}
}

int main()
{
	input();

	r = N / 2, c = N / 2; // 가운데 위치 부터 시작

	// 좌, 하, 우, 상 4방향을 모두 도는 것을 1 사이클로 처리
	for (int cycle = N / 2; 0 < cycle; cycle--)
	{
		for (int i = 0; i < 4; i++) // 4방향 움직임
		{
			if (i % 2 == 0) // 짝수번 이동할 이동 길이 1 증가
				len++;

			for (int j = 0; j < len; j++) // 현재 방향으로 이동 처리
				move();

			dir = (dir == 3) ? 0 : ++dir; // 방향 전환
		}
	}

	// 마지막에 왼쪽 방향으로 N - 1번 이동 처리 (len == N - 1)
	for (int i = 0; i < len; i++)
		move();

	cout << ans;

	return 0;
}