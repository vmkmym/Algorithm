fun main() {
    while (true) {
        val (a, b) = readLine()!!.split(" ").map { it.toInt() }
        if (a == 0 && b == 0) break
        println(a + b)
    }
}