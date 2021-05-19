// 최솟값과 최댓값
// 2시간 47분

// 주어진 배열을 이진트리로 바꿀 수는 있었지만
// 그 이상은 방법이 떠오르지않아서 다른 풀이를 참고했다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println(sb.toString());
	}

  static int N;
  static int[] arr, minTree, maxTree;
  static int[][] range;
  static StringBuilder sb;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    arr = new int[N+1];
    for (int i = 1; i <= N; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    range = new int[M][2];
    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      range[i][0] = Integer.parseInt(st.nextToken());
      range[i][1] = Integer.parseInt(st.nextToken());
    }

    minTree = new int[N*4];
    maxTree = new int[N*4];

    br.close();
    sb = new StringBuilder();
  }

  public static void solve() {
    initMin(1, N, 1);
    initMax(1, N, 1);

    for (int[] r : range) {
      sb.append(findMin(1, N, 1, r[0], r[1])).append(" ").append(findMax(1, N, 1, r[0], r[1])).append("\n");
    }
  }

  static int initMin(int start, int end, int node) {
    if (start == end) {
      return minTree[node] = arr[start];
    }
    int mid = (start + end) / 2;
    return minTree[node] = Math.min(initMin(start, mid, node*2), initMin(mid+1, end, node*2+1));
  }

  static int initMax(int start, int end, int node) {
    if (start == end) {
      return maxTree[node] = arr[start];
    }
    int mid = (start + end) / 2;
    return maxTree[node] = Math.max(initMax(start, mid, node*2), initMax(mid+1, end, node*2+1));
  }

  static int findMin(int start, int end, int node, int left, int right) {
    if (right < start || end < left) {
      return Integer.MAX_VALUE;
    }
    if (left <= start && end <= right) {
      return minTree[node];
    }
    int mid = (start + end) / 2;
    return Math.min(findMin(start, mid, node*2, left, right), findMin(mid+1, end, node*2+1, left, right));
  }

  static int findMax(int start, int end, int node, int left, int right) {
    if (right < start || end < left) {
      return Integer.MIN_VALUE;
    }
    if (left <= start && end <= right) {
      return maxTree[node];
    }
    int mid = (start + end) / 2;
    return Math.max(findMax(start, mid, node*2, left, right), findMax(mid+1, end, node*2+1, left, right));
  }
}