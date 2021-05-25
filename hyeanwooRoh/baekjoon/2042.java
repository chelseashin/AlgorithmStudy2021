// 구간 합 구하기

// 세그먼트 트리 알고리즘 기본

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println();
	}

  static int N, M, K;
  static long[] a, tree;
  static long[][] commands;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    a = new long[N];
    for (int i = 0; i < N; i++) {
      a[i] = Long.parseLong(br.readLine());
    }

    commands = new long[M+K][3];
    for (int i = 0; i < commands.length; i++) {
      st = new StringTokenizer(br.readLine());
      commands[i][0] = Long.parseLong(st.nextToken());
      commands[i][1] = Long.parseLong(st.nextToken());
      commands[i][2] = Long.parseLong(st.nextToken());
    }

    br.close();

    int h = (int) Math.ceil(Math.log(N) / Math.log(2));
    tree = new long[1 << (h+1)];
    
    initTree(1, 0, N - 1);
  }

  public static void solve() {
    for (long[] cmd : commands) {
      if (cmd[0] == 1) {
        int t2 = (int) cmd[1];
        long t3 = cmd[2];

        t2--;
        long diff = t3 - a[t2];
        a[t2] = cmd[2];
        update(1, 0, N - 1, t2, diff);
      } else {
        int t2 = (int) cmd[1];
        int t3 = (int) cmd[2];
        System.out.println(sum(1, 0, N-1, t2 - 1, t3 - 1));
      }
    }
  }

  static long initTree(int node, int start, int end) {
    if (start == end) {
      return tree[node] = a[start];
    } else {
      return tree[node] = initTree(node*2, start, (start+end)/2) + initTree(node*2+1, (start+end)/2+1, end);
    }
  }

  static void update(int node, int start, int end, int index, long diff) {
    if (index < start || index > end) return;
    tree[node] = tree[node] + diff;
    if (start != end) {
      update(node*2, start, (start+end)/2, index, diff);
      update(node*2+1, (start+end)/2+1, end, index, diff);
    }
  }

  static long sum(int node, int start, int end, int left, int right) {
    if (left > end || right < start) return 0;
    if (left <= start && end <= right) return tree[node];

    return sum(node*2, start, (start+end)/2, left, right) + sum(node*2+1, (start+end)/2+1, end, left, right);
  }
}