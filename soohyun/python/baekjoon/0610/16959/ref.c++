#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;
//나이트의 이동
const int niy[8] = { 2,1,-1,-2,-2,-1,1,2 };
const int nix[8] = { 1,2,2,1,-1,-2,-2,-1 };
//비숍의 이동
const int by[4] = { 1,1,-1,-1 };
const int bx[4] = { 1,-1,-1,1 };
//룩의 이동
const int ly[4] = { 1,-1,0,0 };
const int lx[4] = { 0,0,1,-1 };
int n;

int a[10][10];
// y,x 좌표 // 찾아야하는 숫자 ( 0 ~ n*n -1 까지 ) // 0은 나이트 1은 비숍 2는 룩
int d[10][10][100][3];
int main()
{
	memset(d, -1, sizeof(d));
	queue<tuple<int, int, int, int>> q;
	cin >> n;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			cin >> a[i][j];
			a[i][j]--;

			if (a[i][j] == 0) {
				//처음이 나이트인지 비숍인지 룩인지 모르므로 3개 다 넣어준다.
				for (int k = 0; k < 3; ++k) {
					d[i][j][0][k] = 0;
					q.push({ i,j,0,k });
				}
			}
		}

	int ans = -1;
	while (!q.empty())
	{
		int y, x, num, cand;
		tie(y, x, num, cand) = q.front();
		q.pop();

		// n*n-1까지 완료 시
		if (num == n * n - 1) {
			if (ans == -1 || ans > d[y][x][num][cand]) {
				ans = d[y][x][num][cand];
			}
		}
		// 가만히 있고 말을 바꿀 시
		for (int i = 0; i < 3; ++i) {
			if (cand == i) continue;

			if (d[y][x][num][i] == -1) {
				d[y][x][num][i] = d[y][x][num][cand] + 1;
				q.push({ y,x,num,i });
			}
		}

		// 나이트
		if (cand == 0) {
			for (int i = 0; i < 8; ++i) {
				int ny = y + niy[i];
				int nx = x + nix[i];

				if (0 <= ny && ny < n && 0 <= nx && nx < n) {
					int nextnum = num;
					if (a[ny][nx] == num + 1) {
						nextnum = num + 1;
					}

					if (d[ny][nx][nextnum][cand] == -1) {
						d[ny][nx][nextnum][cand] = d[y][x][num][cand] + 1;
						q.push({ ny,nx,nextnum,cand });
					}
				}
			}
		}
		// 비숍
		else if (cand == 1) {
			for (int i = 0; i < 4; ++i) {
				for (int k = 1; ; k++) {
					int ny = y + by[i] * k;
					int nx = x + bx[i] * k;

					if (0 <= ny && ny < n && 0 <= nx && nx < n) {
						int nextnum = num;
						if (a[ny][nx] == num + 1) {
							nextnum = num + 1;
						}
						if (d[ny][nx][nextnum][cand] == -1) {
							d[ny][nx][nextnum][cand] = d[y][x][num][cand] + 1;
							q.push({ ny,nx,nextnum,cand });
						}
					}
					else
						break;
				}
			}
		}
		// 룩
		else if (cand == 2) {
			for (int i = 0; i < 4; ++i) {
				for (int k = 1; ; k++) {
					int ny = y + ly[i] * k;
					int nx = x + lx[i] * k;

					if (0 <= ny && ny < n && 0 <= nx && nx < n) {

						int nextnum = num;
						if (a[ny][nx] == num + 1) {
							nextnum = num + 1;
						}
						if (d[ny][nx][nextnum][cand] == -1) {
							d[ny][nx][nextnum][cand] = d[y][x][num][cand] + 1;
							q.push({ ny,nx,nextnum,cand });
						}
					}
					else
						break;

				}
			}
		}
	}
	cout << ans << "\n";
	return 0;
}