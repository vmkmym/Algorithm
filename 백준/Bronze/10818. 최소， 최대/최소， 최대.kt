fun main() {
    val n = readLine()!!.toInt()
    val digits = readLine()!!.split(" ").map { it.toInt() }
    println("${digits.minOrNull()} ${digits.maxOrNull()}")
}