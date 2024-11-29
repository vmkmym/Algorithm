import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val check = Array(30) { IntArray(30) }

    repeat(n) {
        val (b, a) = br.readLine().split(" ").map { it.toInt() }
        println(
            when {
                a == 0 || b == 0 -> 0
                a >= b -> combination(a, b, check)
                else -> combination(b, a, check)
            }
        )
    }
}

fun combination(a: Int, b: Int, check: Array<IntArray>): Int =
    when {
        a == b || b == 0 -> 1
        check[a][b] != 0 -> check[a][b]
        else -> {
            check[a][b] = combination(a - 1, b - 1, check) + combination(a - 1, b, check)
            check[a][b]
        }
    }

// Kotlin에서 IntArray의 기본값은 0이다. 그래서 명시적으로 check 배열을 0으로 설정할 필요가 없음.
// 'check[a][b] != 0'으로 확인하여 이미 계산된 값이 있는지 확인하고
// check[a][b] = combination(a - 1, b - 1, check) + combination(a - 1, b, check)으로 첫 계산 값을 저장

// 조합의 성질인 a==b, b==0일 때 1인 경우를 이용
// aCb를 계산한 적이 있는지를 dp배열 check에 저장하여 중복 계산을 방지
// combination 함수에서 기본케이스(조합의 성질)이 아닌 경우는 점화식을 이용해서 check[a][b]에 값을 저장하고 반환

// 배운 점 : 코테 풀이는 꾸준히 하자... 이런 문제도 풀이가 생각나지 않아서 헤맸다.