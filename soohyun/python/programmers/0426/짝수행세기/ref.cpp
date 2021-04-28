#include <vector>
 
#define MODULER 10000019
using namespace std;
 
void Calculate_Combination(vector<vector<long long>> &V, int Row)
{
    V[0][0] = 1;
    for (int i = 1; i <= Row; i++)
    {
        for (int j = 0; j <= Row; j++)
        {
            if (j == 0) V[i][j] = 1;
            else if (i == j) V[i][j] = 1;
            else V[i][j] = V[i - 1][j - 1] + V[i - 1][j];
 
            V[i][j] %= MODULER;
        }
    }
}
 
void Calculate_OneCnt(vector<int> &V, vector<vector<int>> MAP)
{
    for (int i = 0; i < MAP.size(); i++)
    {
        for (int j = 0; j < MAP[0].size(); j++)
        {
            V[j] += MAP[i][j];
        }
    }
}
 
int solution(vector<vector<int>> a) 
{
    int Row = a.size();
    int Col = a[0].size();
    
    vector<vector<long long>> nCr(Row + 1, vector<long long>(Row + 1, 0));
    Calculate_Combination(nCr, Row);
 
    vector<int> Arr_OneCnt(Col + 1, 0);
    Calculate_OneCnt(Arr_OneCnt, a);
 
    vector<vector<long long>> DP(Col + 2, vector<long long>(Row + 1, 0));
    DP[1][Row - Arr_OneCnt[0]] = nCr[Row][Row - Arr_OneCnt[0]];
 
    for (int Column = 1; Column < Col; Column++)
    {
        int OneCnt = Arr_OneCnt[Column];
        for (int Even_Num = 0; Even_Num <= Row; Even_Num++)    
        {
            if (DP[Column][Even_Num] == 0) continue;
            for (int K = 0; K <= OneCnt; K++)
            {
                if (Even_Num < K) continue;
 
                int Be_Even_Row = Even_Num + OneCnt - (2 * K);
                if (Be_Even_Row > Row) continue;
 
                long long Result = (nCr[Even_Num][K] * nCr[Row - Even_Num][OneCnt - K]) % MODULER;
                DP[Column + 1][Be_Even_Row] = (DP[Column + 1][Be_Even_Row] + DP[Column][Even_Num] * Result);
                DP[Column + 1][Be_Even_Row] %= MODULER;
            }
        }
    }
    return DP[Col][Row];
}


//출처: https://yabmoons.tistory.com/583 [얍문's Coding World..]