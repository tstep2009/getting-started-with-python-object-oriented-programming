"""
Python Object-Oriented Programming Class Example
"""

class Card:
    def __init__(self, value, suit): #  method gets called every time we create an instance of a class
        """Initialize a Card instance with a value and a suit."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
if __name__ == "__main__":
    card1 = Card ("Ace", "Spades") # Option shift dwn arrow 
    card2 = Card ("Queen", "Hearts")
    card3 = Card ("King", "Clubs")
    card4 = Card ("Jack", "Spades")

    print(card1)
    print(card2)
    print(card3)
    print(card4)

    
    

