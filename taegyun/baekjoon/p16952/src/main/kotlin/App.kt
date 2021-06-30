enum class Piece { Knight, Bishop, Rook }

class FindPath(val piece: Piece, val next: Int, val x: Int, val y: Int, val time: Int, val change: Int)

class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val map = List(n) { readLine()!!.split(" ").map(String::toInt) }
    val visited = Array(n) { Array(n) { Array(n*n) { IntArray(Piece.values().size) } } }
  }
}

fun main() {
  Solution().solution()
}