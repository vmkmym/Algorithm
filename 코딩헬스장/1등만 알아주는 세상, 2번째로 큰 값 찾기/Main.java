import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static Object secondLargest(Integer[] numbers) {
        if (numbers.length < 2) {
            return "Error: 주어진 정수배열의 길이가 2보다 작습니다.";
        }

        int firstNum = Integer.MIN_VALUE, secondNum = Integer.MIN_VALUE;

        for (int num : numbers) {
            if (num > firstNum) {
                secondNum = firstNum;
                firstNum = num;
            } else if (num < firstNum && num > secondNum) {
                secondNum = num;
            }
        }

        if (secondNum == Integer.MIN_VALUE) {
            return "Error: 두 번째로 큰 수가 존재하지 않습니다.";
        }

        return secondNum;
    }

    public static void main(String[] args) {
        // 테스트 케이스
        assert secondLargest(new Integer[]{5,1,52,57,13,53}).equals(53);
        // 모든 원소가 같은 경우
        assert secondLargest(new Integer[]{5, 5, 5, 5, 5}).equals("Error: 두 번째로 큰 수가 존재하지 않습니다.");
        // 원소가 하나인 경우
        assert secondLargest(new Integer[]{1}).equals("Error: 주어진 정수배열의 길이가 2보다 작습니다.");
        // 원소가 두 개인 경우
        assert secondLargest(new Integer[]{3, 3, 2, 2, 1, 1}).equals(2);
        // 음수만 존재하는 경우
        assert secondLargest(new Integer[]{-1, -2, -3, -4, -5}).equals(-2);
        // 음수와 양수가 섞여 있는 경우
        assert secondLargest(new Integer[]{-1, 2, -3, 4, -5}).equals(2);
        System.out.println("All test cases passed");
    }
}