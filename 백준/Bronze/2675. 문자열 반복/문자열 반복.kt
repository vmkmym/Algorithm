fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val (r, s) = readLine()!!.split(' ')
        val repeatCount = r.toInt()
        var p = ""
        for (i in s) {
            p += i.toString().repeat(repeatCount)
        }
        println(p)
    }
}