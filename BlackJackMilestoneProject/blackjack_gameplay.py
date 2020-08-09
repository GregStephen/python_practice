import Card
import Deck
import Player
import Hand
import Chips
import helpers

game_on = True

while True:
  print("Welcome to Blackjack")

  deck = Deck.Deck()
  deck.shuffle()

  player_hand = Hand.Hand()
  player_hand.add_card(deck.deal_one())
  player_hand.add_card(deck.deal_one())

  dealer_hand = Hand.Hand()
  dealer_hand.add_card(deck.deal_one())
  dealer_hand.add_card(deck.deal_one())

  player_chips = Chips.Chips()

  helpers.take_bet(player_chips)

  helpers.show_some(player_hand, dealer_hand)

  while game_on:
    game_on = helpers.hit_or_stand(deck, player_hand, game_on)

    helpers.show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
      helpers.player_busts(player_hand, dealer_hand, player_chips)
      break
  
  if player_hand.value <= 21:
    while dealer_hand.value < 17:
      helpers.hit(deck, dealer_hand)

    helpers.show_all(player_hand, dealer_hand)

    if dealer_hand.value > 21:
      helpers.dealer_busts(player_hand, dealer_hand, player_chips)

    elif dealer_hand.value > player_hand.value:
      helpers.dealer_wins(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value < player_hand.value:
      helpers.player_wins(player_hand,dealer_hand,player_chips)

    else:
      helpers.push(player_hand,dealer_hand) 

  print("\nPlayer's winnings stand at",player_chips.total)
  
  # Ask to play again
  new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
  
  if new_game[0].lower()=='y':
    game_on = True
    continue
  else:
    print("Thanks for playing!")
    break