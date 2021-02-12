import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 1시간 5분

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		solve();
		System.out.println(answer);
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, M, T;
	static int[][] plates, command;
	static int[] phead;
	static int answer;
	
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());
		plates = new int[N][M];
		command = new int[T][3];
		phead = new int[N];
		
		for (int i = 0; i < plates.length; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < plates[i].length; j++) {
				plates[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < command.length; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < command[i].length; j++) {
				command[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		br.close();
	}

	static void solve() throws IOException {
		for (int i = 0; i < command.length; i++) {
			 rotatePlates(command[i][0], command[i][1], command[i][2]);
			 setPlates();
			 removeNumber();
		}
		
		// 정답계산
		for (int i = 0; i < plates.length; i++) {
			for (int j = 0; j < plates[i].length; j++) {
				if(plates[i][j] != -1) answer += plates[i][j];
			} 
		}
	}
	
	// 원판이 회전되는 만큼 헤드 변경
	static void rotatePlates(int x, int d, int k) {
		for (int i = 0; i < plates.length; i++) {
			if((i+1)%x == 0) {
				int moveH = (d == 0) ? -k: k;
				phead[i] = (phead[i] + moveH) % M;
				if(phead[i] < 0) phead[i] += M;
			}
		}
	}
	
	// 변경된 헤드를 기준으로 원판배열 재배치
	static void setPlates() {
		for (int i = 0; i < plates.length; i++) {
			int[] tmpPlate = new int[M];
			int idx = phead[i];
			for (int j = 0; j < tmpPlate.length; j++) {
				tmpPlate[j] = plates[i][idx++]; 
				idx %= M;
			}
			
			for (int j = 0; j < tmpPlate.length; j++) {
				plates[i][j] = tmpPlate[j];
			}
		}
		
		phead = new int[N];
	}
	
	static int[] di = {1,-1,0,0};
	static int[] dj = {0,0,1,-1};
	// 일치하는 숫자 체크한 다음 제거
	static void removeNumber() {
		ArrayList<Node> list = new ArrayList<>();
		double total = 0;
		int cnt = 0;
		
		// 일단 주변에 같은 숫자가 있을 경우 리스트에 추가
		for (int i = 0; i < plates.length; i++) {
			for (int j = 0; j < plates[i].length; j++) {
				if(plates[i][j] != -1) {
					for (int d = 0; d < 4; d++) {
						int ti = i + di[d];
						int tj = (j + dj[d])%M;
						
						if(tj < 0) tj += M;
						if(ti < N && ti >= 0 && plates[i][j] == plates[ti][tj]) {
							list.add(new Node(i, j));
						}
					}
					total += plates[i][j];
					cnt++;
				}
			}
		}
		
		if(list.size() != 0) {
			// 주변에 같은 숫자가 있는 경우 찾아서 제거
			for (int i = 0; i < list.size(); i++) {
				Node tmpNode = list.get(i);
				plates[tmpNode.r][tmpNode.c] = -1;
			}
		} else {
			// 같은 숫자가 없는 경우 평균에서 각각 +1, -1
			total /= cnt;
			for (int i = 0; i < plates.length; i++) {
				for (int j = 0; j < plates[i].length; j++) {
					if(plates[i][j] != -1) {
						if(total < plates[i][j]) {
							plates[i][j]--;
						} else if(total > plates[i][j]) {
							plates[i][j]++;
						}
					}
				}
			}
		}
	}
	
	static class Node {
		int r;
		int c;
		
		public Node(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}
}
