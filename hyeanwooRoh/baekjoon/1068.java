// 트리
// 1시간 10분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    int answer = 0;
    answer = solve(startNode);
    System.out.println(answer);
	}

  static int N, D, startNode;
  static ArrayList<Integer>[] child;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    N = Integer.parseInt(br.readLine());
    child = new ArrayList[N];

    for (int i = 0; i < child.length; i++) {
      child[i] = new ArrayList<>();
    }

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      int node = Integer.parseInt(st.nextToken());
      if (node == -1) {
        startNode = i;
        continue;
      }

      child[node].add(i);
    }

    D = Integer.parseInt(br.readLine());
    br.close();

    // deleteNode(D);
    child[D] = new ArrayList<>();
    child[D].add(-99);
  }

  public static int solve(int idx) {
    if (idx == -99) return 0;
    if (idx == D) return 1;
    if (child[idx].size() == 0) return 1;

    int sum = 0;
    for (int node : child[idx]) {
      sum += solve(node);
    }

    return sum;
  }

  static void deleteNode(int d) {
    if (child[d].size() == 0) {
      child[d].add(-99);
      return;
    }

    for (int node : child[d]) {
      deleteNode(node);
    }
  }
}