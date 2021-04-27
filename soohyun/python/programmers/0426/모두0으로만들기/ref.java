import java.util.ArrayList;

class Solution {
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	static long[] check;
	static long count=0;
	static long answer=0;
    public static long solution(int[] a, int[][] edges) {
    	
        graph = new ArrayList[a.length];
        visited = new boolean[a.length];
        check = new long[a.length];
        for(int i=0; i<a.length; i++)
        	graph[i] = new ArrayList<>();
        //입력 배열을 기반으로 트리 구성
        for(int i=0; i<edges.length; i++)
        {
        	int from = edges[i][0];
        	int to = edges[i][1];
        	graph[from].add(to);
        	graph[to].add(from);
        }
        visited[0] = true;
        dfs(0,a);
        
        
        System.out.println(answer);
        return answer;
    }
    public static void dfs(int cur,int[] a)
    {
    	for(int i=0; i<graph[cur].size(); i++)
    	{
    		if(visited[graph[cur].get(i)]==false)
    		{
    			visited[graph[cur].get(i)]=true;
    			dfs(graph[cur].get(i),a);
                //각 노드의 가중치 값을 더해서 올라오는 과정
    			check[cur] = check[cur]+check[graph[cur].get(i)];
                //가중치 연산 수행 횟수 계산
    			answer = answer+Math.abs(check[graph[cur].get(i)]);

    				
    		}
    	}
    	check[cur] = check[cur]+a[cur];
    	if(cur==0)
    	{
    		if(check[cur]!=0)
    			answer=-1;
    	}
    }
}