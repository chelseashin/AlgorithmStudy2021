import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.println(totalTree);
	}

  static int N;
  static int[] trees;
  static int totalTree;

  private static void init() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    totalTree = 0;
    
    int[] tmpTree = new int[N];
    for(int i=0; i < N; i++) {
      tmpTree[i] = Integer.parseInt(br.readLine());
    }

    trees = new int[N-1];
    for(int i=0; i < N-1; i++) {
      trees[i] = tmpTree[i+1] - tmpTree[i]; 
    }
  }

	private static void solve() {
    int gcd = getGCD(trees[1], trees[0]);
      
    for (int i = 2; i < trees.length; i++) {
      gcd = getGCD(gcd, trees[i]);
    }
    
    for (int i = 0; i < trees.length; i++) {
      totalTree += trees[i]/gcd - 1;
    }
	}
	
	private static int getGCD(int a, int b) {
    int tmp = 0;

    while (b != 0) {
      tmp = a % b;
      a = b;
      b = tmp;
    }
  
    return a;
	}

}