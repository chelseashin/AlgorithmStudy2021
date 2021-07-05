// 암호 만들기
// 21분

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    init();
    
    StringBuilder str = new StringBuilder();
    solve(str, 0, 0, 0, 0);

    System.out.println(sb.toString());
	}

  static int L, C;
  static char[] chars;
  static StringBuilder sb;

  public static void init() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    L = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());

    chars = new char[C];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < C; i++) {
      chars[i] = st.nextToken().charAt(0);
    }

    Arrays.sort(chars);

    br.close();

    sb = new StringBuilder();
  }

  // vowels: 모음
  // consonants: 자음
  public static void solve(StringBuilder str, int depth, int idx, int vowCnt, int consoCnt) {
    if (depth == L) {
      if (vowCnt >= 1 && consoCnt >= 2) sb.append(str.toString()).append("\n");
      return;
    }

    for (int i = idx; i < C; i++) {
      str.append(chars[i]);
      if ("aeiou".contains(chars[i]+"")) {
        solve(str, depth + 1, i + 1, vowCnt + 1, consoCnt);
      } else {
        solve(str, depth + 1, i + 1, vowCnt, consoCnt + 1);
      }
      str.deleteCharAt(str.length() - 1);
    }
  }
}