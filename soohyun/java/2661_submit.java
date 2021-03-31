import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static boolean flag = false;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        backtracking("", N);
    }

    private static void backtracking(String result, int N) {
        if (N  == 0) {
            if (flag == false){
                System.out.println(result);
                flag = true;
            }
            return;

        } else {
            for (int i = 1; i <= 3; i++) {
                if (check(result + i)) {
                    backtracking(result + i, N-1);
                }
            }
        }
    }

    private static boolean check(String s) {
        int length = s.length() / 2;
        for (int i = 1; i <= length; i++) {
            if (s.substring(s.length() - i)
                 .equals(s.substring(s.length() - 2 * i, 
                                     s.length() - i))) {
                return false;
            }
        }
        return true;
    }
}
