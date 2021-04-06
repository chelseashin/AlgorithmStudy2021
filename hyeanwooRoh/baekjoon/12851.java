// 숨바꼭질2
// 1시간 34분

// boolean으로 방문처리를 해줬더니 예외가 발생해서 int형으로 바꿔 저장해가며 처리했다
// 열받는 점은 처음 계획은 int형으로 하려고 했다는 점이다
// 문제를 볼때 문제가 숨기고 있는 부분을 잘 파악하는게 중요하겠다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(time);
    System.out.println(cnt);
	}

  static int N, K, time, cnt;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] st = br.readLine().split(" ");
    N = Integer.parseInt(st[0]);
    K = Integer.parseInt(st[1]);
    time = Integer.MAX_VALUE;
    cnt = 0;
    br.close();
  }

  static int[] visited = new int[100001];

  private static void solve() {
    Queue<Subin> queue = new LinkedList<>();
    queue.add(new Subin(N, 0));
    visited[N] = -1;

    while (!queue.isEmpty()) {
      Subin sub = queue.poll();
      int x = sub.x;
      int t = sub.t;

      if (t > time) continue;

      if (x == K) {
        if (t < time) {
          time = t;
          cnt = 1;
        } else {
          cnt++;
        }
      }

      if (x-1 >= 0 && (visited[x-1] == 0 || t < visited[x-1])) {
        queue.add(new Subin(x-1, t+1));
        visited[x-1] = t+1;
      }
      if (x+1 < visited.length && (visited[x+1] == 0 || t < visited[x+1])) {
        queue.add(new Subin(x+1, t+1));
        visited[x+1] = t+1;
      }
      if (x*2 < visited.length && (visited[x*2] == 0 || t < visited[x*2])) {
        queue.add(new Subin(x*2, t+1));
        visited[x*2] = t+1;
      }

    }
  }

  static class Subin {
    int x;
    int t;

    public Subin(int x, int t) {
      this.x = x;
      this.t = t;
    }
  }
}