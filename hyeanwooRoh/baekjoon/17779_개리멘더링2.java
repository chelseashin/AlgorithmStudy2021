import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 1시간 38분 + 문제고민
// 어떻게 풀어야할지 감이 안와서 접었다가
// 지하철타면서 생각했더니 방법이 떠올랐다
// 조금 방황했지만 코드를 짜다보니 더 적당한 방법이 생각나 큰 어려움없이 풀었다

public class Main {
  public static void main(String[] args) throws Exception {
    init();
    solve();
    out();
  }

  static BufferedReader br;
  static StringTokenizer st;
  static int N, minimumPeople;
  static int[][] map; 
  
  static void init() throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    minimumPeople = Integer.MAX_VALUE;
    map = new int[N][N];
    
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        int tmp = Integer.parseInt(st.nextToken());
        map[i][j] = tmp;
      }
    }
    
    br.close();
  }

  static void solve() {
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < N; c++) {
        for (int d1 = 1; d1 <= N - 2 ; d1++) {
          for (int d2 = 1; d2 <= N - 2; d2++) {
            if(d1 + d2 > N - 1 || c < d1 || c + d2 >= N || r + d1 + d2 >= N) continue;
            
            boolean[][] visit = new boolean[N][N];
            int people5 = areaFive(visit, r,c,d1,d2);
            int[] peoples = divideArea(visit, r,c,d1,d2);
            checkMax(peoples, people5);
          }
        }
      }
    }
  }

  static void checkMax(int[] peoples, int people5) {
    int maxP = people5;
    int minP = people5;

    for(int i = 0; i < 4; i++) {
      maxP = Math.max(maxP, peoples[i]);
      minP = Math.min(minP, peoples[i]);
    }

    minimumPeople = Math.min(minimumPeople, maxP - minP);
  }

  static int areaFive(boolean[][] visit, int x, int y, int d1, int d2) {
    int people5 = map[x][y];
    visit[x][y] = true;
    int ly = y;
    int ry = y;
    for (int tx = x+1; tx <= d1 + d2 + x; tx++) {
      ly = (d1 <= tx - x - 1) ? ly + 1 : ly - 1;
      ry = (d2 <= tx - x - 1) ? ry - 1 : ry + 1;
      int tmp = 0;
      while(ly + tmp != ry + 1) {
        people5 += map[tx][ly+tmp];
        visit[tx][ly+tmp] = true;
        tmp++;
      }
    }
    return people5;
  }
  
  static int[] divideArea(boolean[][] visit, int x, int y, int d1, int d2) {
    int[] people = new int[4];
    for (int r = 0; r < N; r++) {
      for (int c = 0; c < N; c++) {
        if(visit[r][c]) continue;
        
        if(r < x + d1 && c <= y) {
          // Area 1
          people[0] += map[r][c];
        } else if(r <= x + d2 && c > y) {
          // Area 2
          people[1] += map[r][c];
        } else if(r >= x + d1 && c < y - d1 + d2) {
          // Area 3
          people[2] += map[r][c];
        } else if(r > x + d2 && c >= y - d1 + d2) {
          // Area 4
          people[3] += map[r][c];
        } else {
          // Area 5
          people[4] += map[r][c];
        }
      }
    }
    return people;
  }
  
  static void out() {
    System.out.println(minimumPeople);
  }
}
/*
6
1 1 1 1 2 2
1 1 1 5 2 2
1 1 5 5 5 2
3 5 5 5 4 4
3 3 5 4 4 4
3 3 4 4 4 4
*/