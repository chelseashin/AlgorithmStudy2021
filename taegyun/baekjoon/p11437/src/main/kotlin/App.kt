fun tree(n: Int, path: Map<Int, List<Int>>, level: Int, levels: IntArray, parent: Int, parents: IntArray) {
  levels[n-1] = level
  parents[n-1] = parent
  path[n]!!.filter { it != parent }.forEach { tree(it, path, level+1, levels, n, parents) }
}

fun findLCA(v1: Int, v2: Int, levels: IntArray, parents: IntArray): Int {
  var c1 = v1
  var c2 = v2
  while (c1 != c2) {
    if (levels[c1-1] < levels[c2-1]) {
      c2 = parents[c2-1]
    } else if (levels[c1-1] > levels[c2-1]) {
      c1 = parents[c1-1]
    } else {
      c1 = parents[c1-1]
      c2 = parents[c2-1]
    }
  }
  return c1
}

class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val path = hashMapOf<Int, MutableList<Int>>()
    repeat(n-1) {
      val (v1, v2) = readLine()!!.split(" ").map(String::toInt)
      if (v1 !in path) {
        path[v1] = mutableListOf<Int>()
      }
      if (v2 !in path) {
        path[v2] = mutableListOf<Int>()
      }
      path[v1]!! += v2
      path[v2]!! += v1
    }

    val levels = IntArray(n)
    val parents = IntArray(n)
    tree(1, path, 0, levels, 0, parents)

    repeat(readLine()!!.toInt()) {
      val (v1, v2) = readLine()!!.split(" ").map(String::toInt)
      println(findLCA(v1, v2, levels, parents))
    }
  }
}

fun main() {
  Solution().solution()
}