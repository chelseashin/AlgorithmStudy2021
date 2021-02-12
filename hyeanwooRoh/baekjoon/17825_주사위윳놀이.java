import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		init();
		solve();
		out();
	}
	
	private static int ans;
	private static int[] dice = new int[10];
	
	private static void init() throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		ans = 0;
		for(int i=0; i < 10; i++) {
			dice[i] = Integer.parseInt(st.nextToken());
		}
		br.close();
	}
	
	private static int[][] jump = {
		{0,1,2,3,4,5},
		{2,2,3,4,5,6},
		{4,3,4,5,6,7},
		{6,4,5,6,7,8},
		{8,5,6,7,8,9},
		{10,21,22,23,29,30},
		{12,7,8,9,10,11},
		{14,8,9,10,11,12},
		{16,9,10,11,12,13},
		{18,10,11,12,13,14},
		{20,24,25,29,30,31},
		{22,12,13,14,15,16},
		{24,13,14,15,16,17},
		{26,14,15,16,17,18},
		{28,15,16,17,18,19},
		{30,26,27,28,29,30},
		{32,17,18,19,20,32},
		{34,18,19,20,32,32},
		{36,19,20,32,32,32},
		{38,20,32,32,32,32},
		{40,32,32,32,32,32},
		{13,22,23,29,30,31},
		{16,23,29,30,31,20},
		{19,29,30,31,20,32},
		{22,25,29,30,31,20},
		{24,29,30,31,20,32},
		{28,27,28,29,30,31},
		{27,28,29,30,31,20},
		{26,29,30,31,20,32},
		{25,30,31,20,32,32},
		{30,31,20,32,32,32},
		{35,20,32,32,32,32},
		{0,32,32,32,32,32}
	};

	private static void solve() {
		for(int bit=0; bit < (1 << 20); bit++) {
			int score = 0;
			int[] horse = new int[4];
			boolean[] using = new boolean[35];
			
			for(int step=0; step < 10; step++) {
				int marker = (bit >> (step*2)) & 0x3;
				int nextMove = jump[horse[marker]][dice[step]];
				int getScore = jump[nextMove][0];
				
				if(using[nextMove] && nextMove > 0 && nextMove != 32) {
					break;
				} else {
					using[horse[marker]] = false;
					using[nextMove] = true;
					score += getScore;
					horse[marker] = nextMove;
				}
			}
			ans = Math.max(ans, score);
		}
	}
	
	private static void out() throws Exception {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.append(String.valueOf(ans));
		bw.flush();
		bw.close();
	}
}