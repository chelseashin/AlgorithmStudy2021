// 수묶기
// 36분

// 양수부분과 음수부분(0포함)을 나눠 계산해줘야 했다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    solve();
    System.out.println();
	}

  static int[] nums;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    nums = new int[N];

    for (int i = 0; i < N; i++) {
      nums[i] = Integer.parseInt(br.readLine());
    }
    
    br.close();
  }

  public static void solve() {
    Arrays.sort(nums);

    int sum = 0;
    int idx = 0;
    for (int i = nums.length - 1; i >= 0; i--) {
      if (nums[i] > 0) {
        if (i - 1 >= 0 && nums[i-1] > 1) {
          sum += nums[i] * nums[i-1];
          i--;
          continue;
        }
      } else {
        idx = i;
        break;
      }
      sum += nums[i];
    }

    for (int i = 0; i <= idx; i++) {
      if (i + 1 <= idx) {
        sum += nums[i] * nums[i+1];
        i++;
      } else {
        sum += nums[i];
      }
    }

    System.out.println(sum);
  }
}