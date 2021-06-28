class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val liquid = readLine()!!.split(' ').map(String::toInt).sorted()

    var leftIndex = 0
    var rightIndex = n - 1
    var l1 = 0
    var l2 = 0
    var min = 2000000000

    while (leftIndex < rightIndex) {
      val leftLiquid = liquid[leftIndex]
      val rightLiquid = liquid[rightIndex]

      val solution = leftLiquid + rightLiquid
      val abs = Math.abs(solution)
      if (abs < min) {
        l1 = leftLiquid
        l2 = rightLiquid
        min = abs
      }
      if (abs == 0) {
        break
      }

      if (solution > 0) {
        rightIndex--
      } else {
        leftIndex++
      }
    }

    println("$l1 $l2")
  }
}

fun main() {
  Solution().solution()
}