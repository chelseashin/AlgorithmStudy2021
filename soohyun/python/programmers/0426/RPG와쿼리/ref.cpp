#include <string>
#include <vector>
#include <cstring>

using namespace std;

typedef long long ll;

vector<pair<int, int>> v[3001];
int dp[3001][2501];
int cost[2501];
int INF = 1e9;

void calc(int n, int z) {
    memset(cost, -1, sizeof(cost));
    for(int i = 1; i <= n; i++) {
        for(int j = 0; j <= z * z; j++) {
            dp[i][j] = INF;
        }
    }

    dp[1][0] = 0;
    for(int i = 0; i <= z * z; i++) {
        int costTmp = INF;

        for(int j = 1; j <= n; j++) {
            costTmp = min(costTmp, dp[j][i]);
        }
        if(costTmp == INF) continue;
        for(int j = 1; j <= n; j++) {
            dp[j][i] = min(dp[j][i], costTmp + 1);
        }
        cost[i] = costTmp;

        for(int j = 1; j <= n; j++) {
            for(auto next : v[j]) {
                if(next.second + i > z * z) continue;
                dp[next.first][next.second + i] = min(dp[next.first][next.second + i], dp[j][i] + 1);
            }
        }
    }
}

vector<ll> solution(int n, int z, vector<vector<int>> roads, vector<ll> queries) {
    vector<ll> answer;

    for(auto e : roads) {
        v[e[0] + 1].push_back({e[1] + 1, e[2]});
    }

    calc(n, z);
    for(int q = 0; q < queries.size(); q++) {
        if(queries[q] % (ll)z == 0) {
            answer.push_back(queries[q] / (ll)z);
            continue; 
        }

        int remain = queries[q] % (ll)z;
        ll cnt = queries[q] / (ll)z;
        ll ans = -1;

        while(cnt >= 0 && remain <= z * z) {
            if(cost[remain] != -1) {
                if(ans == -1) ans = (ll)cost[remain] + cnt;
                else ans = min(ans, (ll)cost[remain] + cnt);
            }
            cnt -= 1;
            remain += z;
        }
        answer.push_back(ans);
    }
    return answer;
}
