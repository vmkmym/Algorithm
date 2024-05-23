import kotlin.math.abs

fun main() {
    val (n, m) = readLine()!!.split(" ").map { it.toLong() }
    println(abs(n - m))
}