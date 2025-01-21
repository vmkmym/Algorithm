fun main() {
    val (_, X) = readLine()!!.split(" ").map { it.toInt() }
    val A = readLine()!!.split(" ").map { it.toInt()}
    val list = A.filter { it < X }
    println(list.joinToString(" "))
}