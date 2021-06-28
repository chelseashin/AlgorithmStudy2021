class Solution {
  fun isPromising(queens: IntArray, row: Int): Boolean {
    val me = queens[row]
    for (i in 0..row-1) {
      val other = queens[i]
      val diff = row - i
      // 열이 겹치는지, / 대각선으로 겹치는지, \ 대각선으로 겹치는지
      if (me == other || other - me == diff || me - other == diff) {
        return false
      }
    }
    return true
  }

  fun find(queens: IntArray, row: Int, n: Int): Int {
    if (row == n) {
      return 1
    }

    var cases = 0

    for (col in 0 until n) {
      queens[row] = col
      if (this.isPromising(queens, row)) {
        cases += find(queens, row+1, n)
      }
    }

    return cases
  }

  fun solution() {
    val n = readLine()!!.toInt()
    val queens = IntArray(n) { -1 }
    val cases = find(queens, 0, n)

    println(cases)
  }
}

fun main() {
  Solution().solution()
}