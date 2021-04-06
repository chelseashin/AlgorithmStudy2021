// 신입사원
// 33분

// 풀이1. 서류순위로 정렬하고 인터뷰순위를 limit로 주어 해결
// 풀이2. 정렬할 필요없이 배열을 만들어 저장후 해결

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    int[] score = new int[100001];

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    
    int T = Integer.parseInt(br.readLine());
    for (int tc = 0; tc < T; tc++) {
      int N = Integer.parseInt(br.readLine());

      StringTokenizer st;
      for (int i = 0; i < N; i++) {
        st = new StringTokenizer(br.readLine());
        score[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken());
      }

      int pass = 1;
      int limit = score[1];
      for (int i = 2; i <= N; i++) {
        if (score[i] < limit) {
          limit = score[i];
          pass++;
        }
      }
      sb.append(pass).append("\n");
    }
    br.close();
    System.out.println(sb.toString());
  }
}


// public class Main {
// 	public static void main(String[] args) throws IOException {
//     init();
//     System.out.println(sb.toString());
// 	}

//   static int T, N;
//   static Score[] score;
//   static StringBuilder sb;

//   private static void init() throws IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     sb = new StringBuilder();
//     T = Integer.parseInt(br.readLine());
    
//     for (int tc = 0; tc < T; tc++) {
//       N = Integer.parseInt(br.readLine());
//       score = new Score[N];
//       for (int i = 0; i < N; i++) {
//         String[] st = br.readLine().split(" ");
//         score[i] = new Score(Integer.parseInt(st[0]), Integer.parseInt(st[1]));
//       }

//       sortScore();
//     }

//     br.close();
//   }

//   private static void sortScore() {
//     Arrays.sort(score);
//     // System.out.println(Arrays.toString(score));

//     int pass = 0;
//     int limit = score[0].interview;
//     for (Score s : score) {
//       if (s.resume == 1) {
//         pass++;
//       } else if (s.interview < limit) {
//         limit = s.interview;
//         pass++;
//       }
//     }

//     sb.append(pass).append("\n");
//   }

//   static class Score implements Comparable<Score> {
//     int resume;
//     int interview;

//     public Score(int r, int i) {
//       this.resume = r;
//       this.interview = i;
//     }

//     @Override
//     public int compareTo(Score s) {
//       if (this.resume > s.resume) {
//         return 1;
//       } else {
//         return -1;
//       }
//     }

//     @Override
//     public String toString() {
//       return this.resume + "," + this.interview;
//     }
//   }
// }
