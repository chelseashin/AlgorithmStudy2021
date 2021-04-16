# include <iostream>
# include <string>
using namespace std;

// const int MAX = 1000;

string graph[1000];
int visited[1000][1000];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;

    string s;
    cin >> s;

    for (int i = 0; i < N; i++)
            graph[0] += s[i];

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            if (graph[i][j] == "#")     // 검은색 타일이면
            {
                // 좌
                if (j > 0)
                    visited[i][j-1] ^= 1;
                // 우
                if (j < N-1)
                    visited[i][j+1] ^= 1;
                // 하
                if (i < N-1)
                    visited[i+1][j] ^= 1;
            }
        for (int j = 0; j < N; j++)
            if (visited[i][j])
                graph[i+1] += "#";
            else
                graph[i+1] += ".";
        for (int j = 0; j < N; j++)
            cout << graph[i][j];
        cout << "\n";
    }
    return 0;
}