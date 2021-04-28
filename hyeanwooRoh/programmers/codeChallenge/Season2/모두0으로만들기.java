// 01:00 ~ 02:00

import java.util.*;

public class Main {
	public static void main(String[] args) {
    int[] weights = {-5,0,2,1,2};
    int[][] edges = {{0,1},{3,4},{2,3},{0,3}};
    System.out.println(solution(weights, edges));
	}

  static ArrayList<Integer>[] list;
  static Long[] sumWeight;
  static boolean[] visited;
  static Long answer;

  public static long solution(int[] weights, int[][] edges) {
    list = new ArrayList[weights.length];
    sumWeight = new Long[weights.length];
    visited = new boolean[weights.length];
    answer = 0l;

    long sum = 0l;
    for (int i = 0; i < weights.length; i++) {
      list[i] = new ArrayList<>();
      sumWeight[i] = (long) weights[i];
      sum += weights[i];
    }

    if (sum != 0l) return -1l;

    for (int[] edge : edges) {
      list[edge[0]].add(edge[1]);
      list[edge[1]].add(edge[0]);
    }

    dfs(0,0);

    return answer;
  }

  static void dfs(int cur, int prt) {
    if (visited[cur]) return;

    visited[cur] = true;

    for (int next : list[cur]) {
      if (next != prt) {
        dfs(next, cur);
      }
    }

    sumWeight[prt] += sumWeight[cur];
    answer += Math.abs(sumWeight[cur]);
  }

}
