// 로봇 시뮬레이션
// 1시간 35분

// 풀이 코드는 금방짰지만 좌표의 북쪽과 남쪽을 반대로 바꾼걸 코드에 적용하지않아 계속 틀렸었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
	}

  private static int[][] map;
  private static Robot[] robots;
  private static Command[] commands;

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    map = new int[B][A];
    robots = new Robot[N+1];
    commands = new Command[M];

    for (int i = 1; i <= N; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken()) - 1;
      int y = Integer.parseInt(st.nextToken()) - 1;
      int d = convertDir(st.nextToken());
      robots[i] = new Robot(y,x,d);
      map[y][x] = i;
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int num = Integer.parseInt(st.nextToken());
      char cmd = st.nextToken().charAt(0);
      int rCnt = Integer.parseInt(st.nextToken());
      commands[i] = new Command(num, cmd, rCnt);
    }

    br.close();
  }

  private static void solve() {
	boolean isActivated = true;
    for (Command command : commands) {
      isActivated = activateRobot(command);
      if (!isActivated) break;
    }
    
    if (isActivated) System.out.println("OK");
  }

  private static int[] di = {-1,0,1,0};
  private static int[] dj = {0,1,0,-1};

  private static boolean activateRobot(Command command) {
    int num = command.num;
    char cmd = command.cmd;
    int rCnt = command.rCnt;
    
    for (int i = 0; i < rCnt; i++) {
	  int r = robots[num].r;
	  int c = robots[num].c;
	  int d = robots[num].d;
      
	  if (cmd == 'R') { // 오른쪽 턴
        robots[num].d = (d + 3) % 4;
      } else if (cmd == 'L') { // 왼쪽 턴
        robots[num].d = (d + 1) % 4;
      } else { // 한칸 앞으로
        int nr = r + di[d];
        int nc = c + dj[d];

        if (nr < 0 || nr >= map.length || nc < 0 || nc >= map[0].length) {
          System.out.println(robotCrashedWall(num));
          return false;
        }

        if (map[nr][nc] != 0) {
          System.out.println(robotCrashedRobot(num, map[nr][nc]));
          return false; 
        }

        map[r][c] = 0;
        map[nr][nc] = num;
        robots[num].r = nr;
        robots[num].c = nc;
      }
    }
    return true;
  }

  private static int convertDir(String dir) {
    if (dir.equals("S")) {
      return 0;
    } else if (dir.equals("E")) {
      return 1;
    } else if (dir.equals("N")) {
      return 2;
    } else {
      return 3;
    }
  }

  private static String robotCrashedWall(int x) {
    return String.format("Robot %d crashes into the wall", x);
  }
  
  private static String robotCrashedRobot(int x, int y) {
    return String.format("Robot %d crashes into robot %d", x, y);
  }

  private static class Robot {
    int r;
    int c;
    int d;

    public Robot(int r, int c, int d) {
      this.r = r;
      this.c = c;
      this.d = d;
    }
  }
  
  private static class Command {
    int num;
    char cmd;
    int rCnt;

    public Command(int n, char c, int r) {
      this.num = n;
      this.cmd = c;
      this.rCnt = r;
    }
  }

}
