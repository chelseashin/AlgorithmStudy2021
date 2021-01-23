import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 2시간 26분

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		solve();
		System.out.println(fuel);
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, M, fuel;
	static int[][] map;
	static int taxiRow, taxiCol;
	static ArrayList<Guest> guests;
	static boolean isGoing;
	
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		fuel = Integer.parseInt(st.nextToken());
		
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		st = new StringTokenizer(br.readLine());
		taxiRow = Integer.parseInt(st.nextToken()) - 1;
		taxiCol = Integer.parseInt(st.nextToken()) - 1;
		
		guests = new ArrayList<Guest>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			guests.add(new Guest(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1));
		}
		
		isGoing = true;
	}

	static void solve() throws IOException {
		for (int i = 0; i < M; i++) {
			if(!isGoing) return;
			measureDist();
		 	driveTaxi();
		}
	}

	static void measureDist() {
		for (int i = 0; i < guests.size(); i++) {
			Guest tmpGuest = guests.get(i);
			tmpGuest.dist = findShortestDist(taxiRow, taxiCol, tmpGuest.sti, tmpGuest.stj);
			guests.set(i, tmpGuest);
		}
	}
	
	static int[] di = {0,0,1,-1};
	static int[] dj = {-1,1,0,0};
	
	static int findShortestDist(int stR, int stC, int dtR, int dtC) {
		if(stR == dtR && stC == dtC) return 0;
		
		boolean[][] isVisit = new boolean[N][N];
		Queue<Node> queue = new LinkedList<>();
		
		queue.add(new Node(stR, stC, 0));
		isVisit[stR][stC] = true;
		
		while(!queue.isEmpty()) {
			Node node = queue.poll();
			int tmpLen = node.len+1;
			
			for (int d = 0; d < 4; d++) {
				int ti = node.r + di[d];
				int tj = node.c + dj[d];
				
				if(ti < N && ti >= 0 && tj < N && tj >=0
						&& map[ti][tj] != 1 && !isVisit[ti][tj]) {
					if(ti == dtR && tj == dtC) {
						return tmpLen;
					}
					queue.add(new Node(ti,tj,tmpLen));
					isVisit[ti][tj] = true;
				}
			}
		}
		
		return Integer.MAX_VALUE;
	}
	
	static void driveTaxi() {
		// find Shortest Guest
		Guest curGuest = findGuest();
		if(curGuest.dist == Integer.MAX_VALUE) {
			fuel = -1;
			isGoing = false;
			return;
		}
		// checkFuel
		fuel = (fuel - curGuest.dist > 0) ? fuel - curGuest.dist : -1;  
		if(fuel == -1) {
			isGoing = false;
			return;
		}
		// driving
		int usedFuel = findShortestDist(curGuest.sti, curGuest.stj, curGuest.dti, curGuest.dtj);
		fuel = (fuel - usedFuel >= 0) ? fuel + usedFuel : -1;
		if(fuel == -1) {
			isGoing = false;
			return;
		}
		// change taxi location
		taxiRow = curGuest.dti;
		taxiCol = curGuest.dtj;
	}
	
	static Guest findGuest() {
		Guest g = guests.get(0);
		int min = g.dist;
		int gIdx = 0;
		for (int i = 1; i < guests.size(); i++) {
			Guest tg = guests.get(i);
			if(min > tg.dist) {
				min = tg.dist;
				g = tg;
				gIdx = i;
			} else if(min == tg.dist) {
				if(g.sti > tg.sti) {
					g = tg;
					gIdx = i;
				} else if(g.sti == tg.sti){
					if(g.stj > tg.stj) {
						g = tg;
						gIdx = i;
					}
				}
			}
		}
		
		guests.remove(gIdx);
		
		return g;
	}
	
	static class Node {
		int r;
		int c;
		int len;
		
		public Node(int r, int c, int l) {
			this.r = r;
			this.c = c;
			this.len = l;
		}
		
		@Override
		public String toString() {
			return String.format("(%d,%d) %d", this.r, this.c, this.len);
		}
	}
	
	static class Guest {
		int sti;
		int stj;
		int dti;
		int dtj;
		int dist;
		
		public Guest(int si, int sj, int di, int dj) {
			this.sti = si;
			this.stj = sj;
			this.dti = di;
			this.dtj = dj;
			this.dist = Integer.MAX_VALUE;
		}
		
		public void setDistance(int dist) {
			this.dist = dist;
		}
		
		@Override
		public String toString() {
			return String.format("(%d,%d) => (%d,%d) '%d'", this.sti+1, this.stj+1, this.dti+1, this.dtj+1, this.dist);
		}
	}
}
