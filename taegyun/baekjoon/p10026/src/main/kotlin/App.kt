class MapGrouper<T>(val n: Int, val map: List<List<T>>, val groups: List<Set<T>>) {
  private val visited = Array(n) { BooleanArray(n) }
  private var count = 0
  private var done = false

  private fun grouping(group: Set<T>, x: Int, y: Int) {
    if (x < 0 || n <= x || y < 0 || n <= y || visited[y][x]) {
      return
    }

    val item = map[y][x]
    if (item in group) {
      visited[y][x] = true
      grouping(group, x, y-1)
      grouping(group, x+1, y)
      grouping(group, x, y+1)
      grouping(group, x-1, y)
    }
  }

  fun scan(): Int {
    if (!done) {
      for (y in 0 until n) {
        for (x in 0 until n) {
          if (visited[y][x]) {
            continue
          }

          val item = map[y][x]
          val group = groups.find { item in it }!!
          count++
          grouping(group, x, y)
        }
      }
    }

    done = true
    return count
  }
}

class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val map = List(n) { readLine()!!.map { it } }

    val normal = MapGrouper(n, map, listOf(setOf('R'), setOf('G'), setOf('B'))).scan()
    val colorBlindness = MapGrouper(n, map, listOf(setOf('R', 'G'), setOf('B'))).scan()

    println("$normal $colorBlindness")
  }
}

fun main() {
  Solution().solution()
}