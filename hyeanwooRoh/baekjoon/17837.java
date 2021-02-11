import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 50분 + 50분 + 45분
// 2시간 25분
// 한번에 풀려다가 풀이설계가 이상해서 재도전
// 결국 어레이리스트로 맵을 만들어 성공

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		solve();
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, K;
	static int[][] board;
	static Piece[] pieces;
	static ArrayList<Integer>[][] boardList;

	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		board = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		boardList = new ArrayList[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				boardList[i][j] = new ArrayList<>();
			}
		}

		pieces = new Piece[K];
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			pieces[i] = new Piece(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1,
					Integer.parseInt(st.nextToken()) - 1, i);
			boardList[pieces[i].r][pieces[i].c].add(i);
		}

		br.close();
	}

	static void solve() {
		for (int t = 1; t <= 1000; t++) {
			if(spreadOnBoard()) {
				System.out.println(t);
				return ;
			}
		}
		System.out.println(-1);
	}

	static boolean spreadOnBoard() {
		for (int i = 0; i < K; i++) {
			Piece p = pieces[i];
			if (boardList[p.r][p.c].size() > 1) {
				moveChild(p);
			} else {
				movePiece(p);
			}
			
			if(over4Piece())
				return true;
		}
		
		return false;
	}
	
	static boolean over4Piece() {
		for (int i = 0; i < boardList.length; i++) {
			for (int j = 0; j < boardList[i].length; j++) {
				if(boardList[i][j].size() > 3)
					return true;
			}
		}
		
		return false;
	}

	static final int WHITE = 0;
	static final int RED = 1;
	static final int BLUE = 2;

	static int[] di = { 0, 0, -1, 1 };
	static int[] dj = { 1, -1, 0, 0 };

	static void movePiece(Piece p) {
		int pi = p.r + di[p.d];
		int pj = p.c + dj[p.d];

		if (pi >= N || pi < 0 || pj >= N || pj < 0 || board[pi][pj] == BLUE) {
			p.d = (p.d % 2 == 1) ? p.d - 1 : p.d + 1;
			pi = p.r + di[p.d];
			pj = p.c + dj[p.d];
			if (pi < N && pi >= 0 && pj < N && pj >= 0 && board[pi][pj] != BLUE) {
				handlePiece(pi, pj, p);
			}
		} else {
			handlePiece(pi, pj, p);
		}
	}

	static void handlePiece(int r, int c, Piece p) {
		boardList[p.r][p.c].remove(0);
		p.r = r;
		p.c = c;
		boardList[r][c].add(p.num);
	}

	static void moveChild(Piece p) {
		int pi = p.r + di[p.d];
		int pj = p.c + dj[p.d];

		if (pi >= N || pi < 0 || pj >= N || pj < 0 || board[pi][pj] == BLUE) {
			p.d = (p.d % 2 == 1) ? p.d - 1 : p.d + 1;
			pi = p.r + di[p.d];
			pj = p.c + dj[p.d];
			if (pi < N && pi >= 0 && pj < N && pj >= 0 && board[pi][pj] != BLUE) {
				handleChild(board[pi][pj], pi, pj, p);
			}
		} else if (board[pi][pj] == RED) {
			handleChild(RED, pi, pj, p);
		} else if (board[pi][pj] == WHITE) {
			handleChild(WHITE, pi, pj, p);
		}
	}

	static void handleChild(int color, int r, int c, Piece p) {
		int pi = p.r;
		int pj = p.c;
		int len = boardList[pi][pj].size();
		int sIdx = 0;
		
		for (int i = 0; i < boardList[pi][pj].size(); i++) {
			if(p.num == boardList[pi][pj].get(i)) {
				sIdx = i;
				break;
			}
		}
		
		if(color == RED) {
			for (int i = len - 1; i >= sIdx; i--) {
				int pieceNum = boardList[pi][pj].get(boardList[pi][pj].size() - 1);
				boardList[pi][pj].remove(boardList[pi][pj].size() - 1);
				pieces[pieceNum].r = r;
				pieces[pieceNum].c = c;
				boardList[r][c].add(pieces[pieceNum].num);
			}
		} else {
			for (int i = sIdx; i < len; i++) {
				int pieceNum = boardList[pi][pj].get(sIdx);
				boardList[pi][pj].remove(sIdx);
				pieces[pieceNum].r = r;
				pieces[pieceNum].c = c;
				boardList[r][c].add(pieces[pieceNum].num);
			}
		}
	}

	static class Piece {
		int r;
		int c;
		int d;
		int num;

		public Piece(int r, int c, int d, int num) {
			this.r = r;
			this.c = c;
			this.d = d;
			this.num = num;
		}
	}

}