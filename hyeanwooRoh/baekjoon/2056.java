// 작업
// 45분

// 선행작업을 거치지않았을 경우에 시간이 더 많이 걸리는 경우가 있어 조금 헤맸다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    int answer = topologicalSolve();
    System.out.println(answer);
	}

  static int N;
  static int[] totalTime, cntOfLink, buildTime;
  static ArrayList<ArrayList<Integer>> graph;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = null;
    N = Integer.parseInt(br.readLine());

    graph = new ArrayList<>();
    buildTime = new int[N];
    totalTime = new int[N];
    cntOfLink = new int[N];
    
    for (int v = 0; v < N; v++) {
      graph.add(new ArrayList<Integer>());
      st = new StringTokenizer(br.readLine());
      buildTime[v] = Integer.parseInt(st.nextToken());
      int k = Integer.parseInt(st.nextToken());
      for (int j = 0; j < k; j++) {
        int v2 = Integer.parseInt(st.nextToken()) - 1;
        graph.get(v).add(v2);
        cntOfLink[v2]++;
      }
    }

    br.close();
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

      for (int next : graph.get(cur)) {
        cntOfLink[next]--;

        if (cntOfLink[next] == 0) queue.add(next);

        if (totalTime[next] < totalTime[cur] + buildTime[next]) {
          totalTime[next] = totalTime[cur] + buildTime[next];
        }
      }
    }

    int max = 0;
    for (int time : totalTime) {
      max = Math.max(time, max);
    }
    return max;
  }
}