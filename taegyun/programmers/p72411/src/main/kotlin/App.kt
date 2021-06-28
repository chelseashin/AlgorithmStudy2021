fun <T> combinationTo(destination: MutableList<List<T>>, items: List<T>, checked: BooleanArray, start: Int, left: Int) {
  if (left == 0) {
      destination += items.filterIndexed { index, _ -> checked[index] }
  } else {
      for (i in start until items.size) {
          checked[i] = true
          combinationTo(destination, items, checked, i+1, left-1)
          checked[i] = false
      }
  }
}

fun String.combinations(n: Int): List<String> {
  val results = mutableListOf<List<Char>>()
  combinationTo(results, this.toList(), BooleanArray(this.length), 0, n)
  return results.map { it.sorted().joinToString("") }
}

class Solution {
  fun solution(orders: Array<String>, course: IntArray): Array<String> {
      val candidates = orders.flatMap { order ->
          course.filter { it <= order.length }.flatMap { order.combinations(it) }
      }.groupingBy { it }.eachCount().filterValues { it >= 2 }
      val maxCounts = candidates.entries.groupingBy { it.key.length }.fold(0) { acc, el ->
          if (el.value > acc) el.value else acc
      }
      return candidates.filter { (key, value) ->
          value >= maxCounts[key.length]!!
      }.keys.sorted().toTypedArray()
  }
}