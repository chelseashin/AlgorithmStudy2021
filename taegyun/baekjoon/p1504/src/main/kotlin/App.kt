import java.util.HashSet
import java.util.HashMap

class Solution {
  fun solution() {
    val INFINITE = 1000000

    val (n, e) = readLine()!!.split(' ').map(String::toInt)
    val edges = HashMap<Int, HashMap<Int, Int>>()
    for (i in 1..n) {
      edges.put(i, HashMap<Int, Int>())
    }
    repeat(e) {
      val (a, b, c) = readLine()!!.split(' ').map(String::toInt)
      edges[a]!!.put(b, c)
      edges[b]!!.put(a, c)
    }
    val (v1, v2) = readLine()!!.split(' ').map(String::toInt)

    val dijkstra: (Int) -> IntArray = {
      val done = HashSet<Int>(n)
      val remain = HashSet<Int>(n)
      remain.addAll(edges.keys)
      val paths = IntArray(n+1) { INFINITE }
      paths[it] = 0

      while (remain.size > 0) {
        var minNode = 0
        var minDistance = INFINITE
        for (i in 1..n) {
          if (i in done || paths[i] >= INFINITE) {
            continue
          }
          if (paths[i] < minDistance) {
            minNode = i
            minDistance = paths[i]
          }
        }
        if (minNode == 0) {
          break
        }

        done.add(minNode)
        remain.remove(minNode)

        edges[minNode]!!.filterKeys { it in remain }.forEach { (n, d) ->
          if (paths[n] > minDistance + d ) {
            paths[n] = minDistance + d
          }
        }
      }

      paths
    }

    val paths1 = dijkstra(1)
    val pathsV1 = dijkstra(v1)
    val pathsV2 = dijkstra(v2)

    val t1 = paths1[v1] + pathsV1[v2] + pathsV2[n]
    val t2 = paths1[v2] + pathsV2[v1] + pathsV1[n]
    val min = if (t1 < t2) t1 else t2
    if (min >= INFINITE) {
      println(-1)
    } else {
      println(min)
    }
  }
}

fun main() {
  Solution().solution()
}