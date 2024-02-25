class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val n = friends.size

        // 친구들의 이름을 인덱스로 변환한 맵을 생성
        val friendToIndex = friends.withIndex().associate { it.value to it.index }

        // 친구들끼리 주고 받은 선물을 저장할 2차원 리스트 초기화
        val giftCounts = Array(n) { IntArray(n) }

        // 주고 받은 선물 기록
        for (gift in gifts) {
            val (giver, receiver) = gift.split(" ")
            val i = friendToIndex[giver]!!
            val j = friendToIndex[receiver]!!
            giftCounts[i][j]++
        }

        // 다음 달에 줄 선물의 개수를 저장할 배열
        val giftsNextMonth = IntArray(n)

        // 다음 달에 줄 선물의 개수 계산
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i != j && giftCounts[i][j] > giftCounts[j][i]) {
                    giftsNextMonth[i]++
                } else if (i != j && giftCounts[i][j] == giftCounts[j][i]) {
                    val giveCountI = giftCounts[i].sum() - giftCounts.sumBy { it[i] }
                    val giveCountJ = giftCounts[j].sum() - giftCounts.sumBy { it[j] }
                    if (giveCountI > giveCountJ) {
                        giftsNextMonth[i]++
                    }
                }
            }
        }

        return giftsNextMonth.maxOrNull() ?: 0
    }
}

// Kotlin스럽게 Refactoring
class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val n = friends.size
        val friendToIndex = friends.withIndex().associate { it.value to it.index }
        val giftCounts = Array(n) { IntArray(n) }

        gifts.forEach { gift ->
            gift.split(" ").let { (giver, receiver) ->
                friendToIndex[giver]?.let { i ->
                    friendToIndex[receiver]?.let { j ->
                        giftCounts[i][j]++
                    }
                }
            }
        }

        val giftsNextMonth = IntArray(n)

        (0 until n).forEach { i ->
            (0 until n).forEach { j ->
                if (i != j) {
                    when {
                        giftCounts[i][j] > giftCounts[j][i] -> giftsNextMonth[i]++
                        giftCounts[i][j] == giftCounts[j][i] -> {
                            val giveCountI = giftCounts[i].sum() - giftCounts.sumBy { it[i] }
                            val giveCountJ = giftCounts[j].sum() - giftCounts.sumBy { it[j] }
                            if (giveCountI > giveCountJ) giftsNextMonth[i]++
                        }
                    }
                }
            }
        }

        return giftsNextMonth.maxOrNull() ?: 0
    }
}