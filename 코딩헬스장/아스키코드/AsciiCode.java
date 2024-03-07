public class AsciiCode {
    public static int asciiCode(char input) {
        return (int) input;
    }

    public static char asciiCode(int input) {
        if (input >= 0 && input <= 127) {
            return (char) input;
        } else {
            throw new IllegalArgumentException("Input must be an integer between 0 and 127");
        }
    }

    public static void main(String[] args) {
        System.out.println(asciiCode('A') == 65);
        System.out.println(asciiCode(65) == 'A');

        System.out.println(asciiCode('a') == 97);
        System.out.println(asciiCode(97) == 'a');

        System.out.println(asciiCode('4') == 52);
        System.out.println(asciiCode(52) == '4');

        System.out.println(asciiCode('0') == 48);
        System.out.println(asciiCode(48) == '0');
    }
}