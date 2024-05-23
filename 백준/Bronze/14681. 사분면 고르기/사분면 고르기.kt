fun main() {
    val x = readLine()?.toInt()
    val y = readLine()?.toInt()

    if (x != null && y != null) {
        println(
            when {
                x > 0 && y > 0 -> 1
                x < 0 && y > 0 -> 2
                x < 0 && y < 0 -> 3
                else -> 4
            }
        )
    }
}