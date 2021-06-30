data class MeltingCoord(val x: Int, val y: Int, val melt: Int)

class Solution {
  fun visiteIceBerge(map: Array<IntArray>, visited: Array<BooleanArray>, x: Int, y: Int, n: Int, m: Int) {
    visited[y][x] = true

    // 상
    if (y-1 >= 0 && !visited[y-1][x] && map[y-1][x] > 0) {
      visiteIceBerge(map, visited, x, y-1, n, m)
    }
    // 하
    if (y+1 < n && !visited[y+1][x] && map[y+1][x] > 0) {
      visiteIceBerge(map, visited, x, y+1, n, m)
    }
    // 좌
    if (x-1 >= 0 && !visited[y][x-1] && map[y][x-1] > 0) {
      visiteIceBerge(map, visited, x-1, y, n, m)
    }
    // 우
    if (x+1 < m && !visited[y][x+1] && map[y][x+1] > 0) {
      visiteIceBerge(map, visited, x+1, y, n, m)
    }
  }

  fun countIceberg(map: Array<IntArray>, n: Int, m: Int): Int {
    val visited = Array(n) { BooleanArray(m) { false } }
    var count = 0

    for (y in 0 until n) {
      for (x in 0 until m) {
        if (!visited[y][x] && map[y][x] > 0) {
          visiteIceBerge(map, visited, x, y, n, m)
          count++
        } else {
          visited[y][x] = true
        }
      }
    }

    return count
  }

  fun melt(map: Array<IntArray>, n: Int, m: Int) {
    val shouldMelt = mutableListOf<MeltingCoord>()

    for (y in 0 until n) {
      for (x in 0 until m) {
        if (map[y][x] == 0) {
          continue
        }

        var melt = 0
        // 상
        if (y-1 >= 0 && map[y-1][x] == 0) {
          melt++
        }
        // 하
        if (y+1 < n && map[y+1][x] == 0) {
          melt++
        }
        // 좌
        if (x-1 >= 0 && map[y][x-1] == 0) {
          melt++
        }
        // 우
        if (x+1 < m && map[y][x+1] == 0) {
          melt++
        }

        if (melt > 0) {
          shouldMelt.add(MeltingCoord(x, y, melt))
        }
      }
    }

    for ((x, y, melt) in shouldMelt) {
      var remain = map[y][x] - melt
      if (remain < 0) {
        remain = 0
      }
      map[y][x] = remain
    }
  }

  fun solution() {
    val (n, m) = readLine()!!.split(' ').map(String::toInt)
    var map = Array(n) { readLine()!!.split(' ').map(String::toInt).toIntArray() }

    var year = 0
    while (true) {
      val count = countIceberg(map, n, m)
      if (count == 0) {
        year = 0
        break
      } else if (count > 1) {
        break
      }

      melt(map, n, m)
      year++
    }

    println(year)
  }
}

fun main() {
  Solution().solution()
}