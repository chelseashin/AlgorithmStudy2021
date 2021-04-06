// 리모컨
// 1시간 35분

// 그리디알고리즘으로 접근했다가 틀리고 브루트포스로 해결

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(cnt);
	}

  static int channel, cnt;
  static boolean[] isBroken = new boolean[10];

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    channel = Integer.parseInt(br.readLine());
    int m = Integer.parseInt(br.readLine());

    StringTokenizer st = null;
    if (m != 0) {
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < m; i++) {
        isBroken[Integer.parseInt(st.nextToken())] = true;
      }
    }

    cnt = Integer.MAX_VALUE;
  }

  private static void solve() {
    for (int btn = 0; btn < 1000000; btn++) {
      if (!isBrokenBtn(btn)) {
        int len = String.valueOf(btn).length();
        int numPadCnt = Math.abs(channel - btn) + len;
        // System.out.println("Btn:" + btn + " len:" + (len) + " cnt:" + cnt);
        cnt = Math.min(cnt, numPadCnt);
      }
      int movePadCnt = Math.abs(channel - 100);
      cnt = Math.min(cnt, movePadCnt);
    }
  }

  private static boolean isBrokenBtn(int btn) {
    if (btn == 0) return isBroken[btn];

    while (btn > 0) {
      int tmp = btn%10;
      if (isBroken[tmp]) return true;

      btn /= 10;
    }

    return false;
  }

}
