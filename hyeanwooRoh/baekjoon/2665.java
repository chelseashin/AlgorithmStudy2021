// 미로만들기
// 25분

// 방문체크를 하는 visit배열에 boolean값 대신 숫자를 넣어 검은방을 카운트했다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N;
  static int[][] map;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    map = new int[N][N];
    for (int i = 0; i < N; i++) {
      char[] tmp = br.readLine().toCharArray();
      for (int j = 0; j < N; j++) {
        map[i][j] = tmp[j] - '0';
      }
    }

    br.close();
  }

  public static void solve() {
    int[] di = {0,0,1,-1};
    int[] dj = {1,-1,0,0};

    int[][] visited = new int[N][N];
    initVisited(visited);

    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(0,0));
    visited[0][0] = 0;

    while (!queue.isEmpty()) {
      Node node = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = node.r + di[d];
        int nc = node.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        
        if (map[nr][nc] == 0) {
          if (visited[nr][nc] > visited[node.r][node.c] + 1) {
            queue.add(new Node(nr, nc));
            visited[nr][nc] = visited[node.r][node.c] + 1;
          }
        } else {
          if (visited[nr][nc] > visited[node.r][node.c]) {
            queue.add(new Node(nr, nc));
            visited[nr][nc] = visited[node.r][node.c];
          }
        }
      }
    }
    System.out.println(visited[N-1][N-1]);
  }

  static void initVisited(int[][] array) {
    for (int i = 0; i < array.length; i++) {
      for (int j = 0; j < array[0].length; j++) {
        array[i][j] = Integer.MAX_VALUE;
      }
    }
  }

  static class Node {
    int r; int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }

  }
}