// 마법사 상어와 블리자드
// 1시간 40분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(score);
	}

  static int N, M, score;
  static int[] marbles;
  static int[][] board, command;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    score = 0;

    marbles = new int[N*N];
    board = new int[N][N];
    command = new int[M][2];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      command[i][0] = Integer.parseInt(st.nextToken()) - 1;
      command[i][1] = Integer.parseInt(st.nextToken());
    }
    br.close();
  }

  public static void solve() {
      printBoard();
      printMarble();
    for (int[] cmd : command) {
      castBlizzard(cmd[0], cmd[1]);
      breakMarble();
      multiplyMarble();
        printBoard();
        printMarble();
    }
  }

  // 입력받은 방향 순서
  static int[] di = {-1,1,0,0};
  static int[] dj = {0,0,-1,1};

  static void castBlizzard(int d, int s) {
    int r = N / 2;
    int c = N / 2;
    for (int i = 0; i < s; i++) {
      r += di[d];
      c += dj[d];
      board[r][c] = 0; 
    }
    normalizeBoard();
  }

  static void breakMarble() {
    int serialCnt = 0;
    int mNum = marbles[1];
    for (int i = 1; i < marbles.length; i++) {
      if (marbles[i] == 0) continue;

      if (marbles[i] == mNum) {
        serialCnt++;
      } else {
        if (serialCnt > 3) {
          score += mNum * serialCnt;
          int tmpIdx = 1;
          while (serialCnt > 0) {
            if (marbles[i-tmpIdx] == 0) {
              tmpIdx++;
              continue;
            }
            marbles[i-tmpIdx] = 0;
            tmpIdx++;
            serialCnt--;
          }
          i = 1;
        }
        mNum = marbles[i];
        serialCnt = 1;
      }
    }
  }

  static void multiplyMarble() {
    int marbleA = 0;
    int marbleB = 0;

    for (int i = 1; i < marbles.length; i++) {
      if (marbles[i] != 0) {
        marbleA = 0;
        marbleB = marbles[i];
        break;
      }
    }

    int ti = 1;
    int[] tmpMarbles = new int[N*N];
    for (int i = 1; i < marbles.length; i++) {
      if (marbles[i] == 0) continue;
      if (ti >= marbles.length) break;

      if (marbleB == marbles[i]) {
        marbleA++;
      } else {
        tmpMarbles[ti++] = marbleA;
        tmpMarbles[ti++] = marbleB;
        marbleA = 1;
        marbleB = marbles[i];
      }
    }

    if (ti < marbles.length) {
      tmpMarbles[ti++] = marbleA;
      tmpMarbles[ti++] = marbleB;
    }

    marbles = new int[N*N];
    for (int i = 1; i < marbles.length; i++) {
      marbles[i] = tmpMarbles[i];
    }

    denormalizeBoard();
  }

  // 배열 탐색 방향 순서
  static int[] dr = {0,1,0,-1};
  static int[] dc = {-1,0,1,0};

  static void normalizeBoard() {
    marbles = new int[N*N];
    int r = N/2;
    int c = N/2;
    int d = 0;
    int idx = 1;
    for (int i = 0; i < N - 1; i++) {
      for (int j = 0; j < 2; j++) {
        for (int k = 0; k <= i; k++) {
          r += dr[d];
          c += dc[d];
          if (board[r][c] == 0) continue;
          marbles[idx++] = board[r][c];
        }
        d = (d + 1) % 4;
      }
    }

    for (int i = 0; i < N - 1; i++) {
      r += dr[d];
      c += dc[d];
      if (board[r][c] == 0) continue;
      marbles[idx++] = board[r][c];
    }
  }

  static void denormalizeBoard() {
    board = new int[N][N];
    int r = N/2;
    int c = N/2;
    int d = 0;
    int idx = 1;
    for (int i = 0; i < N - 1; i++) {
      for (int j = 0; j < 2; j++) {
        for (int k = 0; k <= i; k++) {
          r += dr[d];
          c += dc[d];

          while (idx < marbles.length && marbles[idx] == 0) idx++;
          if (idx == marbles.length) return;
          board[r][c] = marbles[idx++];
        }
        d = (d + 1) % 4;
      }
    }

    for (int i = 0; i < N - 1; i++) {
      r += dr[d];
      c += dc[d];

      while (idx < marbles.length && marbles[idx] == 0) idx++;
      if (idx == marbles.length) return;
      board[r][c] = marbles[idx++];
    }
  }

  static void printBoard() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(board[i][j] + " ");
      }
      System.out.println();
    }
    System.out.println();
  }

  static void printMarble(){
    for (int i = 0; i < marbles.length; i++) {
      System.out.print(marbles[i] + " ");
    }
    System.out.println();
    System.out.println();
  }
}