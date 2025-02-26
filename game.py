

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
  def _generation_deck(cls):
    deck = [Card(suit, rank) for suit in Card.get_suits() for rank in Card.get_ranks()]
    return cls(deck=deck)
    
  def __len__(self):
    return len(self.__deck)
    
  def __iter__(self):  
    return self 
  
  def __getitem__(self, index):
    return self.__deck[index]  # Доступ к элементу по индексу
    
  def __setitem__(self, index, value):
    self.__deck[index] = value  # Изменение элемента
    
  def __len__(self):
    return len(self.__deck)  # Возвращаем длину списка
    
  def __repr__(self):
    return f"List({self.__deck})"


class PersonalisedDeck:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pass