// 문자열 집합
// 39분

// 트라이 자료구조를 사용하는 문제인데 시간초과가 났고
// set을 사용하니 통과

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    Set<String> set = new HashSet<>();
    for (int i = 0; i < N; i++) {
      set.add(br.readLine());
    }

    int containCnt = 0;
    for (int i = 0; i < M; i++) {
      if (set.contains(br.readLine())) {
        containCnt++;
      }
    }
    br.close();

    System.out.println(containCnt);
  }

}


// trie 1

  // public static class TrieNode {
  //   private Map<Character, TrieNode> childNodes = new HashMap<>();
  //   private boolean isLastChar;

  //   Map<Character, TrieNode> getChildNodes() {
  //     return this.childNodes;
  //   }

  //   boolean isLastChar() {
  //     return this.isLastChar;
  //   }

  //   void setIsLastChar(boolean isLastChar) {
  //     this.isLastChar = isLastChar;
  //   }
  // }

  // public static class Trie {
  //   private TrieNode rootNode;

  //   Trie() {
  //     rootNode = new TrieNode;
  //   }

  //   void insert(String word) {
  //     TrieNode thisNode = this.rootNode;

  //     for (int i = 0; i < word.length(); i++) {
  //       thisNode = thisNode.getChildNodes().computeIfAbsent(word.charAt(i), c -> new TrieNode());
  //     } 
  //     thisNode.setIsLastChar(true);
  //   }

  //   boolean contains(String word) {
  //     TrieNode thisNode = this.rootNode;

  //     for (int i = 0; i < word.length(); i++) {
  //       char character = word.charAt(i);
  //       TrieNode node = thisNode.getChildNodes().get(character);

  //       if (node == null) return false;

  //       thisNode = node;
  //     }

  //     return thisNode.isLastChar();
  //   }
  // }

// trie 2

// public class B5052 {
//   static int T;
//   static int N;
//   static final int NUMS = 10;

//   static class Trie {
//     boolean isEndWord;
//     Trie children[];

//     public Trie() {
//       isEndWord = false;
//       children = new Trie[NUMS];
//       for (int i = 0; i < NUMS; ++i)
//         children[i] = null;
//     }
//   }

//   static Trie root;

//   static void insert(String key) {
//     Trie curTrie = root;
//     int length = key.length();
//     int level;
//     int index;

//     for (level = 0; level < length; ++level) {
//       index = key.charAt(level) - '0';
//       if (curTrie.children[index] == null) {
//         curTrie.children[index] = new Trie();
//       }
//       curTrie = curTrie.children[index];
//     }
//     curTrie.isEndWord = true;
//   }

//   static boolean available(String key) {
//     Trie curTrie = root;
//     int length = key.length();
//     int level;
//     int index;

//     for (level = 0; level < length; ++level) {
//       index = key.charAt(level) - '0';
//       if (curTrie.isEndWord)
//         return false;
//       curTrie = curTrie.children[index];
//     }

//     return true;
//   }

//   public static void main(String[] args) throws NumberFormatException, IOException {
//     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//     StringBuilder sb = new StringBuilder();

//     T = Integer.parseInt(br.readLine());

//     for (int t = 1; t <= T; t++) {
//       N = Integer.parseInt(br.readLine());
//       root = new Trie();
//       String[] str = new String[N];
//       for (int n = 0; n < N; n++) {
//         str[n] = br.readLine();
//         insert(str[n]);
//       }

//       boolean ans = true;

//       for (int n = 0; n < N; n++) {
//         if (!available(str[n])) {
//           ans = false;
//           break;
//         }
//       }
      
//       if(ans)
//         sb.append("YES\n");
//       else
//         sb.append("NO\n");

//     }
//     System.out.print(sb.toString());
//   }

// }