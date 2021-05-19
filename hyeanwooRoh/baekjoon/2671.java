// 잠수함 식별
// 1시간 10분

// 정규표현식을 사용하자니 걸러지지않는 부분이 있어 for문으로 풂

import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    solve();
  }

  public static void solve() throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = br.readLine();
    br.close();

    boolean isNoise = false;
    int part1, part2;

    if (input.charAt(0) == '1') {
      part1 = 1;
      part2 = 0;
    } else {
      part1 = 0;
      part2 = 1;
    }

    for (int i = 1; i < input.length(); i++) {
      if (part1 != 0) {
        if (input.charAt(i) == '1') {
          switch (part1) {
            case 1:
            case 2:
              isNoise = false;
              part1 = 0;
              break;
            case 3:
              part1 = 4;
              break;
            case 4:
              break;
          }
        } else {
          switch (part1) {
            case 1:
              part1 = 2;
              break;
            case 2:
              part1 = 3;
              break;
            case 3:
              break;
            case 4:
              part1 = 0;
              part2 = 1;
              break;
          }
        }
      } else if (part2 != 0) {
        if (input.charAt(i) == '1') {
          switch (part2) {
            case 1:
              part2 = 2;
              break;
            case 2:
              part2 = 0;
              part1 = 1;
              break;
          }
        } else {
          switch (part2) {
            case 1:
              if (i > 3 && input.charAt(i-3) == '1') {
                part1 = 3;
                part2 = 0;
              } else {
                isNoise = true;
                part2 = 0;
              }
              break;
            case 2:
              part2 = 1;
              break;
          }
        }
      } else {
        isNoise = true;
        break;
      }
    }

    if (!(part1 == 4 || part2 == 2)) isNoise = true;


    if (isNoise) {
      System.out.println("NOISE");
    } else {
      System.out.println("SUBMARINE");
    }
  }

}