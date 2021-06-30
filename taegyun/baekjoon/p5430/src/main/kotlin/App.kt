class Solution {
  fun solution() {
    val numRegex = Regex("\\w+")

    val t = readLine()!!.toInt()
    repeat(t) {
      val functions = readLine()!!.split("")
      val n = readLine()!!.toInt()
      val nums = numRegex.findAll(readLine()!!).map(MatchResult::value).map(String::toInt).toList()
      val deque = ArrayDeque(nums)
      var reverse = false
      var error = false
      for (f in functions) {
        when (f) {
          "R" -> reverse = !reverse
          "D" -> {
            if (deque.size == 0) {
              error = true
              break
            }
            if (reverse) {
              deque.removeLast()
            } else {
              deque.removeFirst()
            }
          }
        }
      }
      if (reverse) {
        deque.reverse()
      }
      println(if (error) "error" else deque.joinToString(",", prefix = "[", postfix = "]"))
    }
  }
}

fun main() {
  Solution().solution()
}