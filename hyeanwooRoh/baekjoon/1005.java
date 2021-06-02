// ACM Craft
// 50분

// 방법은 떠오를듯 말듯한데 코드로 구현하기가 쉽지않아서 다른 사람 풀이를 참고했다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();

    int T = Integer.parseInt(br.readLine());
    for (int tc = 0; tc < T; tc++) {
      init(br);
      sb.append(topologicalSolve()).append("\n");
    }

    br.close();

    System.out.println(sb.toString());
	}

  static int winBulid;
  static int[] totalTime, cntOfLink, buildTime;
  static ArrayList<ArrayList<Integer>> graph;

  public static void init(BufferedReader br) throws IOException {
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    graph = new ArrayList<>();
    buildTime = new int[N];
    totalTime = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      buildTime[i] = Integer.parseInt(st.nextToken());
      graph.add(new ArrayList<Integer>());
    }

    cntOfLink = new int[N];
    for (int i = 0; i < K; i++) {
      st = new StringTokenizer(br.readLine());
      int v1 = Integer.parseInt(st.nextToken()) - 1;
      int v2 = Integer.parseInt(st.nextToken()) - 1;
      graph.get(v1).add(v2);
      cntOfLink[v2]++;
    }

    winBulid = Integer.parseInt(br.readLine()) - 1;
  }

  public static int topologicalSolve() {
    Queue<Integer> queue = new LinkedList<>();
    
    for (int i = 0; i < cntOfLink.length; i++) {
      if (cntOfLink[i] == 0) {
        queue.add(i);
        totalTime[i] = buildTime[i];
      }
    }

    while (!queue.isEmpty()) {
      int cur = queue.poll();
      if (cur == winBulid) break;

      for (int next : graph.get(cur)) {
        cntOfLink[next]--;

        if (cntOfLink[next] == 0) queue.add(next);

        if (totalTime[next] < totalTime[cur] + buildTime[next]) {
          totalTime[next] = totalTime[cur] + buildTime[next];
        }
      }
    }

    return totalTime[winBulid];
  }
}

