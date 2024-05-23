fun main() {
    val year = readLine()?.toInt()

    if (year != null) {
        println(
            if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) "1"
            else "0"
        )
    }
}