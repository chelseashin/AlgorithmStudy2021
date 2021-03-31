import java.util.Scanner;
class Solution{
    public static int numOfCount(int number){
        int count = 0;
        if(number == 0)
            return 1;
        else if (number < 0)
            return 0;
        count += numOfCount(number - 1);
        count += numOfCount(number - 2);
        count += numOfCount(number - 3);
        return count;
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        for(int i = 0; i < N; i++){
            int number = scan.nextInt();
            System.out.println(numOfCount(number));

        }
        scan.close();
    }
}
