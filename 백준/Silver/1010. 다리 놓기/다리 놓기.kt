import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val check = Array(30) { IntArray(30) }

    repeat(n) {
        val (b, a) = br.readLine().split(" ").map { it.toInt() }
        println(
            when {
                a == 0 || b == 0 -> 0
                a >= b -> combination(a, b, check)
                else -> combination(b, a, check)
            }
        )
    }
}

fun combination(a: Int, b: Int, check: Array<IntArray>): Int =
    when {
        a == b || b == 0 -> 1
        check[a][b] != 0 -> check[a][b]
        else -> {
            check[a][b] = combination(a - 1, b - 1, check) + combination(a - 1, b, check)
            check[a][b]
        }
    }