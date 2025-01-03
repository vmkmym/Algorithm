fun main() {
    val n = readLine()!!.toInt()
    val digits = readLine()!!.map { it.toString().toInt() }
    var totalSum = 0
    for (i in 0 until n) {
        totalSum += digits[i]
    }
    println(totalSum)
}