import java.io.*;
import java.util.*;

// 1시간 20분째 고민중

public class MyClass {
	public static void main(String[] args) throws Exception {
		init();
		solve();
    submit();
	}

	static BufferedReader br;
	static StringTokenizer st;
  static int N, M, virusCnt, answer;
  static int[][] lab;
  static ArrayList<Node> virusPoints;

	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
    st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    virusCnt = 0;
    answer = -1;
    lab = new int[N][N];
    virusPoints = new ArrayList<>();

    for(int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for(int j = 0; j < N; j++) {
        int v = Integer.parseInt(st.nextToken());
        if(v == 2) {
          lab[i][j] = -2;
          virusCnt++;
          virusPoints.add(new Node(i, j));
        } else if(v == 1) {
          lab[i][j] = -1;
        }
      }
    }

		br.close();
	}

	static void solve() throws IOException {
    if(isLabFull(lab)) {
      answer = 0;
      return;
    }
    
    boolean[] visit = new boolean[virusCnt];
    comb(visit, 0, 0);
	}

  static boolean isLabFull(int[][] map) {
    for(int i=0; i < N; i++) {
      for(int j=0; j < N; j++) {
        answer = Math.max(answer, map[i][j]);
        if(map[i][j] == 0) return false;
      }
    }

    return true;
  }

  static void comb(boolean[] visit, int depth, int idx) {
    if(depth == M) {
      spreadVirus(visit);
      return;
    }

    for(int i = idx; i < virusCnt; i++) {
      visit[i] = true;
      comb(visit, depth+1, i+1);
      visit[i] = false;
    }
  }

  static int[] di = {0,0,1,-1};
  static int[] dj = {1,-1,0,0};
  static void spreadVirus(boolean[] visit) {
    int[][] map = new int[N][N];
    deepCopy(map);

    Queue<Node> queue = new LinkedList<>();
    for(int i=0; i < visit.length; i++) {
      if(visit[i]) {
        queue.add(virusPoints.get(i));
      }
    }

    while(!queue.isEmpty()) {
      Node tmp = queue.poll();

      for(int d=0; d < 4; d++) {
        int ti = tmp.r + di[d];
        int tj = tmp.c + dj[d];

        if(ti < N && ti >= 0 && tj < N && tj >= 0) {
          if(map[ti][tj] == 0) {
            map[ti][tj] = tmp.sec + 1;
            queue.add(new Node(ti, tj, tmp.sec + 1));
          } else if(map[ti][tj] == -1) {
            // map[ti][tj] = tmp.sec + 1;
            // queue.add(new Node(ti, tj, tmp.sec + 1));
          } else {
            if(map[ti][tj] > tmp.sec + 1) {
              map[ti][tj] = tmp.sec + 1;
              queue.add(new Node(ti, tj, tmp.sec + 1));
            }
          }
        }
      }
    }

    isLabFull(map);
  }

  static void deepCopy(int[][] map) {
    for(int i=0; i < N; i++) {
      for(int j=0; j < N; j++) {
        map[i][j] = lab[i][j];
      }
    }
  }

  static class Node {
    int r;
    int c;
    int sec;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
      this.sec = 0;
    }
    
    public Node(int r, int c, int sec) {
      this.r = r;
      this.c = c;
      this.sec = sec;
    }

    @Override
    public String toString() {
      return String.format("(%d,%d)", this.r, this.c);
    }
  }

  static void submit() {
    System.out.println(answer);
  }
}
