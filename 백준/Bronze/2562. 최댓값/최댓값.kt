fun main() {
    // 9개의 요소를 가진 리스트를 생성하고, 각 요소를 입력받아 정수로 변환하여 저장
    val numbers = List(9) { readLine()!!.toInt() }    

    var max_number = -1
    var max_index = -1

    for (i in 0 until 9) {
        if (numbers[i] > max_number) {
            max_number = numbers[i]
            max_index = i
        }
    }

    println(max_number)
    println(max_index + 1)
}