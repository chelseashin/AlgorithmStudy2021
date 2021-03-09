import java.util.HashSet;
import java.util.LinkedList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Paper{
    int xin;
    int yin;
    int xax;
    int yax;
    public Paper(int xin, int yin, int xax, int yax){
        this.xin = xin;
        this.yin = yin;
        this.xax = xax;
        this.yax = yax;
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
    public static void main(String[] args){
        //declare
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Loc> blankAxis = new HashSet<>();
        LinkedList<Loc> queue = new LinkedList<>();
        LinkedList<Loc> areas = new LinkedList<>();
        LinkedList<Paper> papers = new LinkedList<>();
        int XMin = 0;int YMin = 0;int XMax = 0;int YMax = 0;
        //input & data processing
        String[] rawData = buf.readline().split()
        int M = Integer.parseInt(rawData[0]);
        int N = Integer.parseInt(rawData[1]);
        int K = Integer.parseInt(rawData[2]);
        for(int i = 0; i < K; i++){
            rawData = buf.readline.split();
            XMin = Integer.parseInt(rawData[1]);
            YMin = Integer.parseInt(rawData[0]);
            XMax = Integer.parseInt(rawData[3]) - 1;
            YMax = Integer.parseInt(rawData[2]) - 1;
            paper.add(new Paper(XMin, YMin, XMax, YMax));
        }

        for(int i = 0; i < N-1; i++){
            for(int j = 0; j < M-1; j++){
                for(paper: papers){
                    if((i < paper.xin || j > paper.yax) ||
                       (i > paper.xax || j < paper.xin)){
                            blankAxis.add(new Loc(x, y));
                       }
                }
            }
        }

        //bfs
        while(blankAxis.size() > 0){
            blankAxis.remove
            while(queue.size() > 0){
            }
        }
    }
}
