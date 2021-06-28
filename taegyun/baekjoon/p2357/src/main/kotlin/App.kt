class Solution {
  fun solution() {
    val (n, m) = readLine()!!.split(' ').map(String::toInt)
    val nums = IntArray(n) { readLine()!!.toInt() }
    val pairs = List(m) {
      val (a, b) = readLine()!!.split(' ').map(String::toInt)
      Pair(a, b)
    }
  }
}

fun main() {
  Solution().solution()
}