import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	private static int N, M, K;

	private static int[][] earth;
	private static int[][] nutRobot;
	
	private static Queue<Tree> qBreedTrees;
	private static PriorityQueue<Tree> pqTrees;
	
	private static int[] di = {-1,-1,-1,0,0,1,1,1};
	private static int[] dj = {-1,0,1,-1,1,-1,0,1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		earth = new int[N][N];
		nutRobot = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				nutRobot[i][j] = Integer.parseInt(st.nextToken());
				earth[i][j] = 5;
			}
		}
		
		qBreedTrees = new LinkedList<>();
		pqTrees = new PriorityQueue<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			pqTrees.add(new Tree(x-1,y-1,z));
		}
		
		for (int i = 1; i <= K; i++) {
			spring();
		}
		
		System.out.println(pqTrees.size());
	}

	private static void spring() {
		Tree[] arrGrowTrees = new Tree[pqTrees.size()];
		Queue<Tree> qDeadTree = new LinkedList<>();
		
		int idx = 0;
		while(!pqTrees.isEmpty()) {
			Tree tree = pqTrees.poll();
			int ti = tree.ii;
			int tj = tree.jj;
			int ty = tree.year;
			if(earth[ti][tj] >= ty) {
				earth[ti][tj] -= ty;
				tree.year++;
				arrGrowTrees[idx++] = tree;
			}else {
				qDeadTree.add(tree);
			}
		}
		
		for (int i = 0; i < arrGrowTrees.length; i++) {
			if(arrGrowTrees[i]!=null)
				qBreedTrees.add(arrGrowTrees[i]);
		}
		summer(qDeadTree);
	}

	private static void summer(Queue<Tree> qDeadTree) {
		while(!qDeadTree.isEmpty()) {
			Tree tree = qDeadTree.poll();
			earth[tree.ii][tree.jj] += tree.year/2;
		}
		autumn();
	}

	private static void autumn() {
		while(!qBreedTrees.isEmpty()) {
			Tree tree = qBreedTrees.poll();
			if(tree.year%5==0) {
				int ti = tree.ii;
				int tj = tree.jj;
				for (int d = 0; d < 8; d++) {
					int ni = ti+di[d];
					int nj = tj+dj[d];
					if(ni>=0 && ni<N && nj>=0 && nj<N) {
						pqTrees.add(new Tree(ni,nj,1));
					}
				}
			}
			pqTrees.add(tree);
		}
		winter();
	}

	private static void winter() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				earth[i][j] += nutRobot[i][j];
			}
		}
	}

	static class Tree implements Comparable<Tree>{
		int ii;
		int jj;
		int year;
		
		public Tree(int i, int j, int y) {
			this.ii = i;
			this.jj = j;
			this.year = y;
		}
		
		@Override
		public int compareTo(Tree tree) {
			return this.year >= tree.year ? 1 : -1 ;
		}
	}
	
}