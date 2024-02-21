import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(fibonacci(n));
    }

    public static long fibonacci(int n) {
        if (n <= 0) {
            return 0;
        }
        long[] fib = new long[n+1];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++) {
            fib[i] = (fib[i-1] + fib[i-2]) % 1000000007;
        }
        return fib[n];
    }
}