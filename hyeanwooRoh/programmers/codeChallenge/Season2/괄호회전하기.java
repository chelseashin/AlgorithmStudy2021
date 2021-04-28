// 00:02 ~ 00:40

import java.util.*;

public class Main {
	public static void main(String[] args) {
    System.out.println(solution("[](){}"));
    System.out.println(solution("}]()[{"));
    System.out.println(solution("[)(]"));
    System.out.println(solution("}}}"));
	}

  public static int solution(String s) {
    int answer = 0;
    for (int i = 0; i < s.length(); i++) {
      if(stacking(s, i)) answer++;
    }

    return answer;
  }

  public static boolean stacking(String s, int start) {
    int cycleCnt = 0;
    int idx = start;

    Stack<Character> stack = new Stack<>();
    while (cycleCnt < s.length()) {
      char ch = s.charAt(idx);
      if (ch == '[' || ch == '{' || ch == '(') {
        stack.push(ch);
      } else {
        if (stack.empty() || !correctBraket(stack.pop(), ch)) {
          return false;
        }
      }
      
      idx = idx + 1 == s.length() ? 0 : idx + 1;
      cycleCnt++;
    }

    return stack.empty();
  }

  public static boolean correctBraket(char ch1, char ch2) {
    switch(ch1) {
      case '[':
        return ch2 == ']';
      case '{':
        return ch2 == '}';
      case '(':
        return ch2 == ')';
    }

    return false;
  }
}
