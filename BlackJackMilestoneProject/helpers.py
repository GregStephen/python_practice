def take_bet(chips):
  while True:
    try:
      chips.bet = int(input("How many chips would you like to bet: "))
    except:
      print("Sorry please provide an integer")
    else:
      if chips.bet > chips.total:
        print('Sorry, your bet cannot exceed {}'.format(chips.total))
      else:
        break


def hit(deck, hand):

  hand.add_card(deck.deal_one())
  hand.adjust_for_ace()

def hit_or_stand(deck, hand, game_on):

  while True:
    game_on = True
    x = input('Hit or Stand? enter h or s')

    if x[0].lower() == 'h':
      hit(deck, hand)
    
    elif x[0].lower() == 's':
      print("Player Stands Dealer's Turn")
      game_on = False

    else:
      print("Sorry I didn't understand that, please enter h or s only")
      continue

    return game_on

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
  print("Bust Player!")
  chips.lose_bet()

def player_wins(player, dealer, chips):
  print("Player Wins!")
  chips.win_bet()

def dealer_busts(player, dealer, chips):
  print("Player Wins! Dealer busted")
  chips.win_bet()

def dealer_wins(player, dealer, chips):
  print("Dealer Wins!")
  chips.lose_bet()

def push(player, dealer):
  print('Dealer and player tie! PUSH')

