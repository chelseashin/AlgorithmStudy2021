// 미네랄
// 1시간 42분

// 미네랄을 부숴주고 바닥부터 전수조사해서 클러스터를 체크했는데
// 풀고나서 생각해보니 부셔진것 주위를 탐색하는건 어떨까 싶었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(sb.toString());
	}

  static int R, C;
  static int[][] cave;
  static int[] commands;
  static boolean isLeft = true;
  static StringBuilder sb;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    sb = new StringBuilder();

    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    cave = new int[R][C];
    for (int i = 0; i < R; i++) {
      char[] input = br.readLine().toCharArray();
      for (int j = 0; j < C; j++) {
        if (input[j] == '.') {
          cave[i][j] = 1;
        } else {
          cave[i][j] = 0;
        }
      }
    }

    int N = Integer.parseInt(br.readLine());
    st = new StringTokenizer(br.readLine());
    commands = new int[N];
    for (int i = 0; i < N; i++) {
      commands[i] = Integer.parseInt(st.nextToken());
    }

    br.close();
  }

  private static void solve() {
    for (int c = 0; c < commands.length; c++) {
      throwStick(R - commands[c]);
      pullDownFloatingMinerals();
    }
    convertCave();
  }

  private static void throwStick(int r) {
    if (isLeft) {
      isLeft = false;
      for (int j = 0; j < C; j++) {
        if (cave[r][j] == 0){
          cave[r][j] = 1;
          return;
        }
      }
    } else {
      isLeft = true;
      for (int j = C - 1; j >= 0; j--) {
        if (cave[r][j] == 0){
          cave[r][j] = 1;
          return;
        }
      }
    }
  }

  private static void pullDownFloatingMinerals() {
    boolean[][] visited = new boolean[R][C];
    for (int j = C - 1; j >= 0; j--) {
      if (cave[R - 1][j] == 0) {
        checkGroundMineral(visited, R - 1, j);
      }
    }
    pullDownCluster(visited);
  }

  static int[] di = {0, -1, 0, 1};
  static int[] dj = {-1, 0, 1, 0};

  public static void checkGroundMineral(boolean[][] visited, int row, int col) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(row, col));
    visited[row][col] = true;

    while (!queue.isEmpty()) {
      Node tnode = queue.poll();
      int tr = tnode.r;
      int tc = tnode.c;

      for (int d = 0; d < 4; d++) {
        int nr = tr + di[d];
        int nc = tc + dj[d];
        if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

        if (cave[nr][nc] == 0 && !visited[nr][nc]) {
          queue.add(new Node(nr, nc));
          visited[nr][nc] = true;
        }
      }
    }
  }

  public static void pullDownCluster(boolean[][] visited) {
    int len = R;
    for (int i = R - 2; i >= 0; i--) {
      for (int j = C - 1; j >= 0; j--) {
        if (cave[i][j] == 0 && !visited[i][j]) {
          len = Math.min(len, measureLen(visited, i, j));
        }
      }
    }

    for (int i = R - 2; i >= 0; i--) {
      for (int j = C - 1; j >= 0; j--) {
        if (cave[i][j] == 0 && !visited[i][j]) {
          cave[i+len][j] = 0;
          cave[i][j] = 1;
        }
      }
    }
  }

  public static int measureLen(boolean[][] visited, int r, int c) {
    int tmpLen = 0;
    for (int i = r + 1; i < R; i++) {
      if (cave[i][c] == 0) {
        if (!visited[i][c]) {
          return R;
        } else {
          return tmpLen;
        }
      } else {
        tmpLen++;
      }
    }

    return tmpLen;
  }

  public static void convertCave() {
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        char part = cave[i][j] == 1 ? '.' : 'x';
        sb.append(part);
      }
      sb.append("\n");
    }
  }

  public static class Node {
    int r; int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}