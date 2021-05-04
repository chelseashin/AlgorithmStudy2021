// 상어 중학교
// 2시간 43분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(score);
	}

  static final int EMPTY = 9;
  static final int BLACK = -1;
  static final int RBW = 0;
  static int N, M, score;
  static int[][] board;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken()); // 격자 크기
    M = Integer.parseInt(st.nextToken()); // 색상 수
    score = 0;

    board = new int[N][N];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    br.close();
  }

  public static void solve() {
    boolean flag = true;
    while (flag) {
      flag = autoplay();
    }
  }

  static boolean autoplay() {
    ArrayList<Block> groupList = new ArrayList<>();
    findBlockGroup(groupList);

    Block maxBlock = new Block(-1,-1);
    for (Block block : groupList) {
      if (block.size > maxBlock.size) {
        maxBlock = block;
      } else if (block.size == maxBlock.size) {
        if (block.rCnt > maxBlock.rCnt) {
          maxBlock = block;
        } else if (block.rCnt == maxBlock.rCnt) {
          if (block.r > maxBlock.r || (block.r == maxBlock.r && block.c > maxBlock.c)) {
            maxBlock = block;
          }
        }
      }
    }

    if (maxBlock.size > 1) {
      removeBlockGroup(maxBlock);
      score += Math.pow(maxBlock.size, 2);
    } else {
      return false;
    }
    
    applyGravity();
    rotateBoard();
    applyGravity();

    return true;
  }

  static void rotateBoard() {
    int[][] tmpBoard = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        tmpBoard[N-1-j][i] = board[i][j];
      }
    }
    
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        board[i][j] = tmpBoard[i][j];
      }
    }
  }

  static void applyGravity() {
    for (int j = 0; j < N; j++) {
      int emptyCnt = 0;
      for (int i = N - 1; i >= 0; i--) {
        if (board[i][j] == EMPTY) {
          emptyCnt++;
        } else if (board[i][j] == BLACK) {
          emptyCnt = 0;
        } else {
          if (emptyCnt != 0) {
            board[i+emptyCnt][j] = board[i][j];
            board[i][j] = EMPTY;
          }
        }
      }
    }
  }

  static void findBlockGroup(ArrayList<Block> groupList) {
    boolean[][] visited = new boolean[N][N];
    // calc each group size
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j] == BLACK || board[i][j] == RBW || board[i][j] == EMPTY || visited[i][j]) continue;    
        
        int[] groupInfo = getBlockGroup(visited, i, j);
        initRainbowBlock(visited);
        groupList.add(new Block(i, j, groupInfo[0], groupInfo[1]));
      }
    }
  }

  static int[] di = {1, 0, -1, 0};
  static int[] dj = {0, -1, 0, 1};

  static int[] getBlockGroup(boolean[][] visited, int r, int c) {
    Queue<Block> queue = new LinkedList<>();
    queue.add(new Block(r, c));
    visited[r][c] = true;
    
    int COLOR = board[r][c];
    int[] info = new int[2];
    info[0] = 1;

    while (!queue.isEmpty()) {
      Block tmpB = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = tmpB.r + di[d];
        int nc = tmpB.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;

        if (board[nr][nc] == RBW || board[nr][nc] == COLOR) {
          if (board[nr][nc] == RBW) info[1]++;
          queue.add(new Block(nr, nc));
          info[0]++;
          visited[nr][nc] = true;
        }
      }
    }

    return info;
  }

  static void removeBlockGroup(Block block) {
    Queue<Block> queue = new LinkedList<>();
    boolean[][] visited = new boolean[N][N];
    queue.add(block);
    visited[block.r][block.c] = true;
    
    int COLOR = board[block.r][block.c];
    board[block.r][block.c] = EMPTY;
    

    while (!queue.isEmpty()) {
      Block tmpB = queue.poll();

      for (int d = 0; d < 4; d++) {
        int nr = tmpB.r + di[d];
        int nc = tmpB.c + dj[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= N || visited[nr][nc]) continue;

        if (board[nr][nc] == RBW || board[nr][nc] == COLOR) {
          queue.add(new Block(nr, nc));
          visited[nr][nc] = true;
          board[nr][nc] = EMPTY;
        }
      }
    }
  }

  static void initRainbowBlock(boolean[][] visited) {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j] == RBW) visited[i][j] = false;
      }
    }
  }

  static class Block {
    int r;
    int c;
    int size;
    int rCnt;

    public Block(int r, int c) {
      this.r = r;
      this.c = c;
      this.size = 0;
      this.rCnt = 0;
    }
    
    public Block(int r, int c, int s, int rbw) {
      this.r = r;
      this.c = c;
      this.size = s;
      this.rCnt = rbw;
    }

    @Override
    public String toString() {
      return "("+this.r+","+this.c+"):"+this.size+"|"+this.rCnt;
    }
  }

  static void printBoard() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j] == BLACK) {
          System.out.print("X ");
        } else if (board[i][j] == EMPTY) {
          System.out.print("0 ");
        } else if (board[i][j] == RBW) {
          System.out.print("7 ");
        } else {
          System.out.print(board[i][j]+" ");
        }
      }
      System.out.println();
    }
    System.out.println();
  }
}