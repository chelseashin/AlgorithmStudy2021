import kotlin.math.log2
import kotlin.math.ceil

class Solution {
  fun getRangeSum(tree: LongArray, node: Int, start: Int, end: Int, left: Int, right: Int): Long {
    if (right < start || end < left) {
      return 0
    } else if (left <= start && end <= right) {
      return tree[node]
    } else {
      return getRangeSum(tree, node*2, start, (start+end)/2, left, right) + getRangeSum(tree, node*2+1, (start+end)/2+1, end, left, right)
    }
  }

  fun changeNodeValue(tree: LongArray, node: Int, start: Int, end: Int, index: Int, diff: Long) {
    if (index < start || end < index) {
      return
    }
    tree[node] += diff
    if (start != end) {
      changeNodeValue(tree, node*2, start, (start+end)/2, index, diff)
      changeNodeValue(tree, node*2+1, (start+end)/2+1, end, index, diff)
    }
  }

  fun initSegmentTree(nums: LongArray, tree: LongArray, node: Int, start: Int, end: Int): Long {
    if (start == end) {
      tree[node] = nums[start]
    } else {
      tree[node] = initSegmentTree(nums, tree, node*2, start, (start+end)/2) + initSegmentTree(nums, tree, node*2+1, (start+end)/2+1, end)
    }
    return tree[node]
  }
  
  fun solution() {
    val (n, m, k) = readLine()!!.split(' ').map(String::toInt)
    val segmentTree = LongArray(2 shl ceil(log2(n.toDouble())).toInt())
    val nums = LongArray(n) { readLine()!!.toLong() }
    initSegmentTree(nums, segmentTree, 1, 0, n-1)

    repeat(m+k) {
      val (a, b, c) = readLine()!!.split(' ')
      when (a) {
        "1" -> {
          val index = b.toInt() - 1
          val value = c.toLong()
          changeNodeValue(segmentTree, 1, 0, n-1, index, value-nums[index])
          nums[index] = value
        }
        "2" -> {
          val left = b.toInt() - 1
          val right = c.toInt() - 1
          println(getRangeSum(segmentTree, 1, 0, n-1, left, right))
        }
      }
    }
  }
}

fun main() {
  Solution().solution()
}