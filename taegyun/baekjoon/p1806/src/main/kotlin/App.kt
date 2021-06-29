class Solution {
  fun solution() {
    val (n, s) = readLine()!!.split(' ').map(String::toInt)
    val sequence = readLine()!!.split(' ').map(String::toInt)

    var left = 0
    var right = 0
    var sum = sequence[left]
    var count = n+1

    while (left < n) {
      if (sum >= s) {
        if (right - left + 1 < count) {
          count = right - left + 1
        }
        sum -= sequence[left]
        left++
      } else {
        if (right < n-1) {
          right++
          sum += sequence[right]
        } else {
          break
        }
      }
    }

    println(if (count == n+1) 0 else count)
  }
}

fun main() {
  Solution().solution()
}