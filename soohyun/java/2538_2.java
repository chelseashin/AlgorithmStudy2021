import java.io.*;   
import java.util.*;

public class boj_2583 {
	static boolean[][] check;
	static int m,n;
	static int count=0;		//영역의 개수를 count 
	static Queue<String> queue = new LinkedList<>();
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] vertex=new int[4];
		check= new boolean[m][n]; 
		LinkedList<Integer> sizeArr=new LinkedList<>();

		for(int i=0; i<k; i++) {		//주어진 사각형을 true로 색칠 
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<vertex.length; j++) {
				vertex[j]=Integer.parseInt(st.nextToken());
			}
			for(int j=vertex[0]; j<vertex[2]; j++) {
				for(int l=vertex[1]; l<vertex[3]; l++) {
					check[l][j]=true;
				}
			}
		}
			
		for(int i=0; i<m; i++) {	//색칠되지 않은 부분(false)을 찾아서 크기를 구함 
			for(int j=0; j<n; j++) {
				if(check[i][j]==false) {	//영역을 하나찾았으므로 
					count=1;
					check[i][j]=true;
					BFS(i,j);	//너비우선탐색으로 영역의 크기를 구함 
					sizeArr.add(count);
				}
			}
		}
		sizeArr.sort(null);
		bw.write(sizeArr.size()+"\n");
		for(int i=0; i<sizeArr.size(); i++) {
			bw.write(sizeArr.get(i)+" ");
		}
		
		bw.flush();
		bw.close();
		
	}
	public static void BFS(int x,int y) { 	//너비 우선 탐색 재귀적 실행 
		//주변을 탐색해 false면 true로 바꾸면서 큐에 넣음 
		if(x>0&&check[x-1][y]==false) {	
			check[x-1][y]=true;
			queue.add((x-1)+","+y);
		}
		if(x<m-1&&check[x+1][y]==false) {
			check[x+1][y]=true;
			queue.add((x+1)+","+y);
		}
		if(y>0&&check[x][y-1]==false) {
			check[x][y-1]=true;
			queue.add(x+","+(y-1));
		}
		if(y<n-1&&check[x][y+1]==false) {
			check[x][y+1]=true;
			queue.add(x+","+(y+1));
		}
		if(!queue.isEmpty()) {
		String str=queue.poll();
		count++;
		BFS(Integer.parseInt(str.split(",")[0]),Integer.parseInt(str.split(",")[1]));
		}
	}

}
