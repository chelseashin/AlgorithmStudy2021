// 소문난 칠공주
// 1시간 43분

// 단순 백트래킹이 아닌 아이디어가 필요한 문제
// 조합을 백트래킹으로, 붙어있는지 확인을 bfs로 해서 풀었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    combination(0, 0, 0);
    System.out.println(cnt);
	}

  static int cnt = 0;
  static char[][] students = new char[5][5];
  // static boolean[][] visited = new boolean[5][5];
  static boolean[] visited = new boolean[25];
  static ArrayList<Princess> princessList = new ArrayList<>();

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    for (int i = 0; i < 5; i++) {
      students[i] = br.readLine().toCharArray();
    }
    
    br.close();
  }

  static void combination(int idx, int lee, int lim) {
    if (lee + lim == 7) {
      if (lim > lee) return;
      if (bfs()) cnt++;
      return;
    }

    for (int i = idx; i < 25; i++) {
      if (visited[i]) continue;
      int r = i / 5;
      int c = i % 5;

      Princess tmpP = new Princess(r, c);

      princessList.add(tmpP);
      visited[i] = true;
      if (students[r][c] == 'Y') {
        combination(i + 1, lee, lim + 1);
      } else {
        combination(i + 1, lee + 1, lim);
      }
      visited[i] = false;
      princessList.remove(princessList.size() - 1);
    }
  }

  static int[] di = {0,1,0,-1};
  static int[] dj = {1,0,-1,0};

  static boolean bfs() {
    Queue<Princess> queue = new LinkedList<>();
    boolean[] isVisit = new boolean[7];
    
    queue.add(princessList.get(0));
    isVisit[0] = true;
    int linkCnt = 1;

    while (!queue.isEmpty()) {
      Princess tmpP = queue.poll();

      for (int i = 1; i < 7; i++) {
        if (isVisit[i]) continue;
        for (int d = 0; d < 4; d++) {
          int nr = tmpP.r + di[d];
          int nc = tmpP.c + dj[d];
          
          if (nr == princessList.get(i).r && nc == princessList.get(i).c) {
            queue.add(new Princess(nr, nc));
            isVisit[i] = true;
            linkCnt++;
          }
        }
      }
    }

    return linkCnt == 7 ? true : false;
  }

  static class Princess {
    int r; int c;

    public Princess(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}
