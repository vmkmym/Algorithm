fun main() {
    val input = readLine()
    if (input != null) {
        val (a, b) = input.split(" ").map { it.toInt() }
        val answer = a - b
        println(answer)
    }
}