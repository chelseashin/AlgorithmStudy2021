import java.util.ArrayList;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> inputs = new ArrayList<>();
        int max = -1;
        while(true){
            int num = Integer.parseInt(buf.readLine());
            if(num == 0) break;
            if(num > max) max = num;
            inputs.add(num);
        }

        int[] primeNums = new int[max + 1];
        int primeNum = 2;
        primeNums[0] = -1;
        primeNums[1] = -1;

        //primeNums계산
        while(primeNum * primeNum <= max){
            for(int i = 2; primeNum * i < max + 1; i++){
                primeNums[primeNum * i] = -1;
            }
            primeNum += 1;
        }

        //순회회가며 값이 존재하는지 확인
        for(Integer number: inputs){
            int primeNumA = -1;
            int primeNumB = -1;
            for(int i = 2; i < number/2 + 1; i++){
                if(primeNums[i] == 0 && primeNums[number - i] == 0){
                        primeNumA = i;
                        primeNumB = number - i;
                        break;
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
