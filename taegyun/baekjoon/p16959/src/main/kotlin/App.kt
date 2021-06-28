import java.util.Queue
import java.util.LinkedList

val KNIGHT_DS = listOf(Coord(-2, -1), Coord(-2, 1), Coord(2, -1), Coord(2, 1),
                          Coord(-1, -2), Coord(-1, 2), Coord(1, -2), Coord(1, 2))
val BISHOP_DS = listOf(Coord(-1, -1), Coord(-1, 1), Coord(1, -1), Coord(1, 1))
val ROOK_DS = listOf(Coord(-1, 0), Coord(0, -1), Coord(1, 0), Coord(0, 1))

enum class Piece {
  Knight, Bishop, Rook
}

data class Coord(val x: Int, val y: Int) {
  operator fun plus(other: Coord) = Coord(x + other.x, y + other.y)
  operator fun times(num: Int) = Coord(x * num, y * num)

  fun isOut(max: Int) = x < 0 || x >= max || y < 0 || y >= max
}

data class PiecePath(val next: Int, val piece: Piece, val trying: Int, val count: Int, val coord: Coord) {
  companion object {
    private lateinit var visited: List<Map<Piece, MutableSet<Coord>>>

    fun initVisited(n: Int) {
      visited = List(n*n) { Piece.values().map { it to mutableSetOf<Coord>() }.toMap() }
    }

    fun isVisited(next: Int, piece: Piece, coord: Coord) = coord in visited[next-2][piece]!!
  }

  init {
    visited[next-2][piece]!! += coord
  }

  fun createAnotherPieceAtSameCoord(piece: Piece) = PiecePath(next, piece, trying+1, count+1, coord)
}

class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val lastNumber = n * n
    PiecePath.initVisited(n)

    val map = Array(n) { readLine()!!.split(" ").map(String::toInt).toIntArray() }
    val numberToCoords = mutableMapOf<Int, Coord>()
    for (y in 0 until n) {
      for (x in 0 until n) {
        numberToCoords[map[y][x]] = Coord(x, y)
      }
    }
    
    val queue: Queue<PiecePath> = LinkedList<PiecePath>().apply {
      val startCoord = numberToCoords[1]!!
      this += PiecePath(2, Piece.Knight, 0, 0, startCoord)
      this += PiecePath(2, Piece.Bishop, 0, 0, startCoord)
      this += PiecePath(2, Piece.Rook, 0, 0, startCoord)
    }

    var minCount = Int.MAX_VALUE
    while (!queue.isEmpty()) {
      val piecePath = queue.remove()!!

      // 도착 확인
      if (piecePath.next > lastNumber) {
        if (piecePath.count < minCount) {
          minCount = piecePath.count
        }
        continue
      }

      // 시도가 3이상일 경우 그냥 제외
      if (piecePath.trying >= 3) {
        continue
      }

      // 말 변경
      for (piece in Piece.values()) {
        if (piece == piecePath.piece || PiecePath.isVisited(piecePath.next, piece, piecePath.coord)) {
          continue
        }
        queue += piecePath.createAnotherPieceAtSameCoord(piece)
      }

      when (piecePath.piece) {
        Piece.Knight -> {
          for (d in KNIGHT_DS) {
            val nextCoord = piecePath.coord + d
            if (nextCoord.isOut(n)) {
              continue
            }
            if (numberToCoords[piecePath.next]!! == nextCoord) {
              if (!PiecePath.isVisited(piecePath.next+1, piecePath.piece, nextCoord)) {
                queue += PiecePath(piecePath.next+1, piecePath.piece, 0, piecePath.count+1, nextCoord)
              }
            } else {
              if (!PiecePath.isVisited(piecePath.next, piecePath.piece, nextCoord)) {
                queue += PiecePath(piecePath.next, piecePath.piece, piecePath.trying+1, piecePath.count+1, nextCoord)
              }
            }
          }
        }
        Piece.Bishop -> {
          for (d in BISHOP_DS) {
            var offset = 0
            while (true) {
              val nextCoord = piecePath.coord + d * offset
              offset++
              if (nextCoord.isOut(n)) {
                break
              }
              if (numberToCoords[piecePath.next]!! == nextCoord) {
                if (!PiecePath.isVisited(piecePath.next+1, piecePath.piece, nextCoord)) {
                  queue += PiecePath(piecePath.next+1, piecePath.piece, 0, piecePath.count+1, nextCoord)
                }
              } else {
                if (!PiecePath.isVisited(piecePath.next, piecePath.piece, nextCoord)) {
                  queue += PiecePath(piecePath.next, piecePath.piece, piecePath.trying+1, piecePath.count+1, nextCoord)
                }
              }
            }
          }
        }
        Piece.Rook -> {
          for (d in ROOK_DS) {
            var offset = 0
            while (true) {
              val nextCoord = piecePath.coord + d * offset
              offset++
              if (nextCoord.isOut(n)) {
                break
              }
              if (numberToCoords[piecePath.next]!! == nextCoord) {
                if (!PiecePath.isVisited(piecePath.next+1, piecePath.piece, nextCoord)) {
                  queue += PiecePath(piecePath.next+1, piecePath.piece, 0, piecePath.count+1, nextCoord)
                }
              } else {
                if (!PiecePath.isVisited(piecePath.next, piecePath.piece, nextCoord)) {
                  queue += PiecePath(piecePath.next, piecePath.piece, piecePath.trying+1, piecePath.count+1, nextCoord)
                }
              }
            }
          }
        }
      }
    }

    println(minCount)
  }
}

fun main() {
  Solution().solution()
}