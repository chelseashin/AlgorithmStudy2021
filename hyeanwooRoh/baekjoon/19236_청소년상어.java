import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 2시간 43분

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		calc();
		System.out.println(max);
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static Fish[][] waterTank;
	static int max;
	
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		waterTank = new Fish[4][4];
		
		for (int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				waterTank[i][j] = new Fish(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			}
		}
		max = waterTank[0][0].n;
	}

	static void calc() throws IOException {
		Shark shark = new Shark(waterTank[0][0].n, waterTank[0][0].d, 0, 0);
		waterTank[0][0].d = 0;
		waterTank[0][0].n = 0;
		waterTank[0][0].isShark = true;
		dfs(waterTank, shark);
	}

	static int[] di = {0,-1,-1,0,1,1,1,0,-1};
	static int[] dj = {0,0,-1,-1,-1,0,1,1,1};
	
	static void dfs(Fish[][] fishs, Shark shark) {
		max = Math.max(max, shark.n);

		Fish[][] tmpArr = goFishGo(fishs);
		
		int d = shark.d;
		for (int p = 1; p <= 3; p++) {
			// 상어가 갈수있는지 확인해서 보냄
			int ti = shark.r + p*di[d];
			int tj = shark.c + p*dj[d];
			if(ti < 4 && ti >= 0 && tj < 4 && tj >= 0 && tmpArr[ti][tj].n != 0) {
				tmpArr[shark.r][shark.c].isShark = false;
				int fishN = tmpArr[ti][tj].n;
				int fishD = tmpArr[ti][tj].d;
				tmpArr[ti][tj].n = 0;
				tmpArr[ti][tj].d = 0;
				tmpArr[ti][tj].isShark = true;
				dfs(tmpArr, new Shark(shark.n+fishN, fishD, ti, tj));
				tmpArr[ti][tj].n = fishN;
				tmpArr[ti][tj].d = fishD;
				tmpArr[ti][tj].isShark = false;
			}
		}
	}
	
	static Fish[][] goFishGo(Fish[][] fishs) {
		Fish[][] tmpFishs = new Fish[4][4];
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				tmpFishs[i][j] = fishs[i][j];
			}
		}
		for (int f = 1; f <= 16; f++) {
			boolean isChecked = false;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if(tmpFishs[i][j].n == f) {
						int d = tmpFishs[i][j].d;
						for (int k = 0; k < 8; k++) {
							int ti = i + di[d];
							int tj = j + dj[d];
							if(ti < 4 && ti >= 0 && tj < 4 && tj >= 0 && !tmpFishs[ti][tj].isShark) {
								Fish tmp = tmpFishs[ti][tj];
								tmpFishs[ti][tj] = new Fish(tmpFishs[i][j].n, d);
								tmpFishs[i][j] =  tmp;
								break;
							}
							d = (d + 1 > 8) ? 1 : d + 1; 
						}
						isChecked = true;
						break;
					}
				}
				if(isChecked) break;
			}
		}
		
		return tmpFishs;
	}
	
	static class Fish {
		int n;
		int d;
		boolean isShark;
		
		public Fish(int n,int d) {
			this.n = n;
			this.d = d;
			this.isShark = false;
		}
		
		@Override
		public String toString() {
			String str = this.isShark ? "S" : "F";
			return str+"("+this.n+","+this.d+")";
		}
	}
	
	static class Shark extends Fish {
		int r;
		int c;
		
		public Shark(int n, int d, int r, int c) {
			super(n, d);
			this.r = r;
			this.c = c;
		}
		
		@Override
		public String toString() {
			return "n:"+this.n+" d:"+this.d+"("+this.r+","+this.c+")";
		}
	}
}
