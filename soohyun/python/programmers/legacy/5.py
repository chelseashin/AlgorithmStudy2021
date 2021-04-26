#시작 13:00
    '''
    초기화 game
    while cards갯수가 0보다 크다면:
        game이 0이나 2라면 player += card (더하는 방법도 달리해야함)
        game이 1이나 3이라면 dealer += card
        만약 player가 blackjack이면 result + 3
        만약 dealer가 blackjack이면 result - 2
        모두 blackjack이라면 0
        game = 0, dealer, player 0,0
        game 3일때 그 값이 1, 7 라면
            while player < 17: player += cars.pop(0), game += 1
            만약 player > 21 이라면 result - 2 //
        game=3 일때 그 값이 이 4,5,6이라면
            while dealer < 17 dealer += cards.pop(0), game += 1
            만약 delaer > 21이면 result + 3
        game=3일때 그 값이 2, 3인 경우 player 
        승부로 
        game = 0, dealer player 0,0
    '''
def card_calc(card):
    continue


def check_victory(player, dealer):
    continue


def solution(cards):
    dealer, player = 0, 0
    game = 0
    cache = 0
    while len(cards) > 0:
        card = cards.pop(0)
        if game == 0 or game == 2:
            player += card_calc(card)
        elif game == 1 or game == 3:
            dealer += card_calc(card)
        play_result = check_victory(player, dealer)
        if play_result > 0:
            result += play_result
            dealer, player = 0, 0
            game = 0
            continue

        if game == 3:
            if card == 1 or card >=7:
                while player < 17: 
                    player += card_calc(cards.pop(0))
                    game += 1
            elif card == 4 or card == 5 or card == 6:
                while dealer < 17:
                    dealer += card_calc(cards.pop(0))
                    game += 1
            else:
                while player < 12:
                    player += card_calc(cards.pop(0))
                    game += 1
            play_result = check_victory(player, dealer)
            if play_result > 0:
                result += card_calc(play_result)
                dealer, player = 0, 0
                game = 0
                continue
        game += 1  
    return None

if __name__ == "__main__":
    print(solution([12, 7, 11, 6, 2, 12]))
    print(solution([1, 4, 10, 6, 9, 1, 8, 13]))
    print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
    print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))

#1. 딜러의 보이는 카드가 1이거나 7 이상인 경우, 플레이어는 카드 합이 17 이상이 될 때까지 받는다.
#2. 딜러의 보이는 카드가 4, 5, 6인 경우, 플레이어는 카드를 받지 않는다.
#3. 딜러의 보이는 카드가 2, 3인 경우, 플레이어는 카드 합이 12 이상이 될 때까지 받는다.
