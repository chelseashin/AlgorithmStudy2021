import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    int[][] arr = {{0,1,0},{1,1,1},{1,1,0},{0,1,1}};
    int[][] arr2 = {{1,0,0},{1,0,0}};
    int[][] arr3 = {{1,0,0,1,1},{0,0,0,0,0},{1,1,0,0,0},{0,0,0,0,1}};
    System.out.println(solution(arr));
    // System.out.println(solution(arr2));
    // System.out.println(solution(arr3));
	}

  static long MOD = 10000019l;
  static long[][] combi;

  public static long getComb(int n, int r) {
    if (n < r) return 0;
    if (combi[n][r] != 0) return combi[n][r];

    if (n == r || r == 0) return combi[n][r] = 1;
    return combi[n][r] = (getComb(n - 1, r - 1) + getComb(n - 1, r)) % MOD;
  }

  public static int solution(int[][] arr) {
    int n = arr.length;
    int m = arr[0].length;
    combi = new long[301][301];

    // j열의 1의 갯수
    int[] oneCnts = new int[m+1];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        oneCnts[j+1] += arr[i][j];
      }
    }

    // dp[col][row] = arr[0 ~ row][0 ~ col]까지의 행이 짝수인 경우의 수
    long[][] dp = new long[m+1][n+1];
    dp[1][n - oneCnts[1]] = getComb(n, oneCnts[1]);

    for (int col = 1; col <= m; col++) {
      int oneCnt = oneCnts[col];
      for (int row = 0; row <= n; row++) {
        // 기존에 있던 행 중 짝수 개의 1을 가진 행에 1을 세팅하고자 하는 갯수. (가정)
        for (int k = 0; k <= oneCnt; k++) {
          // 기존에 있던 행 중 홀수 개의 1을 가진 행에 1을 세팅하고자 하는 갯수 = col열이 가진 1의 갯수 중 짝수 개를 가진 행에 세팅할 1을 뺀 나머지
          int willSetOddRow = oneCnt - k;
          // 1을 세팅하고 난 뒤 1을 짝수 개 가진 행의 갯수 = (짝수 행 중  1을 세팅하지 않는 행) + (홀수 행 중 1을 세팅하는 행)
          int willBeEvenRowCnt = (row - k) + willSetOddRow;
          if (willSetOddRow < 0 || willBeEvenRowCnt < 0 || willBeEvenRowCnt > n) continue;

          // 경우의 수 = (짝수 행에 1을 세팅하는 경우의 수) * (홀수 행에 1을 세팅하는 경우의 수) % MOD
          long numOfCase = (getComb(row, k) * getComb(n - row, oneCnt - k)) % MOD;
          dp[col][willBeEvenRowCnt] += dp[col-1][row] * numOfCase % MOD;
          dp[col][willBeEvenRowCnt] %= MOD;
          // for (int i = 0; i < dp.length; i++) {
          //   System.out.println(Arrays.toString(dp[i]));
          // }
          // System.out.println();
        }
      }
    }

    return (int) dp[m][n];
  }
}
