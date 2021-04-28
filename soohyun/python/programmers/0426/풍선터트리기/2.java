import java.util.*;
class Solution {
    public int solution(int[] a) {
		/**
		출처: https://velog.io/@jkh2801/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0
		풀이방식: 작은값들을 가져온다.
		시간 복잡도 O(2*N)
		 */
        HashSet <Integer> set = new HashSet<Integer>();
		// 가에있는값은 무조건 남길 수 있음
		int min = a[0];
		for (int i = 1; i < a.length; i++) {
			// 최소값을 set에 넣음
			set.add(min);
			// 이전값보다 더 작으면 어차피 남겨질수있으므로
			min = Math.min(a[i], min);
		}
		// 가에있는값은 무조건 남길 수 있음
		min = a[a.length-1];
		for (int i = a.length-2; i >= 0; i--) {
			// 최소값을 set에 넣음
			set.add(min);
			// 이전값보다 작으면 어차피 남겨질 수 있으므로
			min = Math.min(a[i], min);
		}
        return set.size();
    }
}