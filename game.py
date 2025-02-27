

import random


class Card:
  __suits = ["♠", "♣", "♦", "♥"]
  __ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  
  def __init__(self, suit: str, rank: str):
    if suit not in Card.__suits:
      raise ValueError(f"Некорректная масть: {suit}. Возможные значения: {Card.__suits}")
    if rank not in Card.__ranks:
      raise ValueError(f"Некорректный ранг: {rank}. Возможные значения: {Card.__ranks}")
    
    self.__suit = suit
    self.__rank = rank

  @staticmethod
  def get_suits():
    return Card.__suits
  
  @staticmethod
  def get_ranks():
    return Card.__ranks

  def __repr__(self):
    return f'{self.__suit}{self.__rank}'


class Deck:
  def __init__(self, deck: list):
    self.__deck = deck

  @property
  def get_deck(self):
    return self.__deck

  @classmethod
  def generation_deck(cls):
    __deck = [Card(suit, rank) for suit in Card.get_suits() for rank in Card.get_ranks()]
    return cls(deck=__deck)

  def card_shuffling(self):
    random.shuffle(self.__deck)

  def post_first_card(self):
    return self.__deck[:6]
  
  def get_trump_card(self):
    return random.choice(self.__deck)

  def __iter__(self):  
    return self 
  
  def __getitem__(self, index):
    return self.__deck[index]

  def __delitem__(self, index):
    del self.__deck[index]

  def __len__(self):
    return len(self.__deck)

  def __repr__(self):
    return f"CardList({self.__deck})"


d = Deck.generation_deck()
d.card_shuffling()


class Player:
  def __init__(self, name: str):
    self.name = name
    self.__hands = []

  def get_firs_card(self):
    self.__hands.extend(d.post_first_card())
    del d[:6]

  def __repr__(self):
    return f'игрок: {self.name}'


p = Player('Илья')


class Game:
  def __init__(self):
    pass