fun main() {
    val t = readLine()!!.toInt()
    for (i in 0 until t) {
        val (a, b) = readLine()!!.split(" ").map { it.toInt() }
        println(a + b)
    }
}