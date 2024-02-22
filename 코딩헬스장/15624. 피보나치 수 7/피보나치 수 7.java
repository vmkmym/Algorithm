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

// 메모리, 시간 개선 코드
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    System.out.println(fibonacci(n)); 
  }

  public static long fibonacci(int n) {
    if (n < 0) return 0;
    
    long first = 0; 
    long second = 1;
    for (int i = 1; i <= n; i++) {
      long temp = (first + second) % 1000000007;
      first = second;
      second = temp;
    }
    return first;
  }

}