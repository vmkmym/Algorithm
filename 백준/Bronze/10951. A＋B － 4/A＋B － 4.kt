fun main() {
    while (true) {
        val input = readLine() ?: break
        val (a, b) = input.split(" ").map { it.toInt() }
        println(a + b)
    }
}