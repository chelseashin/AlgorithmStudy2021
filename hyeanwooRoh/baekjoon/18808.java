// 스티커 붙이기
// 1시간 40분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(count);
	}

  static int N, M, count;
  static int[][] laptop;
  static ArrayList<int[][]> stickers = new ArrayList<>();

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    laptop = new int[N][M];
    for (int k = 0; k < K; k++) {
      st = new StringTokenizer(br.readLine());
      int tr = Integer.parseInt(st.nextToken());
      int tc = Integer.parseInt(st.nextToken());
      
      int[][] sticker = new int[tr][tc];
      for (int i = 0; i < tr; i++) {
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < tc; j++) {
          sticker[i][j] = Integer.parseInt(st.nextToken());
        }
      }
      stickers.add(sticker);
    }

    br.close();
  }

  public static void solve() {
    for (int[][] sticker : stickers) {
      checkSticker(sticker, 0);
    }
    calcCount();
  }

  static void checkSticker(int[][] sticker, int rotateIdx) {
    if (rotateIdx == 4) return;

    boolean canAttach = false;
    int ar = -1, ac = -1;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if (isAttachable(sticker, rotateIdx, i, j)) {
          canAttach = true;
          ar = i;
          ac = j;
          break;
        }
      }
      if (canAttach) break;
    }

    if (!canAttach) {
      checkSticker(sticker, rotateIdx + 1);
    } else {
      attachSticker(sticker, rotateIdx, ar, ac);
    }
  }

  static boolean isAttachable(int[][] sticker, int rotateIdx, int r, int c) {
    int nr = r;
    int nc = c;
    int row = sticker.length;
    int col = sticker[0].length;

    switch(rotateIdx) {
      case 0:
        if (c + col > M || r + row > N) return false;

        for (int i = 0; i < row; i++) {
          for (int j = 0; j < col; j++) {
            if (sticker[i][j] == 1 && laptop[nr][nc] != 0) return false;
            
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 1:
        if (c + row > M || r + col > N) return false;

        for (int j = 0; j < col; j++) {
          for (int i = row - 1; i >= 0; i--) {
            if (sticker[i][j] == 1 && laptop[nr][nc] != 0) return false;
            
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 2:
        if (c + col > M || r + row > N) return false;

        for (int i = row - 1; i >= 0; i--) {
          for (int j = col - 1; j >= 0; j--) {
            if (sticker[i][j] == 1 && laptop[nr][nc] != 0) return false;
            
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 3:
        if (c + row > M || r + col > N) return false;

        for (int j = col - 1; j >= 0; j--) {
          for (int i = 0; i < row; i++) {
            if (sticker[i][j] == 1 && laptop[nr][nc] != 0) return false;
            
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
    }

    return true;
  }

  static void attachSticker(int[][] sticker, int rotateIdx, int r, int c) {
    int nr = r;
    int nc = c;
    int row = sticker.length;
    int col = sticker[0].length;

    switch(rotateIdx) {
      case 0:
        for (int i = 0; i < row; i++) {
          for (int j = 0; j < col; j++) {
            laptop[nr][nc] += sticker[i][j];
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 1:
        for (int j = 0; j < col; j++) {
          for (int i = row-1; i >= 0; i--) {
            laptop[nr][nc] += sticker[i][j];
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 2:
        for (int i = row - 1; i >= 0; i--) {
          for (int j = col - 1; j >= 0; j--) {
            laptop[nr][nc] += sticker[i][j];
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
      case 3:
        for (int j = col - 1; j >= 0; j--) {
          for (int i = 0; i < row; i++) {
            laptop[nr][nc] += sticker[i][j];
            nc++;
          }
          nr++;
          nc = c;
        }
        break;
    }
  }

  static void calcCount() {
    count = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        count += laptop[i][j];
      }
    }
  }

  static void print() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        System.out.print(laptop[i][j]+" ");
      }
      System.out.println();
    }
    System.out.println();
  }
}