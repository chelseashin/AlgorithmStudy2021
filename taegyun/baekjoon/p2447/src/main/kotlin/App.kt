fun drawStar(canvas: Array<CharArray>, n: Int, x: Int, y: Int) {
  if (n == 1) {
    canvas[y][x] = '*'
  } else {
    val nextN = n / 3
    drawStar(canvas, nextN, x, y)
    drawStar(canvas, nextN, x+nextN, y)
    drawStar(canvas, nextN, x+nextN+nextN, y)
    drawStar(canvas, nextN, x, y+nextN)
    drawStar(canvas, nextN, x+nextN+nextN, y+nextN)
    drawStar(canvas, nextN, x, y+nextN+nextN)
    drawStar(canvas, nextN, x+nextN, y+nextN+nextN)
    drawStar(canvas, nextN, x+nextN+nextN, y+nextN+nextN)
  }
}

class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val canvas = Array(n) { CharArray(n) { ' ' } }
    
    drawStar(canvas, n, 0, 0)
    
    canvas.forEach { println(it.joinToString("")) }
  }
}

fun main() {
  Solution().solution()
}