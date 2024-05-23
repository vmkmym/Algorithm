fun main() {
    val input = readLine()
    if (input != null) {
        val (a, b, c) = input.split(" ").map { it.toLong() }
        val answer = a + b + c
        println(answer)
    }
}