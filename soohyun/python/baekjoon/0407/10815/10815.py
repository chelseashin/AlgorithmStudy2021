import sys
inputs = sys.stdin.readline


def bin_search(card, compare_cards):
    end = len(compare_cards) - 1
    start = 0
    while start <= end:
        mid = (start + end) // 2
        if card == compare_cards[mid]:
            return 1
        elif card > compare_cards[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


def main():
    _ = inputs().rstrip()
    have_cards = list(map(int, inputs().rstrip().split()))
    _ = inputs().rstrip()
    compare_cards = list(map(int, inputs().rstrip().split()))
    have_cards.sort()
    for card in compare_cards:
        result = bin_search(card, have_cards)
        print(result, end=" ")

if __name__ == "__main__":
    main()