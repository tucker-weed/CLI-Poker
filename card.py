class Card:
    """A class handling the creation of a card and its attributes."""

    def __init__(self,name,suit):
        """Initialize attributes."""
        
        self.name = name
        self.suit = suit
        
        try:
            i = int(name)
            self.rank = i-1
        except:
            if name == "jack":
                self.rank = 10
            elif name == "queen":
                self.rank = 11
            elif name == "king":
                self.rank = 12
            elif name == "ace":
                self.rank = 13

    def clone(self):
        """This method creates a copy of the initialized card object and returns it for further work."""
        
        new = Card(self.name,self.suit)
        new.rank = self.rank
        return new
