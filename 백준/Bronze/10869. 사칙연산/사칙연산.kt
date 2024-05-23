fun main() {
    val input = readLine()
    if (input != null) {
        val (a, b) = input.split(" ").map { it.toInt() }
        println(a + b)
        println(a - b)
        println(a * b)
        println(a / b)
        println(a % b)
    }
}