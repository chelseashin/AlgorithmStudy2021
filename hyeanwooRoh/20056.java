import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 문제 이해 1시간 18분
// 문제 끝까지 착각함 
// 문제 풀이 2시간 35분
// 참고블로그
// https://blog.naver.com/PostView.nhn?blogId=adamdoha&logNo=222133906106&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		calc();
		br.close();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int n, m, k;
	
	// inputdata 입력
	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
	}

	static void calc() throws IOException {
		// 파이어볼위주로 다루기위해 큐사용
		Queue<Fireball> queue = new LinkedList<>();
		for (int o = 0; o < m; o++) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			queue.add(new Fireball(i, j, m, s, d));
		}
		
		// 파이어볼 k번 이동
		while(k-- > 0) moveFireball(queue);
		
		int totalFireballMass = 0;
		while(!queue.isEmpty()) {
			totalFireballMass += queue.poll().mass;
		}
		System.out.println(totalFireballMass);
	}
	
	static int[] di = {-1,-1, 0, 1, 1, 1, 0,-1};
	static int[] dj = { 0, 1, 1, 1, 0,-1,-1,-1};
	static int[] evenDir = {0,2,4,6};
	static int[] oddDir = {1,3,5,7};
	
	static void moveFireball(Queue<Fireball> queue) {
		List<Fireball>[][] map = new ArrayList[n+1][n+1];
		// 1. 파이어볼 이동
		while(!queue.isEmpty()) {
			Fireball fb = queue.poll();
			int dy = (fb.row + fb.speed * di[fb.dir])%n;
			int dx = (fb.col + fb.speed * dj[fb.dir])%n;
			fb.row = (dy > 0) ? dy : dy+n;
			fb.col = (dx > 0) ? dx : dx+n;
			
			if(map[fb.row][fb.col] == null) {
				map[fb.row][fb.col] = new ArrayList<>();				
			}
			map[fb.row][fb.col].add(fb);				
		}
		
		// 2. 이동이 끝난뒤 과정
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if(map[i][j] != null) {
					if(map[i][j].size() > 1) {
						// 2-1. 파이어볼 합체
						int massSum = 0;
						int speedSum = 0;
						for (int k = 0; k < map[i][j].size(); k++) {
							massSum += map[i][j].get(k).mass;
							speedSum += map[i][j].get(k).speed;
						}
						// 2-2. 4개로 나누기
						int childMass = massSum / 5;
						int childSpeed = speedSum / map[i][j].size();
						// 2-3. 방향정하기
						boolean isSame = true;
						for (int k = 0; k < map[i][j].size()-1; k++) {
							if(map[i][j].get(k).dir%2 != map[i][j].get(k+1).dir%2) {
								isSame = false;
								break;
							}
						}
						// 4개로 나눠 큐에 저장
						int[] childDir = isSame ? evenDir : oddDir;
						for (int k = 0; k < 4; k++) {
							if(childMass == 0) break;
							queue.add(new Fireball(i, j, childMass, childSpeed, childDir[k]));
						}
					} else {
						queue.add(map[i][j].get(0));
					}
				}
			}
		}
	}
	
	static class Fireball {
		int row;
		int col;
		int mass;
		int speed;
		int dir;
		
		public Fireball(int i, int j, int m, int s, int d) {
			this.row = i;
			this.col = j;
			this.mass = m;
			this.speed = s;
			this.dir = d;
		}
	}
}

