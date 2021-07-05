// 로봇 청소기
// 33분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(robot.cnt);
	}

  static int N, M;
  static int[][] map;
  static Cleaner robot;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
  
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    int r = Integer.parseInt(st.nextToken());
    int c = Integer.parseInt(st.nextToken());
    int d = Integer.parseInt(st.nextToken());
    robot = new Cleaner(r, c, d);

    map = new int[N][M];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    br.close();
  }

  static int[] di = {-1,0,1,0};
  static int[] dj = {0,1,0,-1};

  public static void solve() {
    boolean[][] visited = new boolean[N][M];
    
    while (true) {
      int cr = robot.r;
      int cc = robot.c;

      // 1. clean
      map[cr][cc] = 0;
      if (!visited[cr][cc]) robot.cnt++;
      visited[cr][cc] = true;

      // 2. left search
      int flag = 0;
      for (int d = 0; d < 4; d++) {
        int nd = (robot.d + 3 ) % 4;
        int nr = cr + di[nd];
        int nc = cc + dj[nd];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M || visited[nr][nc] || map[nr][nc] == 1) {
          robot.d = nd;
          flag++;
          continue;
        }

        if (map[nr][nc] == 0) {
          robot.r = nr;
          robot.c = nc;
          robot.d = nd;
          break;
        }

      }
        if (flag == 4) {
          int bd = (robot.d + 2) % 4;
          int br = cr + di[bd];
          int bc = cc + dj[bd];
          
          if (br < 0 || br >= N || bc < 0 || bc >= M || map[br][bc] == 1) return;
          else {
            robot.r = br;
            robot.c = bc;
          }
        }

    }
  }
  
  static class Cleaner {
    int r; int c; int d; int cnt;

    public Cleaner(int r, int c, int d) {
      this.r = r;
      this.c = c;
      this.d = d;
      this.cnt = 0;
    }
  }
}