import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
class Main{

    public static LinkedList<Integer> addValues(LinkedList<Integer> value){
        for(int i = 1; i <= 3; i++){
            value.add(i);
        }
        return value;
    }


    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        LinkedList<Integer> numbers = new LinkedList<Integer>();
        ArrayList<Integer> arr = new ArrayList<Integer>();
        while(arr.size() < N){
            numbers = addValues(numbers);
            if(arr.size() == 0){
                arr.add(1);
            }
            else{
                int before = arr.get(arr.size()-1);
                numbers.remove(before-1);
                int element_1 = numbers.get(0);
                int element_2 = numbers.get(1);
                
                




            }

            N += 1;
        }
        
        scan.close();
    }
}
