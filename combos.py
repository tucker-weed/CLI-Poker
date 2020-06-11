import collections as COL

class Combos:
    """A class that takes the player's hand plus the river and inputs them into combo algorithms."""
    
    def __init__(self,river):
        """Initialize river for crosschecking with hand."""
        self.river = river

    def evaluate(self,hand):
        """Method which evaluates all potential combos."""
        
        rank = 0
        Crank = 0
        CCrank = 0
        together = []
        for card in hand:
            together.append(card)
        for crd in self.river:
            together.append(crd)
        
        ordered_listt = []
        
        for card in hand:
            ordered_listt.append(card.rank)
        for crd in self.river:
            ordered_listt.append(crd.rank)

        ordered_listt.append(69)
        ordered_listt.sort()

        NAMELIST = []
        for elem in self.river:
            NAMELIST.append(elem.name)
        dictt = COL.Counter(NAMELIST)

        # Check for a pair, three of a kind, four of a kind, full house, or two pair.
        count = 0
        PAIR = False
        if hand[0].name == hand[1].name:
            count = 1
            PAIR = True
            Crank = hand[0].rank
        fakeC1 = 0
        fakeC2 = 0
        C1rank = 0
        C2rank = 0
        for crd in self.river:
            if count == 0:
                if crd.name == hand[0].name:
                    fakeC1 += 1
                    if hand[0].rank > C1rank:
                        C1rank = hand[0].rank
                    if hand[0].rank > Crank:
                        Crank = hand[0].rank
                if crd.name == hand[1].name:
                    fakeC2 += 1
                    if hand[1].rank > C2rank:
                        C2rank = hand[1].rank
                    if hand[1].rank > Crank:
                        Crank = hand[1].rank
            else:
                if crd.name == hand[0].name:
                    count += 1
                    if hand[0].rank > Crank:
                        Crank = hand[0].rank

        if PAIR == True and count < 3:
            if count == 2:
                for val in dictt.values():
                    if val >= 2:
                        count = 10
            elif count == 1:
                for key,val in dictt.items():
                    if val == 2:
                        count = 5
                    if val >= 3:
                        for c in self.river:
                            if c.name == key:
                                Crank = c.rank
                        count = 10

        if fakeC1 >= 1 or fakeC2 >= 1:
            if fakeC1 > fakeC2:
                count = fakeC1
            else:
                count = fakeC2

        if fakeC1 == 1 or fakeC2 == 1 and count < 2:
            for val in dictt.values():
                if val == 2:
                    count = 5
        if (fakeC1 + fakeC2) == 2 and fakeC1 != 0 and fakeC2 != 0:
            count = 5
        if fakeC1 == 2 or fakeC2 == 2 and count != 3:
            for key,val in dictt.items():
                if hand[0].name != key and hand[1].name != key and val == 2:
                    if fakeC1 == 2:
                        Crank = C1rank
                    if fakeC2 == 2:
                        Crank = C2rank
                    count = 10
        if fakeC1 == 1 or fakeC2 == 1 and count != 3:
            for key,val in dictt.items():
                if hand[0].name != key and hand[1].name != key and val == 3:
                    count = 10
        if fakeC1 == 2 and fakeC2 == 2:
            if C1rank > C2rank:
                Crank = C1rank
            else:
                Crank = C2rank
            fakeC2 = 1
        if (fakeC1 + fakeC2) == 3 and ((fakeC1 == 2 and fakeC2 == 1) or (fakeC2 == 2 and fakeC1 == 1)):
            if fakeC1 > fakeC2:
                Crank = C1rank
            else:
                Crank = C2rank
    
            if count != 3:
                count = 10


        if count == 1:
            rank = 1
        elif count == 5:
            rank = 2
        elif count == 2:
            rank = 3
        elif count == 10:
            rank = 6
        elif count == 3:
            rank = 7


        # Check for a straight.
        def check_for_straight(lis):
            countS = 0
            highest_is_ace =  False
            lowest_is_ace = False
            rank_saver = 0
            for key, item in enumerate(lis):
                if lis[key+1] == 69:
                    break
                if lis[key+1] == item:
                    continue
                if lis[key+1] == (item + 1):
                    countS += 1
                    if countS == 4:
                        rank_saver = lis[key+1]
                        if lis[key+1] == 13:
                            highest_is_ace = True
                        break
                else:
                    countS = 0
            if countS < 4:
                countS = 0
            if 13 in lis and countS == 0 and len(lis) >= 4:
                if lis[0] == 1:
                    countS += 1
                if lis[1] == 2:
                    countS += 1
                if lis[2] == 3:
                    countS += 1
                if lis[3] == 4:
                    countS += 1
                if countS == 4:
                    lowest_is_ace = True

            return countS, highest_is_ace, lowest_is_ace, rank_saver

        NUMBER, high,low, r = check_for_straight(ordered_listt)
        if NUMBER == 4:
            if rank < 5:
                rank = 4
                if low:
                    Crank = 4
                else:
                    Crank = r

        # Check for a Flush.
        suit_list = [0,0,0,0]
        STRAIGHTFLUSH = False
        together3 = [[],[],[],[]]
        for elem in together:
            if elem.suit == "hearts":
                suit_list[0] += 1
                together3[0].append(elem.rank)
                together3[0].sort()
            elif elem.suit == "diamonds":
                suit_list[1] += 1
                together3[1].append(elem.rank)
                together3[1].sort()
            elif elem.suit == "spades":
                suit_list[2] += 1
                together3[2].append(elem.rank)
                together3[2].sort()
            else:
                together3[3].append(elem.rank)
                together3[3].sort()
                suit_list[3] += 1

        for elem in together3:
            elem.append(69)

        ace_highest = False

        for num, v in enumerate(suit_list):
            if v >= 5:
                AR = together3[num]
                NOOMBER, HIGH, LOW, r = check_for_straight(AR)
                if NOOMBER == 4:
                    STRAIGHTFLUSH = True
                    if HIGH == True:
                        ace_highest = True
                if not STRAIGHTFLUSH and (rank == 6 or rank == 7):
                    continue
                if LOW:
                    Crank = 4
                else:
                    if r != 0:
                        Crank = r
                    else:
                        Crank = AR[-2]
                rank = 5

        # Check for a straight flush.
        if STRAIGHTFLUSH:
            rank = 8

        # Check for a royal flush.
        if STRAIGHTFLUSH and ace_highest:
            rank = 9
        
        return rank, Crank # Return the combo rank and rank of the highest card in combo for further work.
 
