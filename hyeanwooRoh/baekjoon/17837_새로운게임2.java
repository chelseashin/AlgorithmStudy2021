import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 50분 + 50분

public class notyet_17937 {
  public static void main(String[] args) throws Exception {
    init();
    solve();
    out();
  }

  static BufferedReader br;
  static StringTokenizer st;
  static int N, K, turnCnt;
  static int[][] board;
  static Piece[] pieces;
  static ArrayList<Integer>[][] boardList;
  
  static void init() throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());
    turnCnt = 0;
    
    board = new int[N][N];
    for(int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for(int j = 0; j < N; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    boardList = new ArrayList[N][N];
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        boardList[i][j] = new ArrayList<>();
      }
    }
    
    pieces = new Piece[K];
    for (int i = 0; i < K; i++) {
      st = new StringTokenizer(br.readLine());
      pieces[i] = new Piece(Integer.parseInt(st.nextToken()) - 1,Integer.parseInt(st.nextToken()) - 1,Integer.parseInt(st.nextToken()) - 1, i);
      boardList[pieces[i].r][pieces[i].c].add(i);
    }

    br.close();
  }
  
  static void solve() {
    for (int t = 0; t < 1000; t++) {
      spreadOnBoard();
    }
    turnCnt = -1;
  }

  static void spreadOnBoard() {
    for(int i=0; i < K; i++) {
      Piece p = pieces[i];
      if(boardList[p.r][p.c].size() > 1) {
        // moveChild();
      } else {
        movePiece(p);
      }
    print();
    }
  }

  static final int WHITE = 0;
  static final int RED = 1;
  static final int BLUE = 2;

  static int[] di = {0,0,-1,1};
  static int[] dj = {1,-1,0,0};

  static void movePiece(Piece p) {
    int pi = p.r + di[p.d];
    int pj = p.c + dj[p.d];

    if(pi >= N || pi < 0 || pj >= N || pj < 0 || board[pi][pj] == BLUE) {
      p.d = (p.d%2 == 1) ? p.d - 1 : p.d + 1;
      pi = p.r + di[p.d];
      pj = p.c + dj[p.d];
      if(pi < N && pi >= 0 && pj < N && pj >= 0 && board[pi][pj] != BLUE) {
        handlePiece(pi, pj, p);        
      }
    } else if(board[pi][pj] == RED) {
      handlePiece(pi, pj, p);
    } else if(board[pi][pj] == WHITE) {
      handlePiece(pi, pj, p);
    }
  }

  static void handlePiece(int r, int c, Piece p) {
    boardList[p.r][p.c].remove(0);
    p.r = r;
    p.c = c;
    boardList[r][c].add(p.num);
  }

  static void print() {
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        if(boardList[i][j].size() == 0) {
          System.out.print(9+" ");
        } else {
          System.out.print(boardList[i][j].get(0)+" ");
        }
      }
      System.out.println();
    }
      System.out.println();
  }

  static class Piece {
    int r;
    int c;
    int d;
    int num;

    public Piece(int r, int c, int d, int num) {
      this.r = r;
      this.c = c;
      this.d = d;
      this.num = num;
    }

    @Override
    public String toString() {
      return String.format("(%d,%d,%d)", this.r, this.c, this.d);
    }
  }
  
  static void out() {
    System.out.println(turnCnt);
  }
}