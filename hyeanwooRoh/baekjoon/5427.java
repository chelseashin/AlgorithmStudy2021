// 불
// 1시간 12분

// 불과 사람처리 순서를 바꿔주니 풀림 

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine());
    for (int tc = 0; tc < T; tc++) {
      init(br);
      int res = solve();
      if (res == -1) sb.append("IMPOSSIBLE\n");
      else sb.append(res).append("\n");
    }
    br.close();
    
    System.out.println(sb.toString());
	}

  static int W, H;
  static char[][] map;

  public static void init(BufferedReader br) throws IOException {
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    W = Integer.parseInt(st.nextToken());
    H = Integer.parseInt(st.nextToken());

    map = new char[H][W];
    for (int i = 0; i < H; i++) {
      map[i] = br.readLine().toCharArray();
    }
  }

  static int[] di = {1,-1,0,0};
  static int[] dj = {0,0,1,-1};

  public static int solve() {
    Queue<Node> personQueue = new LinkedList<>();
    Queue<Node> fireQueue = new LinkedList<>();
    boolean[][] visited = new boolean[H][W];

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (map[i][j] == '*') fireQueue.add(new Node(i, j));
        else if (map[i][j] == '@') {
          personQueue.add(new Node(i, j));
          visited[i][j] = true;
        }
      }
    }

    while (!personQueue.isEmpty()) {
      int size = fireQueue.size();
      for (int i = 0; i < size; i++) {        
        Node fNode = fireQueue.poll();
        
        for (int d = 0; d < 4; d++) {
          int nr = fNode.r + di[d];
          int nc = fNode.c + dj[d];

          if (nr < 0 || nr >= H || nc < 0 || nc >= W || map[nr][nc] == '*' || map[nr][nc] == '#') continue;

          map[nr][nc] = '*';
          fireQueue.add(new Node(nr, nc));
        }
      }

      size = personQueue.size();
      for (int i = 0; i < size; i++) {        
        Node pNode = personQueue.poll();

        for (int d = 0; d < 4; d++) {
          int nr = pNode.r + di[d];
          int nc = pNode.c + dj[d];

          if (nr < 0 || nr >= H || nc < 0 || nc >= W) return pNode.t + 1;
          else if (visited[nr][nc] || map[nr][nc] == '*' || map[nr][nc] == '#') continue;

          personQueue.add(new Node(nr, nc, pNode.t + 1));
          visited[nr][nc] = true;
        }
      }
    }

    return -1;
  }

  static class Node {
    int r; int c; int t;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
      this.t = 0;
    }
    
    public Node(int r, int c, int t) {
      this.r = r;
      this.c = c;
      this.t = t;
    }
  }
}