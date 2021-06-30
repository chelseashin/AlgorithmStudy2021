consonant = {'a','e','i','o','u'}

def is_contains(visited):
    for value in visited:
        if value in consonant:
            return True
    return False

def is_vowels(visited):
    count = 0
    for value in visited:
        if value not in consonant:
            count += 1
            if count >= 2:
                return True
    return False

def is_satisfy_condition(result, is_visited, visited):
    if result not in is_visited \
        and is_contains(visited) \
        and is_vowels(visited):
        return True
    return False

def solution(numbers, len_words):
    visited = []
    is_visited = set()
    all_words = len(numbers)
    def recurse(visited_len, visited):
        if visited_len == len_words:
            visited.sort()
            result = ''.join(visited)
            if is_satisfy_condition(result, is_visited, visited):
                print(result)
            return
        else:
            for character in range(visited_len, all_words):
                if visited_len == 0:
                    visited.append(numbers[character])
                    recurse(visited_len+1, visited)
                    visited.pop()

                elif visited[-1] < numbers[character]:
                    visited.append(numbers[character])
                    recurse(visited_len+1, visited)
                    visited.pop()
    recurse(len(visited), visited)


def input_values():
    code, _ = map(int, input().rstrip().split(" "))
    words = input().rstrip().split(" ")
    words.sort()
    return words, code

def main():
    numbers, len_words = input_values()
    solution(numbers, len_words) 

if __name__ == "__main__":
    main()