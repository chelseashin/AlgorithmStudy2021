// LCS (최장 공통 부분 수열)
// 1시간 32분

// 1시간 동안 고민하다가 알고리즘 찾아봄

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    solve();
	}

  public static void solve() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    char[] str1 = br.readLine().toCharArray();
    char[] str2 = br.readLine().toCharArray();
    br.close();

    int[][] lcs = new int[1001][1001];
    for (int i = 1; i <= str1.length; i++) {
      for (int j = 1; j <= str2.length; j++) {
        if (str1[i-1] == str2[j-1]) {
          lcs[i][j] = lcs[i-1][j-1] + 1;
        } else {
          lcs[i][j] = Math.max(lcs[i][j-1], lcs[i-1][j]);
        }
      }
    }

    System.out.println(lcs[str1.length][str2.length]);
  }

}