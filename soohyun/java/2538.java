import java.util.HashSet;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Iterator;
class Paper{
    int xmin;
    int ymin;
    int xmax;
    int ymax;
    public Paper(int xmin, int ymin, int xmax, int ymax){
        this.xmin = xmin;
        this.ymin = ymin;
        this.xmax = xmax;
        this.ymax = ymax;
    }
}


class Loc{
    int x;
    int y;
    public Loc(int x, int y){
        this.x = x;
        this.y = y;
    }
}


class Main{
    public static void main(String[] args) throws IOException{
        //declare
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        int[][] paper;
        int[][] visit;
        LinkedList<Loc> queue = new LinkedList<>();
        LinkedList<Integer> areas = new LinkedList<>();
        LinkedList<Paper> squares = new LinkedList<>();
        int XMin = 0;int YMin = 0;int XMax = 0;int YMax = 0;
        //input & data processing
        String[] rawData = buf.readLine().split(" ");
        int M = Integer.parseInt(rawData[0]);
        int N = Integer.parseInt(rawData[1]);
        int K = Integer.parseInt(rawData[2]);
        paper = new int[M][N];
        visit = new int[M][N];
        for(int i = 0; i < K; i++){
            rawData = buf.readLine().split(" ");
            XMin = Integer.parseInt(rawData[1]);
            YMin = Integer.parseInt(rawData[0]);
            XMax = Integer.parseInt(rawData[3]) - 1;
            YMax = Integer.parseInt(rawData[2]) - 1;
            //System.out.println("input:"+XMin+ " "+YMin+" "+XMax+" "+YMax);
            squares.add(new Paper(XMin, YMin, XMax, YMax));
        }
        //make map
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                for(Paper square: squares){
                    if(i >= square.xmin && j <= square.ymax &&
                       i <= square.xmax && j >= square.ymin){
                            paper[i][j] = -1;
                    }
                }
            }
        }
        //debug
        /*for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                System.out.print(paper[i][j]);
            }
            System.out.println();
        }*/

        //bfs
        int[] dx = {0, 0, -1 ,1};
        int[] dy = {-1, 1, 0, 0};
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                //paper의 그린부분이거나  방문한경우
                if(paper[i][j] == -1 || visit[i][j] == 1){
                    continue;
                }
                queue.add(new Loc(i, j));
                visit[i][j] = 1;
                int size = 0;
                while(queue.size() > 0){
                    Loc curLoc = queue.removeFirst();
                    //System.out.println(curLoc.x+" "+curLoc.y);
                    size += 1;
                    for(int k = 0; k < 4; k++){
                        int x = curLoc.x + dx[k];
                        int y = curLoc.y + dy[k];
                        if(x < 0 || y < 0 || x >= M || y >= N) continue;
                        else if(paper[x][y] == -1 || visit[x][y] == 1) continue;
                        else{
                            visit[x][y] = 1;
                            queue.add(new Loc(x, y));
                            //System.out.println("add:"+x+" "+ y);
                            }
                    }
                }
                //System.out.println("size:"+ size);
                areas.add(size);
            }
        }
        System.out.println(areas.size());
        Iterator it = areas.iterator();
        System.out.print(it.next());
        while(it.hasNext()){
            System.out.print(" "+it.next());
        }
        System.out.println();
    }
}
