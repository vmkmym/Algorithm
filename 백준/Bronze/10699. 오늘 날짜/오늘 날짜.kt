import java.time.LocalDate
import java.time.ZoneId

fun main() {
    val seoulTime = ZoneId.of("Asia/Seoul")
    val seoulDate = LocalDate.now(seoulTime)
    println(seoulDate)
}