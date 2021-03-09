import java.io.InputStreamReader;                                               
import java.io.BufferedReader;                                                  
import java.util.LinkedList;                                                    
import java.io.IOException;
import java.util.Queue;

class Place{                                                                       
    int y ;                                                                        
    int x;                                                                         
    int dis;                                                                       
    int drill;                                                                     
    public Place(int x, int y, int dis, int drill){                                
        this.y = y;                                                                
        this.x = x;                                                                
        this.dis = dis;                                                            
        this.drill = drill;                                                         
    }                                                                              
}                                                                                  
class Main{
    public static int bfs(int x, int y,int[][] visit, int[][] map, int N, int M){
    Queue<Place> q = new LinkedList<>();
    q.add(new Place(x, y, 1, 0));
    visit[x][y] = 0;
    int ans = Integer.MAX_VALUE;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    while(!q.isEmpty()){
        Place p = q.poll();
        if(p.y == N - 1 && p.x == M - 1){
            ans = p.dis;
            break;
        }
        for(int i = 0; i < 4; i++){
            int nx = p.x + dx[i];
            int ny = p.y + dy[i];

            if(ny<0 || nx < 0 || ny>=N|| nx>= M) continue;
            if(visit[nx][ny] <= p.drill) continue;
            if(map[nx][ny] == 0){
                visit[nx][ny] = p.drill;
                q.add(new Place(nx, ny, p.dis+1, p.drill));
            }
            else{
                if(p.drill == 0){
                    visit[nx][ny] = p.drill + 1;
                    q.add(new Place(nx, ny, p.dis+1, p.drill+1));
                }
            }
        }
    }
    return ans;
    }
    public static void main(String[] args) throws IOException{                                        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");                                   
        int M = Integer.parseInt(str[0]);                                              
        int N = Integer.parseInt(str[1]);                                              
        int[][] map = new int[M][N];                                                   
        int[][] visited = new int[M][N];                                               
        int ans = 0;                                                                     
        for(int i = 0; i < M; i++){                                                
            str = br.readLine().split("");                                         
            for(int j = 0; j < N; j++){                                            
                map[i][j] = Integer.parseInt(str[j]);                              
                visited[i][j] = Integer.MAX_VALUE;                                 
            }                                                                      
        }                                                                          
        ans = Integer.MAX_VALUE;                                                   
        ans = bfs(0,0, visited, map, N, M);                                                                  
        if(ans == Integer.MAX_VALUE)System.out.println(-1);
        else System.out.println(ans);                                              
    }                                                                              
} 
