import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

//2시간 51분
//1시간 20분동안 DFS로 풀다가 포기하고 답봄
//BFS로 풀면 된다는 것만 보고 다시 도전
//하다가 안돼서 포기하고 답보고 베낌
// 방문체크를 하는 배열을 만들어주는 것이 핵심이라고 생각

public class Main {
	public static void main(String[] args) throws Exception {
		init();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, min;
	static int[][] chess;
	
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		min = Integer.MAX_VALUE;
		
		int r = 0;
		int c = 0;
		chess = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				chess[i][j] = Integer.parseInt(st.nextToken());
				if(chess[i][j] == 1) {
					r = i;
					c = j;
				}
			}
		}
		
		br.close();
		System.out.println(bfs(r, c));
	}

	static int[][] di = {
		{-2,-2,-1,1,2,2,1,-1},
		{-1,-1,1,1},
		{-1,0,1,0}
	};
	static int[][] dj = {
		{-1,1,2,2,1,-1,-2,-2},
		{-1,1,1,-1},
		{0,1,0,-1}
	};
	
	// 0: night | 1: look | 2: bishop
	static int bfs(int r, int c) {
		Queue<Node> queue = new LinkedList<>();
		boolean[][][][] visited = new boolean[N][N][3][N*N+1];

		// 각각 나이트, 비숍, 룩으로 시작
		queue.add(new Node(r,c,0,2,0));
		queue.add(new Node(r,c,0,2,1));
		queue.add(new Node(r,c,0,2,2));
		visited[r][c][0][2] = true;
		visited[r][c][1][2] = true;
		visited[r][c][2][2] = true;
		
		while(!queue.isEmpty()) {
			Node tnode = queue.poll();

			// 마지막 숫자에 도달하면 종료
			if(tnode.step == N*N+1) {
				return tnode.sec;
			}
			
			
			for (int piece = 0; piece < 3; piece++) {
				// 같은 말일 경우 움직여주고
				if(tnode.p == piece) {
					if(piece == 0) { // 나이트
						for (int d = 0; d < 8; d++) {
							int ti = tnode.r + di[0][d];
							int tj = tnode.c + dj[0][d];
							
							if(ti < N && ti >= 0 && tj < N && tj >= 0 && !visited[ti][tj][0][tnode.step]) {
								if(chess[ti][tj] == tnode.step) {
									queue.add(new Node(ti, tj, tnode.sec+1, tnode.step+1, 0));
								} else {
									queue.add(new Node(ti, tj, tnode.sec+1, tnode.step, 0));
								}
								visited[ti][tj][0][tnode.step] = true;
							}
						}
					} else { // 비숍, 룩
						for (int d = 0; d < 4; d++) {
							for (int offset = 1; offset < N; offset++) {
								int ti = tnode.r + di[piece][d]*offset;
								int tj = tnode.c + dj[piece][d]*offset;
								
								if(ti < N && ti >= 0 && tj < N && tj >= 0 && !visited[ti][tj][piece][tnode.step]) {
									if(chess[ti][tj] == tnode.step) {
										queue.add(new Node(ti, tj, tnode.sec+1, tnode.step+1, piece));
									} else {
										queue.add(new Node(ti, tj, tnode.sec+1, tnode.step, piece));
									}
									visited[ti][tj][piece][tnode.step] = true;
								}
							}
						}
					}
				} else {
					// 다른 말일 경우 방문체크만 하고 말을 바꿔줌
					if(!visited[tnode.r][tnode.c][piece][tnode.step]) {
						queue.add(new Node(tnode.r, tnode.c, tnode.sec+1, tnode.step, piece));
						visited[tnode.r][tnode.c][piece][tnode.step] = true;
					}
				}
			}
		}
		
		return -1;
	}
	
	static class Node {
		int r;
		int c;
		int p;
		int sec;
		int step;
		
		public Node(int r, int c, int sec, int step, int p) {
			this.r = r;
			this.c = c;
			this.p = p;
			this.sec = sec;
			this.step = step;
		}
		
		@Override
		public String toString() {
			return String.format("(%d,%d)%ds %dth %s", this.r, this.c, this.sec, this.step, this.p == 0 ? 'N' : this.p == 1 ? 'R' : 'B');
		}
	}
}




















