class Solution {
  fun dfs(seated: Array<BooleanArray>, visited: Array<BooleanArray>, row: Int, col: Int) {
    visited[row][col] = true
    
    // 상
    if (row - 1 >= 0 && !visited[row-1][col] && seated[row-1][col]) {
      dfs(seated, visited, row-1, col)
    }
    // 하
    if (row + 1 < 5 && !visited[row+1][col] && seated[row+1][col]) {
      dfs(seated, visited, row+1, col)
    }
    // 좌
    if (col - 1 >= 0 && !visited[row][col-1] && seated[row][col-1]) {
      dfs(seated, visited, row, col-1)
    }
    // 우
    if (col + 1 < 5 && !visited[row][col+1] && seated[row][col+1]) {
      dfs(seated, visited, row, col+1)
    }
  }

  fun isPromising(map: List<List<Char>>, seated: Array<BooleanArray>, n: Int): Boolean {
    if (n == 7) {
      val visited = Array(5) { BooleanArray(5) { false } }
      var chunk: Int = 0

      for (row in 0 until 5) {
        for (col in 0 until 5) {
          if (!visited[row][col] && seated[row][col]) {
            dfs(seated, visited, row, col)
            chunk++
            if (chunk > 1) {
              return false
            }
          } else {
            visited[row][col] = true
          }
        }
      }
    }

    var yCount: Int = 0
    for (row in 0 until 5) {
      for (col in 0 until 5) {
        if (seated[row][col] && map[row][col] == 'Y') {
          yCount++
        }
      }
    }
    return yCount < 4
  }

  fun find(map: List<List<Char>>, seated: Array<BooleanArray>, n: Int, i: Int): Int {
    if (!isPromising(map, seated, n)) {
      return 0
    } else if (n == 7) {      
      return 1
    }

    var count: Int = 0
    for (j in i until 25) {
      val row = j / 5
      val col = j % 5
      seated[row][col] = true
      count += find(map, seated, n+1, j+1)
      seated[row][col] = false
    }
    return count
  }

  fun solution() {
    val map: List<List<Char>> = List(5) { readLine()!!.toCharArray().toList() }
    val seated = Array(5) { BooleanArray(5) { false } }
    val count = find(map, seated, 0, 0)
    println(count)
  }
}

fun main() {
  Solution().solution()
}