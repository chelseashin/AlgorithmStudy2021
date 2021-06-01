// 회전초밥
// 대략 2시간

// 단순한 투포인터 문제였는데 너무 어렵게 접근했다
// 불필요한 변수를 만들어사용하느라 코드가 꼬인것 같다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println();
	}

  static int n, k, c;
  static int[] belt, sushi;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    n = Integer.parseInt(st.nextToken());
    int d = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());

    sushi = new int[d+1];
    belt = new int[n];
    for (int i = 0; i < n; i++) {
      belt[i] = Integer.parseInt(br.readLine());
    }

    br.close();
  }

  public static void solve() {
    int max = 0;
    int cnt = 0;

    for (int i = 0; i < k; i++) {
      if (sushi[belt[i]] == 0) cnt++;
      sushi[belt[i]]++;
    }
    max = cnt;

    for (int i = 1; i < n; i++) {
      if (max <= cnt) {
        if (sushi[c] == 0) {
          max = cnt + 1;
        } else {
          max = cnt;
        }
      }

      sushi[belt[i-1]]--;
      if (sushi[belt[i-1]] == 0) cnt--;

      int right = (i + k - 1) % n;
      if (sushi[belt[right]] == 0) cnt++;
      sushi[belt[right]]++;
    }

    System.out.println(max);
  }

}