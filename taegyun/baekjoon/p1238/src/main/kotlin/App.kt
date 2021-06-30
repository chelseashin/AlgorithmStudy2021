typealias Paths = Map<Int, Map<Int, Int>>

data class Edge(val start: Int, val end: Int, val time: Int)

const val INFINIT = Int.MAX_VALUE.shr(4)

class Solution {
  fun dijkstra(n: Int, start: Int, paths: Paths): IntArray {
    val times = IntArray(n) { INFINIT }
    times[start-1] = 0
    val after = mutableSetOf<Int>().apply { this += start }
    val before = mutableSetOf<Int>().apply { this += 1..n; this -= start }

    for ((to, time) in paths[start]!!.entries) {
      times[to-1] = time
    }

    while (before.size > 0) {
      val node = before.map { it to times[it-1] }.minByOrNull { it.second }!!.first
      before -= node
      after += node
      for (to in before) {
        if (to in paths[node]!!.keys && times[to-1] > paths[node]!![to]!! + times[node-1]) {
          times[to-1] = paths[node]!![to]!! + times[node-1]
        }
      }
    }
    return times
  }

  fun solution() {
    val (n, m, x) = readLine()!!.split(" ").map(String::toInt)
    val paths = hashMapOf<Int, HashMap<Int, Int>>()
    for (i in 1..m) {
      val (start, end, time) = readLine()!!.split(" ").map(String::toInt)
      if (start !in paths) {
        paths[start] = hashMapOf<Int, Int>()
      }
      paths[start]!![end] = time
    }

    val times = Array(n) { dijkstra(n, it+1, paths) }
    println(List(n) { times[it][x-1] + times[x-1][it] }.maxOrNull()!!)
  }
}

fun main() {
  Solution().solution()
}