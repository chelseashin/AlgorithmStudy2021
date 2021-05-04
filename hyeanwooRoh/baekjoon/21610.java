// 마법사 상어와 비바라기
// 1시간 15분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(sumAllWater());
	}

  static int sumAllWater() {
    int sum = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        sum += bucket[i][j];
      }
    }
    return sum;
  }

  static int N, M;
  static int[][] bucket, command, rainInfo;
  static final int EARTH = 0;
  static final int CLOUD = 1;
  static final int RAIN = 2;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    bucket = new int[N][N];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        bucket[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    command = new int[M][2];
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      command[i][0] = Integer.parseInt(st.nextToken()) - 1;
      command[i][1] = Integer.parseInt(st.nextToken());
    }

    br.close();

    rainInfo = new int[N][N];
    rainInfo[N-1][0] = CLOUD;
    rainInfo[N-1][1] = CLOUD;
    rainInfo[N-2][0] = CLOUD;
    rainInfo[N-2][1] = CLOUD;
  }

  static int[] di = {0,-1,-1,-1,0,1,1,1};
  static int[] dj = {-1,-1,0,1,1,1,0,-1};

  public static void solve() {
        // printRainInfo();
        // printBucket();
    for (int[] cmd : command) {
        // System.out.println("Before Move");
        // printRainInfo();
        // printBucket();
      moveCloud(cmd[0], cmd[1]);
        // System.out.println("After move");
        // printRainInfo();
        // printBucket();
      copyWaterAfterRain();
        // System.out.println("Before make");
        // printRainInfo();
        // printBucket();
      makeCloud();
        // System.out.println("After make");
        printRainInfo();
        printBucket();
    }
  }

  static void moveCloud(int dir, int s) {
    ArrayList<Node> cloudList = new ArrayList<>();
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (rainInfo[i][j] == CLOUD) {
          cloudList.add(new Node(i, j));
        }
      }
    }

    // for (Node node : cloudList) {
    //   int nr = (node.r + di[dir] * (s % N) + N) % N;
    //   int nc = (node.c + dj[dir] * (s % N) + N) % N;
    //   rainInfo[node.r][node.c] = EARTH;
    //   rainInfo[nr][nc] = RAIN;
    //   bucket[nr][nc]++;
    // }

    // int len = cloudList.size();
    // int idx = 0;
    // boolean[] isMoved = new boolean[len];
    // while (idx < len) {
    //   for (int i = 0; i < len; i++) {
    //     if (isMoved[i]) continue;
        
    //     Node node = cloudList.get(i);
    //     int nr = (node.r + di[dir] * (s % N) + N) % N;
    //     int nc = (node.c + dj[dir] * (s % N) + N) % N;

    //     if (rainInfo[nr][nc] != EARTH) continue;
        
    //     rainInfo[node.r][node.c] = EARTH;
    //     rainInfo[nr][nc] = RAIN;
    //     bucket[nr][nc]++;

    //     isMoved[i] = true;
    //     idx++;
    //   }
    // }

    rainInfo = new int[N][N];
    for (Node node : cloudList) {
      int nr = (node.r + di[dir] * (s % N) + N) % N;
      int nc = (node.c + dj[dir] * (s % N) + N) % N;
      rainInfo[nr][nc] = RAIN;
      bucket[nr][nc]++;
    }

  }

  static void copyWaterAfterRain() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (rainInfo[i][j] == RAIN) {
          int waterAmount = checkCross(i, j);
          bucket[i][j] += waterAmount;
        }
      }
    }
  }

  static int checkCross(int r, int c) {
    int cnt = 0;
    for (int d = 1; d < 8; d+=2) {
      int nr = r + di[d];
      int nc = c + dj[d];
      if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

      if (bucket[nr][nc] > 0) cnt++;
    }
    return cnt;
  }

  static void makeCloud() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (rainInfo[i][j] != RAIN && bucket[i][j] > 1) {
          rainInfo[i][j] = CLOUD;
          bucket[i][j] -= 2;
        }

        if (rainInfo[i][j] == RAIN) rainInfo[i][j] = EARTH;
      }
    }
  }

  static class Node {
    int r;
    int c;

    public Node(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }

  static void printRainInfo() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(rainInfo[i][j]+" ");
      }
      System.out.println();
    }  
    System.out.println();
  }

  static void printBucket() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        System.out.print(bucket[i][j]+" ");
      }
      System.out.println();
    }  
    System.out.println();
  }
}