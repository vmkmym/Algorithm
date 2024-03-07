fun asciiCode(input: Any): Any {
    return when (input) {
        is Char -> input.toInt()
        is Int -> {
            if (input in 0..127) input.toChar() else "Invalid input"
        }
        else -> "Invalid input"
    }
}

fun main() {
    println(asciiCode('A') == 65)
    println(asciiCode('a') == 97)
    println(asciiCode('0') == 48)
    println(asciiCode('4') == 52)
}

// is 키워드 : input 타입 검사하고 해당 타입으로 스마트 캐스팅
// 범위 연산자 in : input이 0~127 사이에 있는지 검사
// when 키워드 : Java의 switch 문보다 더 강력하고 유연
// 타입 안정성 : input이 Char, Int 타입이 아닌 경우 "Invalid input" 반환