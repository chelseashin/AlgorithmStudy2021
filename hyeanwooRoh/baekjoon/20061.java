import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 2시간 22분 풀던중 블럭을 옮기는 부분에서 문제가 있어서 다시 품 
// moveblock함수가 계속 어그러짐
// 큐 => 큐,어레이리스트 => 큐 => 커스텀 객체 
// +1시간 43분 
// 반례도 다 맞는데 틀림 포기

public class Main {
	public static void main(String[] args) throws Exception {
		init();
		solve();
		System.out.println(score);
		System.out.println(totalBlock);
	}

	static BufferedReader br;
	static StringTokenizer st;
	static int N, score, totalBlock;
	static int[][] board;
	static Block[] blocks;

	static final int BLUE = 0;
	static final int GREEN = 1;

	static void init() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[10][10];

		blocks = new Block[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			blocks[i] = new Block(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
					Integer.parseInt(st.nextToken()), i+1);
		}

		score = 0;
		totalBlock = 0;
		br.close();
	}

	static void solve() throws IOException {
		for (int i = 0; i < N; i++) {
			moveBlock(blocks[i]);
			removeFullBlock();
			checkPaleBoard();
		}
		getLeftedBlock();
	}

	
	static void moveBlock(Block curBlock) {
		Block blueBlock = new Block(curBlock.t,0,0,curBlock.num);
		Block greenBlock = new Block(curBlock.t,0,0,curBlock.num);
		
		int br = curBlock.r;
		int bc = curBlock.c;
		// move to blue
		for (int j = 4; j < 10; j++) {
			if(isBoardEmpty(BLUE, br, j, curBlock.t)) {
				blueBlock.r = br;
				blueBlock.c = j;
			} else {
				break;
			}
		}
		// move to green
		for (int i = 4; i < 10; i++) {
			if(isBoardEmpty(GREEN, i, bc, curBlock.t)) {
				greenBlock.r = i;
				greenBlock.c = bc;
			} else {
				break;
			}
		}
		
		putBlock(blueBlock);
		putBlock(greenBlock);
	}
	
	static boolean isBoardEmpty(int color, int i, int j, int t) {
		if(color == BLUE) {
			if(t == 1) {
				return board[i][j] == 0;
			} else if(t == 2) {
				return j < 9 && board[i][j] == 0 && board[i][j+1] == 0;
			} else if(t == 3) {
				return board[i][j] == 0 && board[i+1][j] == 0;
			}
		}
		
		if(color == GREEN) {
			if(t == 1) {
				return board[i][j] == 0;
			} else if(t == 2) {
				return board[i][j] == 0 && board[i][j+1] == 0;
			} else if(t == 3) {
				return i < 9 && board[i][j] == 0 && board[i+1][j] == 0;
			}
		}
		
		return false;
	}
	
	static void putBlock(Block block) {
		int i = block.r;
		int j = block.c;
		int t = block.t;
		int num = block.num;
		if(t == 1) {
			board[i][j] = num;
		} else if(t == 2) {
			board[i][j] = num;
			board[i][j+1] = num;
		} else if(t == 3) {
			board[i][j] = num;
			board[i+1][j] = num;
		}
	}

	static void removeFullBlock() {
		// remove blue
		for (int j = 9; j > 3; j--) {
			if (isColFull(j)) {
				for (int i = 0; i < 4; i++) {
					board[i][j] = 0;
				}
				for (int j2 = j; j2 > 3; j2--) {
					for (int i = 0; i < 4; i++) {
						int tmp = board[i][j2];
						board[i][j2] = board[i][j2-1];
						board[i][j2-1] = tmp;
					}
				}
				score++;
				j++;
			}
		}

		// remove green
		for (int i = 9; i > 3; i--) {
			if (isRowFull(i)) {
				for (int j = 0; j < 4; j++) {
					board[i][j] = 0;
				}
				for (int i2 = i; i2 > 3; i2--) {
					for (int j = 0; j < 4; j++) {
						int tmp = board[i2][j];
						board[i2][j] = board[i2-1][j];
						board[i2-1][j] = tmp;
					}
				}
				score++;
				i++;
			}
		}
	}
	

	static boolean isColFull(int j) {
		for (int i = 0; i < 4; i++) {
			if (board[i][j] == 0)
				return false;
		}
		return true;
	}

	static boolean isRowFull(int i) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == 0)
				return false;
		}
		return true;
	}

	static void checkPaleBoard() {
		int exceedBlueCnt = 0;
		// check blue
		for (int j = 4; j < 6; j++) {
			for (int i = 0; i < 3; i++) {
				if(board[i][j] != 0) {
					exceedBlueCnt++;
					break;
				}
			}
		}
		for (int j = 9 - exceedBlueCnt; j > 3; j--) {
			for (int i = 0; i < 4; i++) {
				board[i][j+exceedBlueCnt] = board[i][j];
			}
		}
		for (int j2 = 4; j2 < 6; j2++) {
			for (int i2 = 0; i2 < 4; i2++) {
				board[i2][j2] = 0;
			}
		}
		
		int exceedGreenCnt = 0;
		// check green
		for (int i = 4; i < 6; i++) {
			for (int j = 0; j < 3; j++) {
				if(board[i][j] != 0) {
					exceedGreenCnt++;
					break;
				}
			}
		}
		for (int i = 9 - exceedGreenCnt; i > 3; i--) {
			for (int j = 0; j < 4; j++) {
				board[i+exceedGreenCnt][j] = board[i][j];
			}
		}
		for (int i2 = 4; i2 < 6; i2++) {
			for (int j2 = 0; j2 < 4; j2++) {
				board[i2][j2] = 0;
			}
		}
	}
	
	static void getLeftedBlock() {
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				if(board[i][j] != 0) {
					totalBlock++;
				}
			}
		}
	}

	static class Block {
		int t;
		int r;
		int c;
		int num;

		public Block(int t, int r, int c, int n) {
			this.t = t;
			this.r = r;
			this.c = c;
			this.num = n;
		}
	}

	static void print() {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (i > 3 && j > 3) {
					continue;
				} else if(i < 4 && j < 4){
					System.out.print("- ");
					continue;
				}
				System.out.print(board[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
}

/*
9
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
3 0 3
*/