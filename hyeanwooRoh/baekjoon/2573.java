// 빙산
// 46분

// 구현 + bfs

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(year);
	}

  static int N, M, year = 0;
  static int[][] sea;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    sea = new int[N][M];

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        sea[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    br.close();
  }

  public static void solve() {
    int[][] tmp;

    while (true) {
      year++;

      tmp = new int[N][M];
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (sea[i][j] != 0) tmp[i][j] = checkAround(i, j);
        }
      }
      
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (tmp[i][j] != 0) {
            sea[i][j] -= tmp[i][j];
            if (sea[i][j] < 0) sea[i][j] = 0;
          }
        }
      }

      int chunks = checkChunk();
      if (chunks > 1) {
        break;
      } else if (chunks == 0) {
        year = 0;
        break;
      }
    }
  }

  static int[] di = {0, 0, 1, -1};
  static int[] dj = {1, -1, 0, 0};
  
  static int checkAround(int r, int c) {
    int aroundCnt = 0;
    for (int d = 0; d < 4; d++) {
      int nr = r + di[d];
      int nc = c + dj[d];

      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
      if (sea[nr][nc] == 0) aroundCnt++;
    }
    return aroundCnt;
  }

  static int checkChunk() {
    boolean[][] visited = new boolean[N][M];
    int chunks = 0;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (sea[i][j] != 0 && !visited[i][j]) {
          findChunk(visited, i, j);
          chunks++;
        }
      }
    }

    return chunks;
  }

  static void findChunk(boolean[][] visited, int r, int c) {
    Queue<IceBerg> queue = new LinkedList<>();
    queue.add(new IceBerg(r, c));
    visited[r][c] = true;

    while (!queue.isEmpty()) {
      IceBerg tIce = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = tIce.r + di[d];
        int nc = tIce.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M || visited[nr][nc]) continue;
        if (sea[nr][nc] != 0) {
          queue.add(new IceBerg(nr, nc));
          visited[nr][nc] = true;
        }
      }
    }
  }

  static class IceBerg {
    int r; int c;

    public IceBerg(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }

  static void print() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        System.out.print(sea[i][j]+" ");
      }
      System.out.println();
    }
    System.out.println();
  }
}