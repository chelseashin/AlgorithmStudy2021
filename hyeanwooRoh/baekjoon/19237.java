import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 1시간 39분
// 한번에 통과

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		calc();
		System.out.println(sec);
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, M, K;
	static Queue<Shark> sharks;
	static Smell[][] sea;
	static int[][][] sharkDirs;
	static int sec;
	
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		sharks = new LinkedList<>();
		sea = new Smell[N][N];
		Shark[] tmpArr = new Shark[M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int tmpSharkNum = Integer.parseInt(st.nextToken());
				if(tmpSharkNum != 0) {
					tmpArr[tmpSharkNum-1] = new Shark(tmpSharkNum, i, j);
					sea[i][j] = new Smell(tmpSharkNum, K);
				} else {
					sea[i][j] = new Smell(0,0);
				}
			}
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			tmpArr[i].setDir(Integer.parseInt(st.nextToken()));
			sharks.add(tmpArr[i]);
		}
		
		sharkDirs = new int[M+1][5][5];
		for (int i = 1; i <= M; i++) {
			for (int j = 1; j <= 4; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k = 1; k <= 4; k++) {
					sharkDirs[i][j][k] = Integer.parseInt(st.nextToken());
				}
			}
		}
		
		sec = 0;
	}

	static void calc() throws IOException {
		while(sharks.size() > 1){
			sharkSwim();
			sec++;
			if(sec > 1000) {
				sec = -1;
				return;
			}
		}
	}

	static void sharkSwim() {
		ArrayList<Shark>[][] list = new ArrayList[N][N];
		
		while(!sharks.isEmpty()) {
			Shark curShark = sharks.poll();
			int[] loc = checkAround(curShark);
			curShark.r = loc[0];
			curShark.c = loc[1];
			curShark.d = loc[2];
			if(list[loc[0]][loc[1]] == null) {
				list[loc[0]][loc[1]] = new ArrayList<Shark>();
			}
			list[loc[0]][loc[1]].add(curShark);
		}
		
		reduceSmells();  

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if(list[i][j] != null) {
					if(list[i][j].size() > 1) {
						// remove shark
						while(list[i][j].size() != 1) {
							if(list[i][j].get(0).num > list[i][j].get(1).num) {
								list[i][j].remove(0);
							} else {
								list[i][j].remove(1);
							}
						}
					}
					sharks.add(list[i][j].get(0));
				}
			}
		}

		addSmells(list);
	}
	
	static int[] di = {0,-1,1,0,0};
	static int[] dj = {0,0,0,-1,1};
	
	static int[] checkAround(Shark s) {
		int[] sd = sharkDirs[s.num][s.d];
		// 빈칸
		for (int i = 1; i < 5; i++) {
			int ti = s.r + di[sd[i]];
			int tj = s.c + dj[sd[i]];
			if(ti < N && ti >= 0 && tj < N && tj >= 0 && sea[ti][tj].sNum == 0) {
				int[] loc = {ti,tj,sd[i]};
				return loc;
			}
		}
		// 자기 냄새
		for (int i = 1; i < 5; i++) {
			int ti = s.r + di[sd[i]];
			int tj = s.c + dj[sd[i]];
			if(ti < N && ti >= 0 && tj < N && tj >= 0 && sea[ti][tj].sNum == s.num) {
				int[] loc = {ti,tj,sd[i]};
				return loc;
			}
		}
		return null;
	}
	
	static void reduceSmells() {
		for (int i = 0; i < sea.length; i++) {
			for (int j = 0; j < sea[i].length; j++) {
				if(sea[i][j].sNum != 0) {
					sea[i][j].k--;
					if(sea[i][j].k == 0) sea[i][j].sNum = 0;
				}
			}
		}
	}
	
	static void addSmells(ArrayList<Shark>[][] list) {
		for (int i = 0; i < list.length; i++) {
			for (int j = 0; j < list[i].length; j++) {
				if(list[i][j] != null) {
					sea[i][j] = new Smell(list[i][j].get(0).num, K);
				}
			}
		}
	}
	
	static class Smell {
		int sNum;
		int k;
		
		public Smell(int sNum, int k) {
			this.sNum = sNum;
			this.k = k;
		}
		
		@Override
		public String toString() {
			return String.format("S:%d|k:%d", this.sNum, this.k);
		}
	}
	
	static class Shark {
		int num;
		int r;
		int c;
		int d;
		
		public Shark(int num, int r, int c) {
			this.num = num;
			this.r = r;
			this.c = c;
		}
		
		public void setDir(int d) {
			this.d = d;
		}

		@Override
		public String toString() {
			return String.format("%d:(%d,%d)/%d", this.num, this.r, this.c, this.d);
		}
		
	}

}
