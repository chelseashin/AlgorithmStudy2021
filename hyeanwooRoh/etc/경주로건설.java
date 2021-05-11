package z_etc_coding_test;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {
	
	public static void main(String[] args) throws Exception {
		int[][] board = {{0,0,0},{0,0,0},{0,0,0}};
//		int[][] board = {{0,0,0,0,0,0,0,1},{0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0},{0,0,0,0,1,0,0,0},{0,0,0,1,0,0,0,1},{0,0,1,0,0,0,1,0},{0,1,0,0,0,1,0,0},{1,0,0,0,0,0,0,0}};
//		int[][] board = {{0,0,1,0},{0,0,0,0},{0,1,0,1},{1,0,0,0}};
//		int[][] board = {{0,0,0,0,0,0},{0,1,1,1,1,0},{0,0,1,0,0,0},{1,0,0,1,0,1},{0,1,0,0,0,1},{0,0,0,0,0,0}};
		System.out.println(solution(board));
	}

	static int minValue;
	static int[] di = {-1,0,1,0};
	static int[] dj = {0,1,0,-1};
	
	public static int solution(int[][] board) {
		minValue = Integer.MAX_VALUE;
		int[][] roadValues = new int[board.length][board[0].length];
		for(int i = 0; i < roadValues.length; i++) {
			for(int j = 0; j < roadValues[0].length; j++) {
				roadValues[i][j] = Integer.MAX_VALUE;
			}
		}
		bfs(board, roadValues);
		return minValue;
	}

	private static void bfs(int[][] board, int[][] roadValues) {
		Queue<Road> queue = new LinkedList<>();
		queue.add(new Road(0,0,0,-1));
		roadValues[0][0] = 0;
		
		while(!queue.isEmpty()) {
			Road tmp = queue.poll();
			if(tmp.i == board.length-1 && tmp.j == board[0].length-1) {
				minValue = Math.min(tmp.value, minValue);
				continue;
			}
			
			for(int d = 0; d < 4; d++) {
				int ni = tmp.i + di[d];
				int nj = tmp.j + dj[d];
				int tmpValue = tmp.value + (tmp.dir == -1 || tmp.dir == d ? 100 : 600);
				if(ni >= 0 && ni < board.length && nj >= 0 && nj < board[0].length && roadValues[ni][nj] >= tmpValue && board[ni][nj] != 1) {
					queue.add(new Road(ni,nj,tmpValue,d));
					roadValues[ni][nj] = tmpValue;
				}
			}
		}
	}
	
	static class Road {
		int i;
		int j;
		int value;
		int dir;
		
		public Road(int x,int y,int v,int d) {
			this.i = x;
			this.j = y;
			this.value = v;
			this.dir = d;
		}
	}
}