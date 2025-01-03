fun main() {
    val n = readLine()!!.toInt()
    val digits = readLine()!!.split(" ").map { it.toInt() }
    println("${digits.minOrNull()} ${digits.maxOrNull()}")
}

// 내 풀이 문제점
// digits.minOrNull()와 digits.maxOrNull()를 각각 호출하여 리스트를 두 번 순회함
// 시간복잡도가 O(2n)이므로 리스트를 한 번만 순회하는 O(n)보다 비효율적이다.
// 두 번의 리스트 순회로 메모리 사용량도 증가한다.

// 보완할 방법 : 리스트 한 번만 순회하기
fun main() {
    val n = readLine()!!.toInt()
    val digits = readLine()!!.split(" ").map { it.toInt() }
    
    var min = Int.MAX_VALUE // Int.MAX_VALUE로 초기화
    var max = Int.MIN_VALUE // Int.MIN_VALUE로 초기화
    
    for (digit in digits) {
        if (digit < min) min = digit
        if (digit > max) max = digit
    }
    
    println("$min $max")
}

// 시간복잡도가 O(n)이므로 효율적이다. 