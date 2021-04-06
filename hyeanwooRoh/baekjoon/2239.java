// 스도쿠
// 2시간 34분

// 스택으로 풀어보려다 재귀로 해도 안터진다는 말에 1시간15분동안 하던거 날리고 다시 시작
// 2시간 22분쯤에 조건 빼먹은걸 발견해서 수정

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    // System.out.println();
	}

  static int[][] board = new int[9][9];

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    for (int i = 0; i < 9; i++) {
      String input = br.readLine();
      for (int j = 0; j < 9; j++) {
        board[i][j] = input.charAt(j) - '0';
      }
    }
    br.close();
  }

  static boolean isPrinted = false;

  private static void solve() {
    // print();
    backtracking(0,0);
  }

  private static void backtracking(int r, int c) {
    if (isPrinted) return;

    if (r == 8 && c == 8) {
      printAnswer();
      isPrinted = true;
      return;
    }

    int nr = c == 8 ? r + 1 : r;
    int nc = (c + 1) % 9;
    if (board[r][c] != 0) {
      backtracking(nr, nc);
    } else {
      for (int i = 1; i < 10; i++) {
        if (isSdokuNum(r, c, i)) {
          // 괜찮은 숫자면 board처리
          board[r][c] = i;
          // 다음 요소로
          backtracking(nr,nc);
          // board에서 빼주고 다음숫자로
          board[r][c] = 0;
        }
      }
    }

  }

  private static boolean isSdokuNum(int r, int c, int num) {
    boolean flag = true;

    for (int k = 0; k < 9; k++) {
      if (board[r][k] == num || board[k][c] == num) {
        flag = false;
        break;
      }
    }

    int tr = r - (r % 3);
    int tc = c - (c % 3);
    for (int i = tr; i < tr + 3; i++) {
      for (int j = tc; j < tc + 3; j++) {
        if (board[i][j] == num) {
          flag = false;
          break;
        }
      }
    }

    return flag;
  }

  static void print() {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        System.out.print(board[i][j] + " ");
      }
      System.out.println();
    }
    System.out.println();
  }
  
  static void printAnswer() {
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        System.out.print(board[i][j]);
      }
      System.out.println();
    }
  }

}
