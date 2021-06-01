// N-Queen
// 40분

// 백트래킹의 기본개념같은 문제이지만 시간이 너무 오래걸리고 답이 예측가능하다

import java.io.*;
import java.util.*;

public class Main {
  // public static void main(String[] args) throws IOException {
  //   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  //   int N = Integer.parseInt(br.readLine());
  //   br.close();

  //   int[] answer = {0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596}
  //   System.out.println(answer[N]); 
	// }

	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    br.close();
    
    count = 0;
    board = new int[N];
    
    backtracking(0);

    System.out.println(count);
	}

  static int N, count;
  static int[] board;

  static void backtracking(int depth) {
    if (depth == N) {
      count++;
      return;
    }

    for (int i = 0; i < N; i++) {
      board[depth] = i;

      if (isSafe(depth)) {
        backtracking(depth + 1);
      }
    }
  }

  static boolean isSafe(int col) {
    for (int i = 0; i < col; i++) {
      if (board[col] == board[i]) return false;
      if (Math.abs(col - i) == Math.abs(board[col] - board[i])) return false;
    }
    return true;
  }

}