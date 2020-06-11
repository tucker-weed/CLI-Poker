
class Player:
    """A class that deals with player attributes."""

    def __init__(self,start_cash):
        """Initialize attributes of the class."""
        
        self.cash = start_cash
        self.hand = []
        self.id = 0
        self.alias = ""
        self.total_bet = 0
        self.called = False
        self.all_in = False
        self.current_rank = 0
        self.tied_hand = []
        self.card_rank = 0
        self.is_ai = False
        self.show_cards = False

