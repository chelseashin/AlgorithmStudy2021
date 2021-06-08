// 소용돌이 예쁘게 출력하기
// 42분

// https://blog.naver.com/11tjdnfeo/221465982078 블로그 참고

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    solve();
	}

  public static void solve() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int r1 = Integer.parseInt(st.nextToken());
    int c1 = Integer.parseInt(st.nextToken());
    int r2 = Integer.parseInt(st.nextToken());
    int c2 = Integer.parseInt(st.nextToken());
    br.close();

    int[][] grid = new int[50][50];
    int maxPlace = 0;

    for (int i = r1; i <= r2; i++) {
      for (int j = c1; j <= c2; j++) {
        int r = i - r1;
        int c = j - c1;

        if (i > j) { // 제일 긴 두 개의 대각선을 기준으로 왼쪽과 아래쪽
          if (i + j > 0) { // 왼쪽
            grid[r][c] = (i * 2 + 1) * (i * 2 + 1) - i + j;
          } else {
            grid[r][c] = (j * 2) * (j * 2) - j + 1 + i;
          }
        } else if (i == j) {
          if (i >= 0) {
            grid[r][c] = (i * 2 + 1) * (i * 2 + 1);
          } else {
            grid[r][c] = (i * (-2)) * (i * (-2)) + 1;
          }
        } else { // 제일 긴 두 개의 대각선을 기준으로 오른쪽과 왼쪽
          if (i + j < 0) {
            grid[r][c] = (i * 2) * (i * 2) + i - j + 1;
          } else {
            grid[r][c] = (j * 2 - 1) * (j * 2 - 1) + j - i;
          }
        }

        maxPlace = Math.max(maxPlace, grid[r][c]);
      }
    }

    StringBuilder sb = new StringBuilder();
    int strLen = Integer.toString(maxPlace).length();
    for (int i = r1; i <= r2; i++) {
      for (int j = c1; j <= c2; j++) {
        int r = i - r1;
        int c = j - c1;
        int tmpLen = Integer.toString(grid[r][c]).length();
        while (tmpLen < strLen) {
          sb.append(" ");
          tmpLen++;
        }

        if (j == c2) {
          sb.append(grid[r][c]).append("\n");
        } else {
          sb.append(grid[r][c]).append(" ");
        }
      }
    }

    System.out.println(sb.toString());
  }
}