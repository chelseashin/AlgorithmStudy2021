// 캐슬 디펜스
// 1시간 40분

// 비트마스크도 같이 공부하면서 풀었다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(maxKill);
	}

  static int N, M, D, maxKill;
  static ArrayList<Enemy> enemy; 

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    D = Integer.parseInt(st.nextToken());
    maxKill = 0;

    enemy = new ArrayList<>();
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < M; j++) {
        if (st.nextToken().equals("1")) {
          enemy.add(new Enemy(i, j));
        }
      }
    }

    br.close();
  }

  private static void solve() {
    int[] archer;
    for (int i = 0; i < 1 << M; i++) {
      if (Integer.bitCount(i) == 3) {
        archer = new int[M];
        for (int j = 0; j < M; j++) {
          archer[j] = i & 1 << j;
        }

        shootEnemy(archer);
      }
    }
  }

  private static void shootEnemy(int[] archer) {
    ArrayList<Enemy> copyEnemy = copyList();
    int killCnt = 0;

    while (copyEnemy.size() != 0) {
      // check each enemy for each archer
      for (int i = 0; i < M; i++) {
        if (archer[i] != 0) {
          int killIdx = Integer.MAX_VALUE;
          int minDist = Integer.MAX_VALUE;
          int col = Integer.MAX_VALUE;
          for (int j = 0; j < copyEnemy.size(); j++) {
            Enemy tmpE = copyEnemy.get(j);
            int dist = Math.abs(N - tmpE.r) + Math.abs(i - tmpE.c);
            if (dist <= D && dist <= minDist) {
              if (dist < minDist) {
                killIdx = j;
                minDist = dist;
                col = tmpE.c;
              } else if (dist == minDist && tmpE.c < col) {
                killIdx = j;
                minDist = dist;
                col = tmpE.c;
              }
            }
          }

          if (killIdx != Integer.MAX_VALUE) copyEnemy.get(killIdx).setKilled();
        }
      }  

      // delete enemy from list
      for (int i = copyEnemy.size() - 1; i >= 0; i--) {
        if (copyEnemy.get(i).isKilled) {
          copyEnemy.remove(i);
          killCnt++;
          continue;
        } else if (copyEnemy.get(i).r  == N - 1) {
          copyEnemy.remove(i);
        }
      }

      // update enemy's location
      for (int i = 0; i < copyEnemy.size(); i++) {
        copyEnemy.get(i).moveForward();
      }
    }

    maxKill = Math.max(maxKill, killCnt);
  }

  private static ArrayList<Enemy> copyList() {
    ArrayList<Enemy> tmpList = new ArrayList<>();
    for (int i = 0; i < enemy.size(); i++) {
      tmpList.add(new Enemy(enemy.get(i)));
    }
    return tmpList;
  }

  static class Enemy {
    int r;
    int c;
    boolean isKilled;
    
    public Enemy(int r, int c) {
      this.r = r;
      this.c = c;
      this.isKilled = false;
    }

    public Enemy(Enemy e) {
      this.r = e.r;
      this.c = e.c;
      this.isKilled = false;
    }

    public void moveForward() {
      this.r = this.r + 1;
    }

    public void setKilled() {
      this.isKilled = true;
    }

    @Override
    public String toString() {
      return this.r + "," + this.c + (this.isKilled ? " T" : " F");
    }
  }
}
