import java.util.Queue
import java.util.LinkedList

typealias GameMap = List<List<Boolean>>
typealias GameVisited = Array<Array<BooleanArray>>

data class Position(val x: Int, val y: Int, val broken: Int, val length: Int) {
  companion object {
    private val dx = listOf(-1, 0, 1, 0)
    private val dy = listOf(0, 1, 0, -1)
  }

  fun getPosibleNextPositions(map: GameMap, w: Int, h: Int, breakLimit: Int, visited: GameVisited): List<Position> {
    val nextPositions = mutableListOf<Position>()
    for (i in 0 until 4) {
      val nextX = x + dx[i]
      val nextY = y + dy[i]
      if (nextX < 0 || nextX >= w || nextY < 0 || nextY >= h) {
        continue
      }
      if (map[nextY][nextX]) { // 그냥 길
        if (visited[nextY][nextX][broken] == false) { // 간적 없음
          nextPositions += Position(nextX, nextY, broken, length + 1)
        }
      } else if (broken < breakLimit) { // 벽인데 더 뚫을 수 있음
        if (visited[nextY][nextX][broken + 1] == false) { // 간적 없음
          nextPositions += Position(nextX, nextY, broken + 1, length + 1)
        }
      }
    }
    return nextPositions
  }
}

class Solution {
  fun solution() {
    val (n, m, k) = readLine()!!.split(" ").map(String::toInt)
    val map: GameMap = List(n) { readLine()!!.toCharArray().map { it == '0' } }
    val visited: GameVisited = Array(n) { Array(m) { BooleanArray(k+1) } }
    visited[0][0][0] = true

    var min = Int.MAX_VALUE
    val queue: Queue<Position> = LinkedList<Position>().apply { 
      this += Position(0, 0, 0, 1)
    }
    while (!queue.isEmpty()) {
      val position = queue.remove()!!

      if (position.x == m - 1 && position.y == n - 1) {
        if (position.length < min) {
          min = position.length
          continue
        }
      }

      for (nextPosition in position.getPosibleNextPositions(map, m, n, k, visited)) {
        queue += nextPosition
        visited[nextPosition.y][nextPosition.x][nextPosition.broken] = true
      }
    }

    println(if (min == Int.MAX_VALUE) -1 else min)
  }
}

fun main() {
  Solution().solution()
}