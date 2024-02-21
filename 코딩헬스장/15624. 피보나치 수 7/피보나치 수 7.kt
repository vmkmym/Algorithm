import java.util.Scanner

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextInt()
    println(fibonacci(n))
}

fun fibonacci(n: Int): Long {
    if (n <= 1) return n.toLong()
    var a = 0L
    var b = 1L
    for (i in 2..n) {
        val temp = b // 이전 값만 저장하기 위해 temp 변수 사용
        b = (a + b) % 1000000007 
        a = temp
    }
    return b
}