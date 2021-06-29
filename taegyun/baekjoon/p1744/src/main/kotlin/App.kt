class Solution {
  fun solution() {
    val n = readLine()!!.toInt()
    val nums = List(n) { readLine()!! }.map(String::toInt)
    
    val minus = nums.filter { it < 0 }.sorted().chunked(2) { it.reduce { a, x -> a * x } }.sum()
    val plus = nums.filter { it > 1 }.sortedDescending().chunked(2) { it.reduce { a, x -> a * x } }.sum()
    val one = nums.filter { it == 1 }.sum()
    val sum = minus + plus + one
    
    println(sum)
  }
}

fun main() {
  Solution().solution()
}