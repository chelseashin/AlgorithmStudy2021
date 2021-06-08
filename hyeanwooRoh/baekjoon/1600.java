// 말이 되고픈 원숭이
// 1시간

// 말로 움직일 수 있는 카운트횟수를 visited배열로 처리가 핵심

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    System.out.println(solve());
	}

  static int K, N, M;
  static int[][] map;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = null;

    K = Integer.parseInt(br.readLine());
    
    st = new StringTokenizer(br.readLine());
    M = Integer.parseInt(st.nextToken());
    N = Integer.parseInt(st.nextToken());
    map = new int[N][M];

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    br.close();
  }

  static int[] di = {0,0,1,-1};
  static int[] dj = {1,-1,0,0};
  static int[] dhi = {-2, -1, 1, 2, 2, 1, -1, -2};
  static int[] dhj = {1, 2, 2, 1, -1, -2, -2, -1};

  public static int solve() {
    boolean[][][] visited = new boolean[N][M][K+1];
    Queue<Monkey> queue = new LinkedList<>();
    queue.add(new Monkey(0,0,0,0));
    visited[0][0][0] = true;
    visited[0][0][1] = true;

    while (!queue.isEmpty()) {
      Monkey tmon = queue.poll();
      if (tmon.r == N - 1 && tmon.c == M - 1) return tmon.cnt;

      if (tmon.h + 1 <= K) {
        for (int d = 0; d < 8; d++) {
          int nr = tmon.r + dhi[d];
          int nc = tmon.c + dhj[d];

          if (nr < 0 || nr >= N || nc < 0 || nc >= M || visited[nr][nc][tmon.h + 1]) continue;

          if (map[nr][nc] == 0) {
            queue.add(new Monkey(nr, nc, tmon.h + 1, tmon.cnt + 1));
            visited[nr][nc][tmon.h + 1] = true;
          }
        }
      }

      for (int d = 0; d < 4; d++) {
        int nr = tmon.r + di[d];
        int nc = tmon.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M || visited[nr][nc][tmon.h]) continue;

        if (map[nr][nc] == 0) {
          queue.add(new Monkey(nr, nc, tmon.h, tmon.cnt + 1));
          visited[nr][nc][tmon.h] = true;
        }
      }
    }

    return -1;
  }

  static class Monkey {
    int r; int c; int h; int cnt;

    public Monkey(int r, int c, int h, int cnt) {
      this.r = r;
      this.c = c;
      this.h = h;
      this.cnt = cnt;
    }
  }
}