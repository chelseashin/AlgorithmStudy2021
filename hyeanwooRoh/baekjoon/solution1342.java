// 행운의 문자열
// 1시간 17분

// 처음에 Set으로 중복제거했더니 메모리 터짐
// 문자열 해싱까지 고민했다가 구현이 까다로워서 접고
// 카운트를 다 구한다음에 중복되는 문자만큼 나눠서 계산

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    solve();
    System.out.println(cnt);
	}

  static char[] arr;
  static boolean[] visit;
  static int cnt;

  private static void solve() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    arr = br.readLine().toCharArray();
    visit = new boolean[arr.length];
    cnt = 0;

    getTotalCnt("", 0, ' ');
    int divideNum = duplicateCharacter();

    cnt /= divideNum;
  }

  private static void getTotalCnt(String str, int depth, char prevChar) {
    if (depth == arr.length) {
      cnt++;
      return;
    }

    for (int i = 0; i < arr.length; i++) {
      if (!visit[i] && arr[i] != prevChar) {
        visit[i] = true;
        getTotalCnt(str + arr[i], depth + 1, arr[i]);
        visit[i] = false;
      }
    }
  }

  private static int duplicateCharacter() {
    int[] chars = new int[26];
    for (char c : arr) {
      chars[c-'a']++;
    }

    int divideNum = 1;
    for (int n : chars) {
      divideNum *= factorial(n);
    }

    return divideNum;
  }

  private static int factorial(int n) {
    if (n == 0 || n == 1) return 1;

    int t = 1;
    for (int i = 1; i <= n; i++) {
      t *= i;
    }
    return t;
  }

}
