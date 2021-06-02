// 다리만들기
// 53분

// 마찬가지로 아이디어가 중요했던 문제
// 섬을 넘버링 해준다음 확장해가며 거리를 구해주었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N;
  static int[][] map;
  static boolean[][] visited;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    
    N = Integer.parseInt(br.readLine());
    map = new int[N][N];
    visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        map[i][j] = Integer.parseInt(st.nextToken()) * (-1);
      }
    }

    br.close();
  }

  public static void solve() {
    int landNum = 1;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (map[i][j] == -1 && !visited[i][j]) {
          paintLand(landNum, i, j);
          landNum++;
        }
      }
    }

    int minLen = Integer.MAX_VALUE;
    for (int k = 1; k < landNum; k++) {
      visited = new boolean[N][N];
      minLen = Math.min(minLen, buildBridge(k));
    }

    System.out.println(minLen);
  }

  static int[] di = {0,1,0,-1};
  static int[] dj = {1,0,-1,0};

  static void paintLand(int landNum, int r, int c) {
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(r, c));
    map[r][c] = landNum;
    visited[r][c] = true;

    while(!queue.isEmpty()) {
      Node tnode = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = tnode.r + di[d];
        int nc = tnode.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

        if (map[nr][nc] == -1 && !visited[nr][nc]) {
          queue.add(new Node(nr, nc));
          map[nr][nc] = landNum;
          visited[nr][nc] = true;
        }
      }
    }
  }

  static int buildBridge(int landNum) {
    Queue<Node> queue = new LinkedList<>();

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (map[i][j] == landNum){
          queue.add(new Node(i, j));
          visited[i][j] = true;
        }
      }
    }

    int bridgeLen = 0;
    while (!queue.isEmpty()) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        Node tnode = queue.poll();

        for (int d = 0; d < 4; d++) {
          int nr = tnode.r + di[d];
          int nc = tnode.c + dj[d];

          if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc] || map[nr][nc] == landNum) continue;
          
          if (map[nr][nc] != 0 && map[nr][nc] != landNum) {
            return bridgeLen;
          } else {
            queue.add(new Node(nr, nc));
            visited[nr][nc] = true;
          }
        }
      }
      bridgeLen++;
    }

    return -1;
  }

  static void print() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(map[i][j]+" ");
      }
      System.out.println();
    }
    System.out.println();
  }

  static class Node {
    int r; int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}