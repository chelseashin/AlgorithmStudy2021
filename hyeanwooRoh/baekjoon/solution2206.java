// 벽 부수고 이동하기

// 2시간 37분

// 2시간쯤에 반례찾다가 풀이 힌트 참고
// 링크: https://www.acmicpc.net/board/view/27386
// 한달전에 풀었던 체스판여행1과 유사한 문제였고 그때 풀이방법도 기억하고 있었지만
// 방문 배열의 마지막 항목을 뭘로 구성해야되는지 찾지못하고 힌트를 보고 알게됨

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(minDist);
	}

  static int N, M, minDist;
  static boolean isOnlyZero;
  static int[][] map;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    minDist = Integer.MAX_VALUE;
    isOnlyZero = true;

    map = new int[N][M];
    String[] str;
    for (int i = 0; i < N; i++) {
      str = br.readLine().split("");
      for (int j = 0; j < M; j++) {
        map[i][j] = Integer.parseInt(str[j]);
        if (map[i][j] == 1) isOnlyZero = false;
      }
    }

    br.close();
  }

  static int[] di = {0,1,0,-1};
  static int[] dj = {1,0,-1,0};

	private static void solve() {
    if (isOnlyZero) {
      minDist = N + M - 1;
      return;
    }

    bfs();

    if (minDist == Integer.MAX_VALUE) minDist = -1;
	}

  private static void bfs() {
    Queue<Node> q = new LinkedList<>();
    boolean[][][] visit = new boolean[N][M][2];
    
    q.add(new Node(0, 0, 1, 0));
    visit[0][0][0] = true;

    while (!q.isEmpty()) {
      Node tmpNode = q.poll();

      if (tmpNode.r == N - 1 && tmpNode.c == M - 1) {
        minDist = tmpNode.len;
        break;
      }

      for (int d = 0; d < 4; d++) {
        int ti = tmpNode.r + di[d];
        int tj = tmpNode.c + dj[d];

        if (ti >= 0 && ti < N && tj >= 0 && tj < M) {
          if (tmpNode.hasWall == 1) {
            if (map[ti][tj] == 0 && !visit[ti][tj][1]) {
              q.add(new Node(ti, tj, tmpNode.len + 1, 1));
              visit[ti][tj][1] = true;
            }
          } else {
            if (map[ti][tj] == 1 && !visit[ti][tj][1]) {
              q.add(new Node(ti, tj, tmpNode.len + 1, 1));
              visit[ti][tj][1] = true;
            } else if (map[ti][tj] == 0 && !visit[ti][tj][0]) {
              q.add(new Node(ti, tj, tmpNode.len + 1, 0));
              visit[ti][tj][0] = true;
            }
          }
        }
      }
    }
  }

  private static class Node {
    int r;
    int c;
    int len;
    int hasWall;

    public Node(int r, int c, int l, int flag) {
      this.r = r;
      this.c = c;
      this.len = l;
      this.hasWall = flag;
    }
  }
}


/*
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100

5 6
000000
011110
010000
010111
100000

5 6
011100
011000
010010
010010 
000110

5 8
01000000
01010000
01010000
01010011
00010010

1 1
0

3 3
011
111
110

6 7
0000000
0111111
0100010
0101010
0101010
0001010
*/