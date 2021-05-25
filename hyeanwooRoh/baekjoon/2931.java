// 가스관
//1시간 56분

// 반례가 상당히 많아 조건을 설정하기가 매우 까다로웠음

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, M;
  static int[][] map;
  static boolean[][] visited;
  static Pipe Moscow, Zagreb;

  static int charToInt(char ch, int r, int c) {
    switch(ch) {
      case '.':
        return 0;
      case '1':
      case '2':
      case '3':
      case '4':
        return ch - '0';
      case '|':
        return 5;
      case '-':
        return 6;
      case '+':
        return 7;
      case 'M':
        Moscow = new Pipe(r, c);
        return 99;
      case 'Z':
        Zagreb = new Pipe(r, c);
        return 100;
    }
    return -1;
  }

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    map = new int[N][M];
    visited = new boolean[N][M];
    for (int i = 0; i < N; i++) {
      char[] input = br.readLine().toCharArray();
      for (int j = 0; j < M; j++) {
        map[i][j] = charToInt(input[j], i, j);
      }
    }

    br.close();
  }

  /*
  DR = 1
  UR = 2
  UL = 3
  DL = 4
  | -> 5
  - -> 6
  + -> 7
  */

  static int[][] pi = {{0}, {1,0}, {-1,0}, {-1,0}, {1,0}, {-1, 1}, {0,0}, {-1,0,1,0}};
  static int[][] pj = {{0}, {0,1}, {0,1}, {0,-1}, {0,-1}, {0, 0}, {-1,1}, {0,1,0,-1}};

  public static void solve() {
    Queue<Pipe> queue = new LinkedList<>();
    queue.add(Moscow);
    visited[Moscow.r][Moscow.c] = true;
    
    while (!queue.isEmpty()) {
      Pipe tp = queue.poll();
      // System.out.println("cur: "+tp);
      int curPipe = map[tp.r][tp.c];
      if (curPipe == 99 || curPipe == 100) {
        if (queue.isEmpty()) {
          for (int d = 0; d < 4; d++) {
            int nr = tp.r + pi[7][d];
            int nc = tp.c + pj[7][d];
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

            if (map[nr][nc] != 0 && map[nr][nc] < 10 && map[nr][nc] < 10) {
              queue.add(new Pipe(nr, nc));
              visited[nr][nc] = true;
              break;
            }
          }

          if (queue.isEmpty()) {
            Pipe tmpPipe = curPipe == 99 ? Zagreb : Moscow;
            queue.add(tmpPipe);
            visited[tmpPipe.r][tmpPipe.c] = true;
          }
        }
        continue;
      } else if (curPipe == 0) {
        printAnswer(tp);
        break;
      }

      for (int d = 0; d < pi[curPipe].length; d++) {
        int nr = tp.r + pi[curPipe][d];
        int nc = tp.c + pj[curPipe][d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M || visited[nr][nc]) continue;

        queue.add(new Pipe(nr, nc));
        visited[nr][nc] = true;
      }
      // System.out.println(queue);
    }
  }

  static void printAnswer(Pipe pipe) {
    int[] dir = new int[4];

    for (int d = 0; d < 4; d++) {
      int tr = pipe.r + pi[7][d];
      int tc = pipe.c + pj[7][d];

      if (tr < 0 || tr >= N || tc < 0 || tc >= M || map[tr][tc] == 0) continue;
      
      int tp = map[tr][tc];
      if (tp == 99 || tp == 100) { // M 또는 Z일경우
        int pipeCnt = 0;
        for (int d2 = 0; d2 < 4; d2++) {
          int nr = tr + pi[7][d2];
          int nc = tc + pj[7][d2];

          if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
          if (map[nr][nc] != 0 && map[nr][nc] < 10) pipeCnt++;
        }
        if (pipeCnt == 0) dir[d] = 1;
      } else {
        for (int d2 = 0; d2 < pi[tp].length; d2++) {
          int nr = tr + pi[tp][d2];
          int nc = tc + pj[tp][d2];

          if (nr == pipe.r && nc == pipe.c) {
            dir[d] = 1;
            break;
          }
        }
      }
    }

    String pipeName = "";
    if (dir[0] == 1 && dir[1] == 1 && dir[2] == 1 && dir[3] == 1) {
      pipeName = " +";
    } else if (dir[1] == 1 && dir[2] == 1) {
      pipeName = " 1";
    } else if (dir[0] == 1 && dir[1] == 1) {
      pipeName = " 2";
    } else if (dir[0] == 1 && dir[3] == 1) {
      pipeName = " 3";
    } else if (dir[2] == 1 && dir[3] == 1) {
      pipeName = " 4";
    } else if (dir[0] == 1 && dir[2] == 1) {
      pipeName = " |";
    } else if (dir[1] == 1 && dir[3] == 1) {
      pipeName = " -";
    } 

    System.out.println(pipe + pipeName);
  }

  static class Pipe {
    int r; int c;

    public Pipe(int r, int c) {
      this.r = r;
      this.c = c;
    }

    @Override
    public String toString() {
      return (this.r + 1) + " " + (this.c + 1);
    }
  }
}

// 6 6
// 1--M.Z
// 24..1.
// .|.13.
// .|.24.
// .|1-3.
// .23...

// 3 3
// MZ.
// |..
// 23.