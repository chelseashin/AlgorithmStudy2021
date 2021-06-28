class Solution {
  fun solution() {
    if (Regex("^(100+1+|01)+$").containsMatchIn(readLine()!!)) {
      println("SUBMARINE")
    } else {
      println("NOISE")
    }
  }
}

fun main() {
  Solution().solution()
}