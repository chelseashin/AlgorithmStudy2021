class Solution {
  fun solution() {
    var str1 = "0" + readLine()!!
    var str2 = "0" + readLine()!!
    
    if (str1.length < str2.length) {
      val temp = str1
      str1 = str2
      str2 = temp
    }

    val matrix = Array(str2.length) { IntArray(str1.length) { 0 } }

    for (i in 1..str2.length-1) {
      for (j in 1..str1.length-1) {
        if (str2[i] == str1[j]) {
          matrix[i][j] = matrix[i-1][j-1] + 1
        } else {
          if (matrix[i][j-1] > matrix[i-1][j]) {
            matrix[i][j] = matrix[i][j-1]
          } else {
            matrix[i][j] = matrix[i-1][j]
          }
        }
      }
    }

    println(matrix.last().last())
  }
}

fun main() {
  Solution().solution()
}