// 숫자 카드
// 17분

// 단순이진탐색 문제이지만 메모리를 조금 더 많이 써서 푸는게 시간은 더 빨랐다

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    StringBuilder sb = new StringBuilder();

    int N = Integer.parseInt(br.readLine());
    int[] haveNums = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      haveNums[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(haveNums);

    int M = Integer.parseInt(br.readLine());
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < M; i++) {
      int num = Integer.parseInt(st.nextToken());
      if (binarySearch(haveNums, num)) {
        sb.append("1 ");
      } else {
        sb.append("0 ");
      }
    }
    br.close();
    System.out.println(sb.toString());
	}

  public static boolean binarySearch(int[] nums, int n) {
    int s = 0;
    int e = nums.length - 1;

    while (s <= e) {
      int mid = (s + e) / 2;

      if (nums[mid] > n) {
        e = mid - 1;
      } else if (nums[mid] < n) {
        s = mid + 1;
      } else {
        return true;
      }
    }

    return false;
  }
}
