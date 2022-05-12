# pyPoker

Python poker simulation using OOP principles

### class PokerGame

#### class Card
suit
rank

#### class Deck 
pop()
shuffle()
dealHands()

#### class Player
money
call()
raise(amount)
fold()

#### class Dealer
flop()
turn()
river()
int[] bets
Player firstBet

Driver {

while(players > 1){
  shuffle deck(re-initialize cardstack)
  collect ante
  deal 2 cards to each player
  preFlop();
  flop();
  turn();
  river();
}

players.get(0) is the winner;

}

Deal a hand and calculate number of hands that beat that hand

For front end build card image programatically instead of storing 52 photos 

https://www.learnpythonwithrune.org/master-object-oriented-programming-by-creating-a-card-game/





