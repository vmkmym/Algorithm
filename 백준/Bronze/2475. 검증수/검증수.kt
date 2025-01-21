fun main() {
    val numbers = readLine()!!.split(" ").map { it.toInt()}
    var sum = 0
    for (number in numbers) {
        sum += number * number
    }
    println(sum % 10)
}