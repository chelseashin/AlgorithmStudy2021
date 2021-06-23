// LCA

import java.io.*;
import java.util.*;

public class Main {

  static int[] parents, depths;
  static ArrayList<Integer>[] tree;

  public static void main(String[] args) throws NumberFormatException, IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int inputCnt = Integer.parseInt(br.readLine());
    tree = new ArrayList[inputCnt+1];
    for (int i = 1; i <= inputCnt; i++) {
      tree[i] = new ArrayList<Integer>();
    }

    parents = new int[inputCnt+1];
    depths = new int[inputCnt+1];
    Arrays.fill(depths,-1);
    
    StringTokenizer st;
    for(int i = 0; i < inputCnt - 1; i++){
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      tree[a].add(b);
      tree[b].add(a);
    }
    
    dfs(1,1,0); //레벨 및 부모 노드 저장
    
    int caseCnt = Integer.parseInt(br.readLine());
    for(int i = 0; i < caseCnt; i++){
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      
      int result = LCA(a,b);
      
      bw.write(String.valueOf(result));
      bw.newLine();
    }

    bw.flush();
    bw.close();
    br.close();
  }
  
  public static int LCA(int a, int b){
    int aDepth = depths[a];
    int bDepth = depths[b];
    
    while (aDepth > bDepth){
      a = parents[a];
      aDepth--;
    }

    while (bDepth > aDepth){
      b = parents[b];
      bDepth--;
    }

    while(a != b){
      a = parents[a];
      b = parents[b];
    }

    return a;
  }

  public static void dfs(int current, int depth, int parent){
    depths[current] = depth;
    parents[current] = parent;

    for(int nextNode : tree[current]){
      if(nextNode != parent){
        dfs(nextNode,depth+1,current);
      }
    }
  }
}