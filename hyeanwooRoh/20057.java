import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 달팽이 만드는데 40~50분
// 문제 풀이 2시간 6분

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		calc();
		System.out.println(totalSand);
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int n, totalSand;
	static int[][] board;
	
	// inputdata 입력
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		totalSand = 0;
		
		board = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}

	static int[] di = {0, 1, 0, -1};
	static int[] dj = {-1, 0, 1, 0};
	
	static void calc() throws IOException {
		int breakNum = 1;
		int d = 0;
		int spin = 1;
		int ci = n/2;
		int cj = n/2;
		// 배열 가운데에서 시작하는 달팽이방향으로 순환하는 부분
		for (int i = 0; i < 2*n-1; i++) {
			for (int j = 0; j < spin; j++) {
				// 배열 크기를 넘어서면 순환 종료
				if(breakNum==n*n) break;
				ci += di[d];
				cj += dj[d];
				// 달팽이 방향으로 순환하며 모래를 흩날리기위해 좌표와 방향 전달
				tornado(ci, cj, d);
				breakNum++;
			}
			spin += i%2;
			d = (d > 2) ? 0 : d+1;
		}
	}
	
	// 토네이도 4방향마다 각각 바로 적용하도록 하드코딩
	static double[] pct = {0.01,0.01,0.02,0.02,0.05,0.07,0.07,0.1,0.1};
	static int[][] dr = {
			{-1, 1,-2, 2, 0,-1, 1,-1, 1},
			{-1,-1, 0, 0, 2, 0, 0, 1, 1},
			{ 1,-1, 2,-2, 0, 1,-1, 1,-1},
			{ 1, 1, 0, 0,-2, 0, 0,-1,-1},
	};
	static int[][] dc = {
			{ 1, 1, 0, 0,-2, 0, 0,-1,-1},
			{-1, 1,-2, 2, 0,-1, 1,-1, 1},
			{-1,-1, 0, 0, 2, 0, 0, 1, 1},
			{ 1,-1, 2,-2, 0, 1,-1, 1,-1},
	};
	
	static void tornado(int idxR, int idxC, int d) {
		// 토네이도 방향과 맞는 흩날리는 위치 배열
		int[] rows = dr[d];
		int[] cols = dc[d];
		int sand = board[idxR][idxC];
		int pctSand = 0;
		// 퍼센트지점별로 돌며 흩날리는 모래 계산  
		for (int p = 0; p < pct.length; p++) {
			int sandR = idxR + rows[p];
			int sandC = idxC + cols[p];
			int movedSand = (int) (sand * pct[p]);
			if(sandR < n && sandR >= 0 && sandC < n && sandC >= 0) {
				// 격자 안쪽일경우 board배열에 추가
				board[sandR][sandC] += movedSand;
			} else {
				// 격자 바깥쪽일경우 totalSand에 추가
				totalSand += movedSand;
			}
			// 총 퍼센트지점에 흩날린 모래
			pctSand += movedSand;
		}
		
		// 퍼센트지점 모래를 계산하고 남은 모래 이동
		int tr = idxR + di[d];
		int tc = idxC + dj[d];
		if(tr < n && tr >= 0 && tc < n && tc >= 0) {			
			board[tr][tc] += sand - pctSand;
		} else {
			totalSand += sand - pctSand;
		}
	}
}
