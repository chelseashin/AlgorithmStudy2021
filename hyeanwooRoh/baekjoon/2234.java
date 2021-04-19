// 성곽
// 39분

// 비트마스크 부분을 활용해서 4방향배열로 변환해 사용

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, M;
  static int[][][] wall;
  static boolean[][] visited;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    M = Integer.parseInt(st.nextToken());
    N = Integer.parseInt(st.nextToken());

    wall = new int[N][M][4];
    visited = new boolean[N][M];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        int bitSum = Integer.parseInt(st.nextToken());
        for (int k = 0; k < 4; k++) {
          if ((bitSum & 1 << k) > 0) wall[i][j][k] = 1;
        }
      }
    }

    br.close();
  }

  static int[] di = {0, -1, 0, 1};
  static int[] dj = {-1, 0, 1, 0};

  private static void solve() {
    // 1. find room cnt && 2. max room area
    int roomCnt = 0;
    int maxArea = 0;
    for (int i = 0; i < N; i++) {
      int area = 0;
      for (int j = 0; j < M; j++) {
        if (!visited[i][j]) {
          maxArea = Math.max(maxArea, bfs(i, j));
          roomCnt++;
        }
      }
    }
    
    // 3. find combined room area
    int combineRoomArea = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        for (int d = 0; d < 4; d++) {
          if (wall[i][j][d] == 1) {
            int nr = i + di[d];
            int nc = j + dj[d];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

            wall[i][j][d] = 0;
            visited = new boolean[N][M];
            combineRoomArea = Math.max(combineRoomArea, bfs(i, j));
            wall[i][j][d] = 1;
          }
        }
      }
    }

    System.out.println(String.format("%d\n%d\n%d", roomCnt, maxArea, combineRoomArea));
  }

  public static int bfs(int row, int col) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(row, col));
    visited[row][col] = true;

    int area = 1;
    while (!queue.isEmpty()) {
      Node tnode = queue.poll();
      int tr = tnode.r;
      int tc = tnode.c;

      for (int d = 0; d < 4; d++) {
        if (wall[tr][tc][d] == 1) continue;

        int nr = tr + di[d];
        int nc = tc + dj[d];
        if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

        if (!visited[nr][nc]) {
          queue.add(new Node(nr, nc));
          visited[nr][nc] = true;
          area++;
        }
      }
    }

    return area;
  }

  public static class Node {
    int r; int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }

}