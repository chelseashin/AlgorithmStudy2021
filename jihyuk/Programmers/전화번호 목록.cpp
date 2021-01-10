/**
 1) 소요 시간 : 45분

 2) 사용 알고리즘 및 자료구조
	- map 자료구조 사용
 
 3) 풀면서 겪었던 문제
	- string 대소 비교시, string 크기 차이에 따른 리턴값을 헷갈림
	- 정렬 후 2중 for문을 사용해서 비효율적으로 구현. 추 후 1중 for문으로 다시 구현
	
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book)
{
	/*
	 * 문자열 정렬
	 * 알파벳 순으로 정렬
	 * 접두사가 같고 길이만 다른 경우, 짧은 문자열이 앞쪽으로 배치됨
	 */
	sort(phone_book.begin(), phone_book.end());

	for (size_t i = 0; i < phone_book.size() - 1; ++i)
	{
		/*
		 * 알파벳순으로 정렬되어 있고, 동일한 접두사일 경우 짧은 문자열이 앞쪽에 배치됨
		 * 따라서 앞뒤로만 비교해주면 접두사 포함 관계를 판별할 수 있음
		 */

		// find() 함수로 찾았을 때 리턴 값 : 0
		if (0 == phone_book[i + 1].find(phone_book[i]))
		{
			return false;
		}
	}

	return true;
}