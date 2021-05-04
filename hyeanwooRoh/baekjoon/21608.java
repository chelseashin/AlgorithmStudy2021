// 상어 초등학교
// 1시간 30분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(answer);
	}

  static int N, answer;
  static int[] cmd;
  static int[][] crushList, emptyCnt, classRoom;
  static Student[] studentLoc;
  static boolean[][] isfull;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    N = Integer.parseInt(br.readLine());
    answer = 0;

    cmd = new int[N*N];
    isfull = new boolean[N][N];
    crushList = new int[N*N+1][4];
    classRoom = new int[N][N];
    for (int i = 1; i < crushList.length; i++) {
      st = new StringTokenizer(br.readLine());
      int studentNum = Integer.parseInt(st.nextToken());
      cmd[i-1] = studentNum;

      int[] tmp = crushList[studentNum];
      for (int j = 0; j < 4; j++) {
        tmp[j] = Integer.parseInt(st.nextToken());
      }
    }
    br.close();

    initStudentLoc();
    initEmptyCnt();
  }

  static void initStudentLoc() {
    studentLoc = new Student[crushList.length];
    for (int i = 0; i < studentLoc.length; i++) {
      studentLoc[i] = new Student(-1, -1);
    }
  }

  static void initEmptyCnt() {
    emptyCnt = new int[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        emptyCnt[i][j] = 4;
      }
    }

    for (int i = 1; i < N - 1; i++) {
      emptyCnt[i][0] = 3;
      emptyCnt[i][N-1] = 3;
      emptyCnt[0][i] = 3;
      emptyCnt[N-1][i] = 3;
    }

    emptyCnt[0][0] = 2;
    emptyCnt[0][N-1] = 2;
    emptyCnt[N-1][0] = 2;
    emptyCnt[N-1][N-1] = 2;
  }

  public static void solve() {
    for (int c : cmd) {
      Student loc = findCrushOnLoc(c);
      settleSeat(loc, c);
    }
    calcAnswer();
  }

  static int[] di = {1, 0, -1, 0};
  static int[] dj = {0, 1, 0, -1};

  static Student findCrushOnLoc(int std) {
    Student loc = new Student(-1, -1);
    int[][] tmpRoom = new int[N][N];
    // 1
    for (int s : crushList[std]) {
      Student tmpStd = studentLoc[s];
      if (tmpStd.r == -1) continue;

      for (int d = 0; d < 4; d++) {
        int nr = tmpStd.r + di[d];
        int nc = tmpStd.c + dj[d];
        if (nr < 0 || nr >= N || nc < 0 || nc >= N || isfull[nr][nc]) continue;

        tmpRoom[nr][nc]++;
      }
    }

    int max = 0;
    int maxCnt = 1;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (tmpRoom[i][j] > max) {
          max = tmpRoom[i][j];
          maxCnt = 1;
          loc.r = i;
          loc.c = j;
        } else if (tmpRoom[i][j] == max) {
          maxCnt++;
        }
      }
    }

    if (maxCnt == 1) return loc;

    // 2, 3
    int maxEmpty = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (isfull[i][j]) continue;
        if (tmpRoom[i][j] == max && emptyCnt[i][j] > maxEmpty) {
          maxEmpty = emptyCnt[i][j];
          loc.r = i;
          loc.c = j;
        }
      }
    }

    if (loc.r != -1) return loc;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (classRoom[i][j] == 0) {
          loc.r = i;
          loc.c = j;
          return loc;
        }
      }
    }

    return loc;
  }

  static void settleSeat(Student loc, int stdNum) {
    int r = loc.r;
    int c = loc.c;

    studentLoc[stdNum].r = r;
    studentLoc[stdNum].c = c;
    classRoom[r][c] = stdNum;
    emptyCnt[r][c] = 0;
    isfull[r][c] = true;
    
    for (int d = 0; d < 4; d++) {
      int nr = r + di[d];
      int nc = c + dj[d];
      if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

      emptyCnt[nr][nc]--;
    }
  }

  static void calcAnswer() {
    int aroundCnt;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        aroundCnt = 0;
        for (int s : crushList[classRoom[i][j]]) {
          int tr = studentLoc[s].r;
          int tc = studentLoc[s].c;
          if ((Math.abs(i - tr) + Math.abs(j - tc)) == 1) aroundCnt++;
        }

        answer += getScore(aroundCnt);
      }
    }
  }
  
  static int getScore(int cnt) {
    switch(cnt) {
      case 0:
        return 0;
      case 1:
        return 1;
      case 2:
        return 10;
      case 3:
        return 100;
      case 4:
        return 1000;
    }
    return -1;
  }

  static class Student {
    int r;
    int c;

    public Student(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }

}