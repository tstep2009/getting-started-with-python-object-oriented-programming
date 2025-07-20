"""
Python Object-Oriented Programming Class Example
"""

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
if __name__ == "__main__ ":
    card1 = Card ("Ace", "Spades") # Option shift dwn arrow 
    card2 = Card ("Queen", "Hearts")

    print(card1)
    print(card2)

    
    

