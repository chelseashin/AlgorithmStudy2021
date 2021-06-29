import kotlin.text.toCharArray

enum class Dir {
  UP, DOWN, LEFT, RIGHT, NONE
}

data class Point(val x: Int, val y: Int)
data class StartingPoint(val point: Point, val dir: Dir)

class Solution {
  fun getNextDir(block: Char, inDir: Dir): Dir = when(block) {
    '|' -> when (inDir) {
      Dir.UP -> Dir.UP
      Dir.DOWN -> Dir.DOWN
      else -> throw IllegalArgumentException()
    }
    '-' -> when (inDir) {
      Dir.LEFT -> Dir.LEFT
      Dir.RIGHT -> Dir.RIGHT
      else -> throw IllegalArgumentException()
    }
    '+' -> when (inDir) {
      Dir.UP -> Dir.UP
      Dir.DOWN -> Dir.DOWN
      Dir.LEFT -> Dir.LEFT
      Dir.RIGHT -> Dir.RIGHT
      else -> throw IllegalArgumentException()
    }
    '1' -> when (inDir) {
      Dir.LEFT -> Dir.DOWN
      Dir.UP -> Dir.RIGHT
      else -> throw IllegalArgumentException()
    }
    '2' -> when (inDir) {
      Dir.DOWN -> Dir.RIGHT
      Dir.LEFT -> Dir.UP
      else -> throw IllegalArgumentException()
    }
    '3' -> when (inDir) {
      Dir.RIGHT -> Dir.UP
      Dir.DOWN -> Dir.LEFT
      else -> throw IllegalArgumentException()
    }
    '4' -> when (inDir) {
      Dir.RIGHT -> Dir.DOWN
      Dir.UP -> Dir.LEFT
      else -> throw IllegalArgumentException()
    }
    else -> throw IllegalArgumentException()
  }

  fun solution() {
    val (r, c) = readLine()!!.split(' ').map(String::toInt)
    val map = Array(r) { readLine()!!.toCharArray() }

    val canUp = charArrayOf('|', '+', '1', '4')
    val canDown = charArrayOf('|', '+', '2', '3')
    val canLeft = charArrayOf('-', '+', '1', '2')
    val canRight = charArrayOf('-', '+', '3', '4')

    var startingPoint = StartingPoint(Point(0, 0), Dir.NONE)
    var missing = Point(0, 0)

    val getStartingPointDir: (Int, Int) -> Dir = { x, y ->
      when {
        y-1 >= 0 && map[y-1][x] in canUp -> Dir.UP
        y+1 < r && map[y+1][x] in canDown -> Dir.DOWN
        x-1 >= 0 && map[y][x-1] in canLeft -> Dir.LEFT
        x+1 < c && map[y][x+1] in canRight -> Dir.RIGHT
        else -> Dir.NONE
      }
    }

    for (y in 0..r-1) {
      for (x in 0..c-1) {
        if (map[y][x] == 'M') {
          val dir = getStartingPointDir(x, y)
          if (dir != Dir.NONE) {
            startingPoint = StartingPoint(Point(x, y), dir)
          }
        } else if (map[y][x] == 'Z') {
          val dir = getStartingPointDir(x, y)
          if (dir != Dir.NONE) {
            startingPoint = StartingPoint(Point(x, y), dir)
          }
        }
      }
    }

    var (x, y) = startingPoint.point
    var nextDir = startingPoint.dir
    while (true) {
      when (nextDir) {
        Dir.UP -> y--
        Dir.DOWN -> y++
        Dir.LEFT -> x--
        Dir.RIGHT -> x++
        else -> throw IllegalStateException()
      }
      if (map[y][x] == '.') {
        missing = Point(x, y)
        break
      }
      nextDir = getNextDir(map[y][x], nextDir)
    }

    var up = missing.y-1 >= 0 && map[missing.y-1][missing.x] in canUp
    var down = missing.y+1 < r && map[missing.y+1][missing.x] in canDown
    var left = missing.x-1 >= 0 && map[missing.y][missing.x-1] in canLeft
    var right = missing.x+1 < c && map[missing.y][missing.x+1] in canRight

    val theBlock = when {
      up && down && left && right -> '+'
      up && down -> '|'
      left && right -> '-'
      down && right -> '1'
      up && right -> '2'
      up && left -> '3'
      down && left -> '4'
      else -> throw IllegalStateException()
    }

    println("${missing.y+1} ${missing.x+1} $theBlock")
  }
}

fun main() {
  Solution().solution()
}