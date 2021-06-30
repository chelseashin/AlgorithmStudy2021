class Solution {
  fun solution() {
    val (n, d, k, c) = readLine()!!.split(' ').map { it.toInt() }
    val chobabs = List(n) { readLine()!!.toInt() }

    val circleN: (Int) -> Int = { it % n }

    if (n <= d && d <= k) {
      println(d)
      return
    }

    val countChobobs: (Map<Int, Int>) -> Int = { if (it.containsKey(c)) it.keys.size else it.keys.size + 1 }

    val frequencies = chobabs.subList(0, k).groupingBy { it }.eachCount().toMutableMap()
    var max = countChobobs(frequencies)

    for (i in 1..(n-1)) {
      val prev = chobabs[i-1]
      val next = chobabs[circleN(i+k-1)]
      
      val prevCount = frequencies.getOrDefault(prev, 1)
      if (prevCount == 1) {
        frequencies.remove(prev)
      } else {
        frequencies.put(prev, prevCount - 1)
      }

      val nextCount = frequencies.getOrDefault(next, 0)
      if (nextCount == 0) {
        frequencies.put(next, 1)
      } else {
        frequencies.put(next, nextCount + 1)
      }

      val count = countChobobs(frequencies)
      if (count > max) {
        max = count
      }
    }

    println(max)
  }
}

fun main() {
  Solution().solution()
}