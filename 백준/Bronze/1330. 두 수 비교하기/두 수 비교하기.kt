fun main() {
    val input = readLine()
    if (input != null) {
        val (a, b) = input.split(" ").map { it.toLong() }
        when {
            a > b -> ">"
            a < b -> "<"
            else -> "=="
        }.let { answer ->
            println(answer)
        }
    }
}