# 유저 생성
class User():
    def __init__(self):
        self.cards = []
        self.sum = 0
        # 11은 최대 하나니까 적용할 변수 하나 둬서 처리하기
        self.maxSum = 0
        
    def add(self, card):
        if card > 10:   # J, Q, K 처리 
            card = 10
        if card == 1:   # A 처리, 11로 계산했을 때의 값을 따로 저장
            self.maxSum += 10
        self.cards.append(card)
        self.sum += card
        self.maxSum += card
        
def battle(player, dealer):
    # 11 사용해서 21 이하이면 A를 11로 사용한 것으로 바꿔줌
    if player.maxSum <= 21:
        player.sum = player.maxSum
    if dealer.maxSum <= 21:
        dealer.sum = dealer.maxSum
    # 비김
    if player.sum == dealer.sum:
        return 0
    # 패
    elif player.sum < dealer.sum:
        return -2
    # 승
    else:
        if player.sum == 21:    # 블랙잭
            return 3
        else:
            return 2

def giveCard(user, cards):
    global idx
    user.add(cards[idx])
    idx += 1

# 1로 사용할지, 11로 사용할지 정해서 계산
# limit 이상 될 때까지 카드 받기
def canGive(user, limit):
    # 21 넘어가면 11로 사용 안 함
    # 11 사용하면 maxSum으로 보고, 1 사용하면 sum으로 봄
    if user.maxSum > 21:
        if user.sum < limit:    # limit 넘지 않으면 카드 줄 수 있음
            return True
        else:
            return False
    else:   # 11로 사용
        if user.maxSum < limit:
            return True
        else:
            return False

def play(cards):
    global idx, score
    player = User()
    dealer = User()
    # 처음 한 장씩 두번 받음
    for i in range(4):
        if i % 2 == 0:      # 플레이어가 받음
            giveCard(player, cards)
        else:
            giveCard(dealer, cards)
    # 딜러의 두 번째 카드 오픈
    openCard = dealer.cards[1]

    # player 카드 더 받을지 확인
    while True:
        if player.sum == 21 or player.maxSum == 21:   # 둘다 카드 합 21
            return battle(player, dealer)   # 누가 이겼는지 점수 리턴
        elif player.sum > 21:
            return -2           # 21 넘어가면 즉시 패배
        else:
            if (openCard == 1 or openCard >= 7):
                if canGive(player, 17):     # 카드 합 17이상 될 때까지 받음
                    giveCard(player, cards)
                else:
                    break
            elif openCard in [4, 5, 6]:     # 플레이어 카드 받지 X
                break
            elif openCard in [2, 3]:
                if canGive(player, 12):     # 카드 합 12이상 될 때까지 받음
                    giveCard(player, cards)
                else:
                    break
    # dealer 카드 더 받을지 확인
    while True:
        if dealer.sum > 21:         # 딜러 카드 합 21 넘으면 즉시 패배
            return 2
        if canGive(dealer, 17):     # 딜러 카드 합 17 넘을 때까지 카드 받기
            giveCard(dealer, cards)
        else:                       # 17 넘으면 받기 중단
            break
    # 이번 게임 종료
    return battle(player, dealer)

def solution(cards):
    global idx, score
    idx, score = 0, 0
    while True:
        # 예외처리로 카드 인덱스 넘기면서 끝나도록
        try:        # play()에서 예외 발생하지 않으면 점수 리턴,
            score += play(cards)
        except:     # 발생하면 점수 출력하고 종료
            return score
print(solution([12, 7, 11, 6, 2, 12]))
print(solution([1, 4, 10, 6, 9, 1, 8, 13]))
print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))
print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))

# 2
# 1
# -2
# -2