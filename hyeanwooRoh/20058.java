import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 1차 문제풀이 3시간
// 2차 문제풀이 1시간 35분

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		calc();
		System.out.println(totalIce);
		System.out.println(biggestChunk);
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, Q, len;
	static int[][] iceMap;
	static int[] L;
	static int totalIce = 0, biggestChunk = 0;
	
	// inputdata 입력
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		Q = Integer.parseInt(st.nextToken());

		len = (int) Math.pow(2, N);
		iceMap = new int[len][len];
		for (int i = 0; i < len; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < len; j++) {
				iceMap[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		L = new int[Q];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < L.length; i++) {
			L[i] = Integer.parseInt(st.nextToken());
		}
	}

	static void calc() throws IOException {
		// Q번 만큼 수행
		for (int i = 0; i < Q; i++) {
			// L크기로 격자를 나눠 회전
			rotate((int) Math.pow(2,L[i]));
			// 얼음 녹이기
			meltIce();
		}
		// 정답 구하기
		sumIce();
		measureChunk();
	}

	static void rotate(int l) {
		// 격자 크기가 1일 경우 회전할 필요가 없으므로 함수 종료
		if(l == 1) return;
		
		// 원본과 비교를 위해 임시배열 생성
		int[][] tmpArr = copyArr();
		// 격자 크기만큼 순환하며 회전 기준 좌표 생성
		for (int i = 0; i < len; i+=l) {
			for (int j = 0; j < len; j+=l) {
				// 기준 좌표로 회전
				clockworkArray(tmpArr, i, j, l);
			}
		}
		// 회전하고 녹인 임시배열을 원본에 적용
		applyArr(tmpArr);
	}
	
	static void clockworkArray(int[][] tmpArr, int si, int sj, int l) {
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < l; j++) {
				tmpArr[si+j][sj-i+l-1] = iceMap[si+i][sj+j];
			}
		}
	}
	
	static int[] di = {0, 1, 0, -1};
	static int[] dj = {-1, 0, 1, 0};
	
	static void meltIce() {
		// 얼음을 한번에 녹이기 위해 체크용 배열 생성
		int[][] checkAround = new int[len][len];
		for (int i = 0; i < iceMap.length; i++) {
			for (int j = 0; j < iceMap.length; j++) {
				if(iceMap[i][j] > 0) {
					// 4방향 탐색
					for (int d = 0; d < 4; d++) {
						int ti = i + di[d];
						int tj = j + dj[d];
						if(ti < len && ti >= 0 && tj < len && tj >= 0) {
							checkAround[ti][tj]++;
						}
					}
				}
			}
		}
		
		// 탐색 종료후 얼음이 3방향 미만인 배열 녹임
		for (int i = 0; i < checkAround.length; i++) {
			for (int j = 0; j < checkAround.length; j++) {
				if(iceMap[i][j] != 0 && checkAround[i][j] < 3) {
					iceMap[i][j]--;
				}
			}
		}
		
	}
	
	static void sumIce() {
		for (int i = 0; i < iceMap.length; i++) {
			for (int j = 0; j < iceMap.length; j++) {
				int ice = iceMap[i][j] < 0 ? 0 : iceMap[i][j];
				totalIce += ice;
			}
		}
	}
	
	static boolean[][] isVisit;
	
	// 가장 큰 덩어리를 찾기위한 함수, BFS사용
	static void measureChunk() {
		Queue<Node> queue = new LinkedList<>();
		isVisit = new boolean[len][len];
		
		for (int i = 0; i < iceMap.length; i++) {
			for (int j = 0; j < iceMap.length; j++) {
				if(iceMap[i][j] > 0 && !isVisit[i][j]) {
					queue.add(new Node(i,j));
					isVisit[i][j] = true;
					bfs(queue, 0);
				}
			}
		}
	}
	
	static void bfs(Queue<Node> queue, int tmpChunk) {
		while(!queue.isEmpty()) {
			Node tmp = queue.poll();
			tmpChunk++;
			
			for (int d = 0; d < 4; d++) {
				int ti = tmp.i + di[d];
				int tj = tmp.j + dj[d];
				if(ti < len && ti >= 0 && tj < len && tj >= 0 && iceMap[ti][tj] > 0 && !isVisit[ti][tj]) {
					queue.add(new Node(ti, tj));
					isVisit[ti][tj] = true;;
				}
			}
			
		}
		biggestChunk = Math.max(biggestChunk, tmpChunk);
	}
	
	static int[][] copyArr() {
		int[][] tmpArr = new int[len][len];
		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				tmpArr[i][j] = iceMap[i][j];
			}
		}
		return tmpArr;
	}
	static void applyArr(int[][] tmpArr) {
		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				iceMap[i][j] = tmpArr[i][j];
			}
		}
	}
	
	static class Node {
		int i;
		int j;
		
		public Node(int i, int j) {
			this.i = i;
			this.j = j;
		}
	}
}
