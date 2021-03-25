// 로봇
// 2시간 38분

// 처음에 풀었던 방법 자체는 맞았지만 메모리초과때문에 오류를 제대로 알지못했고
// 다른방식으로 계속 도전하다가 직진가능거리가 1,2,3이라는 걸 1시간 20분쯤에 알았다
// 빠트린 조건을 추가했는데도 계속 실패했고
// 결국 정답을 보고 나서야 방문배열 처리가 문제임을 알았다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  static int N, M;
  static Robot sRobot, eRobot;
  static int[][] map;
  static boolean[][][] visit;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    map = new int[N][M];
    visit = new boolean[N][M][4];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    st = new StringTokenizer(br.readLine());
    sRobot = new Robot(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, 0);
    
    st = new StringTokenizer(br.readLine());
    eRobot = new Robot(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, 0);
  
    br.close();
  }

  // 우 좌 하 상
  static int[] di = {0,0,1,-1};
  static int[] dj = {1,-1,0,0};

  private static void solve() {
    Queue<Robot> queue = new LinkedList<>();
    queue.add(sRobot);
    visit[sRobot.r][sRobot.c][sRobot.d] = true;

    while (!queue.isEmpty()) {
      Robot tRobot = queue.poll();

      if (tRobot.r == eRobot.r && tRobot.c == eRobot.c && tRobot.d == eRobot.d) {
        System.out.println(tRobot.move);
        return;
      }

      // 지금 로봇의 방향쪽의 0확인
      int ti = tRobot.r + di[tRobot.d];
      int tj = tRobot.c + dj[tRobot.d];
      int len = 0;
      while (len < 3 && ti >= 0 && ti < N && tj >= 0 && tj < M && map[ti][tj] == 0) {
        if (!visit[ti][tj][tRobot.d]) {
          visit[ti][tj][tRobot.d] = true;
          queue.add(new Robot(ti, tj, tRobot.d, tRobot.move + 1));
        }
        ti += di[tRobot.d];
        tj += dj[tRobot.d];
        len++;
      }

      // 왼쪽 오른쪽 체크
      int leftD = tRobot.d > 1 ? (tRobot.d + 2) % 4 : tRobot.d == 0 ? (tRobot.d + 3) % 4 : (tRobot.d + 1) % 4;
      if (!visit[tRobot.r][tRobot.c][leftD]) {
        visit[tRobot.r][tRobot.c][leftD] = true;
        queue.add(new Robot(tRobot.r, tRobot.c, leftD, tRobot.move + 1));
      }

      int rightD = tRobot.d < 2 ? (tRobot.d + 2) % 4 : tRobot.d == 2 ? (tRobot.d + 3) % 4 : (tRobot.d + 1) % 4;
      if (!visit[tRobot.r][tRobot.c][rightD]) {
        visit[tRobot.r][tRobot.c][rightD] = true;
        queue.add(new Robot(tRobot.r, tRobot.c, rightD, tRobot.move + 1));
      }
    }

  }

  private static class Robot {
    int r;
    int c;
    int d;
    int move;

    public Robot(int r, int c, int d, int m) {
      this.r = r;
      this.c = c;
      this.d = d;
      this.move = m;
    }
  }
}
