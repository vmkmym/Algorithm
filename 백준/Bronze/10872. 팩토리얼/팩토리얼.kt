fun factorial(n: Int): Long {
    if (n == 0) {
        return 1
    }
    return n * factorial(n - 1)
}

fun main() {
    val n = readLine()!!.toInt()
    println(factorial(n))
}