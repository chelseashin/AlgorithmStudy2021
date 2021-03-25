// 로또
// 27분

// 조합
// depth를 자꾸 다음 재귀함수에 넣어줘서 틀리다가 i+1로 바꿔서 해결

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    System.out.println(sb.toString());
	}

  static StringBuilder sb = new StringBuilder();

  private static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    while (true) {
      String input = br.readLine();
      if (input.equals("0")) break;
      solve(input);
      sb.append("\n");
    }
  }

  private static void solve(String input) {
    String[] inputs = input.split(" ");
    int[] nums = new int[Integer.parseInt(inputs[0])];
    boolean[] isUsed = new boolean[nums.length];

    for (int i = 0; i < nums.length; i++) {
      nums[i] = Integer.parseInt(inputs[i+1]);
    }

    comb(nums, isUsed, 0, 0);
  }

  private static void comb(int[] nums, boolean[] isUsed, int depth, int cnt) {
    if (cnt == 6) {
      appendToStringBuilder(nums, isUsed);
      return;
    }

    for (int i = depth; i < nums.length; i++) {
      isUsed[i] = true;
      comb(nums, isUsed, i+1, cnt+1);
      isUsed[i] = false;
    }
  }

  private static void appendToStringBuilder(int[] nums, boolean[] isUsed) {
    for (int i = 0; i < isUsed.length; i++) {
      if (isUsed[i]){
        sb.append(nums[i]).append(" ");
      }
    }
    sb.append("\n");  
  }

}
