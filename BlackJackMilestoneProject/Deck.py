import random
import data
import Card

class Deck():
  def __init__(self):
    self.all_cards = []

    for suit in data.suits:
      for rank in data.ranks:
        created_card = Card.Card(suit, rank)
        self.all_cards.append(created_card)
  
  def __str__(self):
    deck_comp = ''
    for card in self.all_cards:
      deck_comp += '\n' + card.__str__()
    return "The deck has: " + deck_comp

  def shuffle(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()