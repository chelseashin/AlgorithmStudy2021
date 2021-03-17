// 01:46:30 ~ 02:14:50 28분
// +1시간 15분

const log = console.log;

const cardPack = [
  [12, 7, 11, 6, 2, 12],
  [1, 4, 10, 6, 9, 1, 8, 13],
  [10, 13, 10, 1, 2, 3, 4, 5, 6, 2],
  [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
];

function solve(cards) {
  let money = 0;
  let player = [];
  let dealer = [];

  for (let cardIdx = 0; cardIdx < cards.length; ) {
    // 1 ~ 4
    player[0] = cards[cardIdx++];
    dealer[0] = cards[cardIdx++];
    player[1] = cards[cardIdx++];
    dealer[1] = cards[cardIdx++];

    // log('phase1');
    // log(player);
    // log(dealer);

    if (cardIdx > cards.length) {
      // log('phase1 break')
      break;
    }
    
    // 5
    let playerScore = calcScore(player);
    let dealerScore = calcScore(dealer);

    if (playerScore < 21) {
      // get more card
      const [mcScore, drawCardCnt] = getMoreCard(player, cards, cardIdx, dealer[1]);
      cardIdx += drawCardCnt;
      
      if (cardIdx > cards.length) {
      // log('phase1-2 break')
      break;
      }
      
      if (mcScore > 21) {
        money -= 2;
        player = [];
        dealer = [];
        continue;
      }
    } else if (playerScore === 21) {
      if (calcScore(dealer) !== 21) {
        money += 3;
      }
      player = [];
      dealer = [];
      continue;
    }

    // log('phase2');
    // log(player, playerScore);
    // log(dealer);
    
    //6
    while (dealerScore < 17) {
      dealer.push(cards[cardIdx++]);
      dealerScore = calcScore2(dealer, 17);
    }

    if (cardIdx > cards.length) break;

    if (dealerScore > 21) {
      money += 2;
    } else {
      if (playerScore > dealerScore) {
        money += 2;
      } else if (playerScore < dealerScore) {
        money -= 2;
      }
    }
    // log('phase3');
    // log(player, playerScore);
    // log(dealer, dealerScore);
    
    player = [];
    dealer = [];
  }
  
  return money;
}

function calcScore(deck) {
  let [card1, card2] = deck;
  card1 = card1 > 10 ? 10 : card1;
  card2 = card2 > 10 ? 10 : card2;
  
  if (card1 === 1 || card2 === 1 && card1 + card2 === 11) {
    return 21;
  }
  
  return card1 + card2;
}

function calcScore2(deck, limit) {
  deck.sort((a,b) => b - a);
  let score = 0;

  for (const idx in deck) {
    if (idx === deck.length - 1 && deck[i] === 1) {
      if (score + 11 >= limit && score <= 10) {
        return score + 11;
      } else {
        return score + 1;
      }
    } else {
      score += deck[idx] > 10 ? 10 : deck[idx];
    }
  }

  return score;
}

function getMoreCard(user, cards, cardIdx, openCard) {
  let drawCardCnt = 0;
  let tmpScore = calcScore(user);
  if (openCard === 1 || openCard >= 7) {
    while (tmpScore < 17) {
      user.push(cards[cardIdx + drawCardCnt++]);
      tmpScore = calcScore2(user, 17);
    }
  } else if (openCard === 2 || openCard === 3) {
    while (tmpScore < 12) {
      user.push(cards[cardIdx + drawCardCnt++]);
      tmpScore = calcScore2(user, 12);
    }
  }

  return [tmpScore, drawCardCnt];
}

// console.log(solve(cardPack[1]));

for (const cards of cardPack) {
  console.log(solve(cards));
}