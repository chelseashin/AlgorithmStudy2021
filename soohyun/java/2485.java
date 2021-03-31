import java.util.Scanner;

class Main{
    public static int findMin(int[] arr){
        int value = Integer.MAX_VALUE;
        int minIdx = -1;
        for(int i = 0; i < arr.length; i++){
            if(value > arr[i]){
                value = arr[i];
                minIdx = i;
            }
        }
        return value;
    }

    public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = scan.nextInt();
    int[] diff = new int[N-1];
    int loc = -1;
    //diff에 값넣기
    for(int i = 0; i < N; i++){
        int input = scan.nextInt();
        if(loc < 0){
            loc = input;
        }
        else{
            int curLoc = input;
            diff[i-1] = curLoc - loc;
            loc = curLoc;
        }
    }
    //find minimum common divisor
    int divisor = findMin(diff);
    int diffIdx = 0;
    while(diffIdx < (diff.length-1) && divisor > 1){
        for(diffIdx = 0; diffIdx < diff.length; diffIdx++){
            if(diff[diffIdx] % divisor != 0){
                divisor -= 1;
                diffIdx = 0;
                break;}
        }
    }

    //calculate number of trees
    int numTrees = 0;
    for(int i = 0; i < diff.length; i++){
        numTrees += (diff[i]/divisor) -1;
    }
    System.out.println(numTrees);

    }
}
