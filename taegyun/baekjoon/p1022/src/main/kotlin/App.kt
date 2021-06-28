class Solution {
  private var max: Int = 1
  private var ox: Int = 0
  private var oy: Int = 0

  private fun updateMax(value: Int) {
    if (value > this.max) {
      this.max = value
    }
  }

  fun fill(map: Array<IntArray>, y: Int, x: Int) {
    val my = y + this.oy
    val mx = x + this.ox

    if (map[my][mx] != 0) {
      return
    }

    val n = Math.max(Math.abs(x), Math.abs(y))
    val length = 2 * n + 1
    val prevLength = 2 * (n - 1) + 1
    val startValue = prevLength * prevLength + 1
    val qLength = length - 1

    // 꼭지점 검사
    val pq = when {
      x == n && y == -n -> 1
      x == -n && y == -n -> 2
      x == -n && y == n -> 3
      x == n && y == n -> 4
      else -> 0
    }
    if (pq > 0) {
      map[my][mx] = startValue + qLength * (pq - 1) + qLength - 1
      updateMax(map[my][mx])
      return
    }

    when {
      x == n -> {
        val qOffset = n - y - 1
        val qStartValue = startValue
        map[my][mx] = qStartValue + qOffset
        updateMax(map[my][mx])
      }
      y == -n -> {
        val qOffset = n - x - 1
        val qStartValue = startValue + qLength
        map[my][mx] = qStartValue + qOffset
        updateMax(map[my][mx])
      }
      x == -n -> {
        val qOffset = y + n - 1
        val qStartValue = startValue + qLength * 2
        map[my][mx] = qStartValue + qOffset
        updateMax(map[my][mx])
      }
      y == n -> {
        val qOffset = x + n - 1
        val qStartValue = startValue + qLength * 3
        map[my][mx] = qStartValue + qOffset
        updateMax(map[my][mx])
      }
    }
  }

  fun solution() {
    val (r1, c1, r2, c2) = readLine()!!.split(" ").map(String::toInt)
    val h = Math.abs(r1 - r2) + 1
    val w = Math.abs(c1 - c2) + 1
    val map = Array(h) { IntArray(w) { 0 } }

    this.oy = -r1
    this.ox = -c1

    if (0 in r1..r2 && 0 in c1..c2) {
      map[this.oy][this.ox] = 1
    }

    for (y in r1..r2) {
      for (x in c1..c2) {
        fill(map, y, x)
      }
    }

    val digit = Math.log10(this.max.toDouble()).toInt() + 1
    for (row in map) {
      println(row.map { it.toString().padStart(digit, ' ') }.joinToString(" "))
    }
  }
}

fun main() {
  Solution().solution()
}