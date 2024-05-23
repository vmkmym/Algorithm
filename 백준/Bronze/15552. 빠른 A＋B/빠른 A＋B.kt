fun main() {
    val t = readLine()!!.toInt()
    val result = ArrayList<Int>()
    for (i in 0 until t) {
        val (a, b) = readLine()!!.split(" ").map { it.toInt() }
        result.add(a + b)
    }
    println(result.joinToString("\n"))
}