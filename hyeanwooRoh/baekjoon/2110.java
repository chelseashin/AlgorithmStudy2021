// 공유기 설치
// 시간 의미 없음

// 답보고 해결했다
// 저번 입국심사와 비슷하게 전혀 다른 관점에서 해결해야되는데 도무지 생각나는게 없었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, C;
  static int[] home;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    home = new int[N];
    for (int i = 0; i < N; i++) {
      home[i] = Integer.parseInt(br.readLine());
    }
    br.close();
  }

  private static void solve() {
    Arrays.sort(home);
    int left = 1;
    int right = home[N-1] - home[0];
    int maxDist = 0;

    while (left <= right) {
      int mid = (left + right) / 2;
      int start = home[0];
      int cnt = 1;

      for (int i = 1; i < N; i++) {
        int dist = home[i] - start;
        if (mid <= dist) {
          start = home[i];
          cnt++;
        }
      }

      if (cnt >= C) {
        left = mid + 1;
        maxDist = mid;
      } else {
        right = mid - 1;
      }
    }

    System.out.println(maxDist);
  }
}
