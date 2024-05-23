fun main() {
    val input = readLine()
    if (input != null) {
        val a = input.toInt()
        when {
            a >= 90 -> "A"
            a >= 80 -> "B"
            a >= 70 -> "C"
            a >= 60 -> "D"
            else -> "F"
        }.let { answer ->
            println(answer)
        }
    }
}