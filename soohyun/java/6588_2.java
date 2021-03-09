import java.util.ArrayList;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            int number = Integer.parseInt(buf.readLine());
            if(number == 0) break;
       

        int[] primeNums = new int[number + 1];
        int primeNum = 2;
        primeNums[0] = -1;
        primeNums[1] = -1;

        //primeNums계산
        while(primeNum * primeNum <= number){
            for(int i = 2; primeNum * i < number + 1; i++){
                primeNums[primeNum * i] = -1;
            }
            primeNum += 1;
        }

        //순회회가며 값이 존재하는지 확인
            int primeNumA = -1;
            int primeNumB = -1;
            for(int i = 2; i < number/2 + 1; i++){
                int tempNumA = 0;
                int tempNumB = 0;
                if(primeNums[i] == 0 && primeNums[number - i] == 0){
                        tempNumA = i;
                        tempNumB = number - i;
                   }
                if(tempNumB - tempNumA > primeNumB - primeNumA){
                    primeNumA = tempNumA;
                    primeNumB = tempNumB;
                }
            }
            if(primeNumA == -1 && primeNumB == -1){
                System.out.println("Goldbach's conjecture is wrong.");
            }
            else{
                System.out.println(String.format("%d = %d + %d",
                                                 number, primeNumA, primeNumB));
                }
        }
        buf.close();
    
    }
}
