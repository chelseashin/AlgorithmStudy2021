import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.LinkedList;
import java.io.IOException;

class Location{
    int row;
    int col;
    int breakCount;
    int pathCount;
    public Location(int row, int col, int breakCount, int pathCount){
        this.row = row;
        this.col = col;
        this.breakCount = breakCount;
        this.pathCount = pathCount;
    }
}

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        String[] rawData = buf.readLine().split(" ");
        int row = Integer.parseInt(rawData[0]);
        int col = Integer.parseInt(rawData[1]);
        int[][] maze = new int[row][col];
        int[][] visited = new int[row][col];
        //copy array
        for(int i = 0; i < row; i++){
            String rawLine = buf.readLine();
            for(int j = 0; j < col; j++){
                maze[i][j] = rawLine.charAt(j) - 48;
                visited[i][j] = Integer.MAX_VALUE;
            }
        }


        //dfs
        LinkedList<Location> stack = new LinkedList<>();
        stack.add(new Location(0, 0, 0, 1));
        int remainBreak = 1;
        int result = Integer.MAX_VALUE;
        int[] XDirection = {-1, 1, 0, 0};
        int[] YDirection = {0, 0, -1, 1};
        visited[0][0] = 1;
        while(stack.size() > 0){
            Location location = stack.removeFirst();
            //System.out.println(location.row+" "+location.col+" "+location.pathCount);
            if(location.row >= row-1 && location.col >= col-1){
                //System.out.println("[mid] "+pathCount);
                if(location.pathCount < result){
                    result = location.pathCount;
                }
            }
            else{
                int newX = 0;
                int newY = 0;
                for(int i = 0; i < 4; i++){
                    newX = location.row + XDirection[i];
                    newY = location.col + YDirection[i];
                    if(newX < 0 || newY < 0 || newX >= row || newY >= col)
                        continue;
                    if(visited[newX][newY] <= location.breakCount) continue;
                    if(maze[newX][newY] == 1){
                        if(location.breakCount == 0){
                            visited[newX][newY] = location.breakCount + 1;
                            stack.add(new Location(newX, 
                                                   newY, 
                                                   location.breakCount+1,
                                                   location.pathCount+1));
                            //System.out.println(newX+" "+newY+" "+pathCount);
                         }
                    }
                    else{
                        visited[newX][newY] = location.breakCount;
                        stack.add(new Location(newX, 
                                               newY, 
                                               location.breakCount,
                                               location.pathCount+1));
                            //System.out.println(newX+" "+newY+" "+pathCount);
                        }

                    }

                    //System.out.println("visited: "+visited[newX][newY]+" "+newX+" "+newY);
                }
            }
        if(result == Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(result);
        }
        buf.close();
    }
}
