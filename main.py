import random
import time
import card as mod
import player as plr
import combos as cb
import screen

Atrr = screen.Atrr

deck = []
players = []
folded_players = []
river = []
pot = [0]
rounds_counter = 0
highest_id = 0
starters = 0
tieS = [False]
blinds = [False]
blinds_pos = [0,1]

# Game environment variables
percent = 3
percent_memory = 3
DEBUGGER = False
TOURNAMENT_STYLE = True
AI_ON = False

def make_under_5(inpu):
    while inpu >= 5:
        inpu = inpu//5
    return inpu


def return_ai_response(arr, to_call, play):
    """This method is fed an array of possible responses, and then gives back a response after weighing other paramater info."""
    global starters

    time.sleep(1)

    bad = 0
    good = 2
    great = 3

    if blinds[0] and to_call <= round(starters*(percent/100)):
        new = cb.Combos(river)
        curr, crd = new.evaluate(play.hand)
        if curr > 0:
            other = 13 - ( max([play.hand[0].rank,play.hand[1].rank]) * 2 )
            if other < 0:
                other = 0
        else:
            other = 13 - max([play.hand[0].rank,play.hand[1].rank])
        sw = (random.randint(0,other) == 0)
        if not sw or play.cash < (starters/2):
            return "bet", 69696969
        elif not play.cash < (starters/2):
            return "bet", round(starters*(percent/100)) * random.randint(1,2)

    if to_call <= (play.cash*0.1) and to_call != 0:
        new = cb.Combos(river)
        curr, crd = new.evaluate(play.hand)
        check = random.randint(0,1)
        sw = (random.randint(0,3) == 1)
        if curr <= 1 and check == 1:
            return  "fold", 0
        else:
            if not sw:
                return "bet", 69696969
            else:
                return "bet", round(starters*(percent/100)) * random.randint(1,2)

    if to_call > 0:
        new = cb.Combos(river)
        curr, crd = new.evaluate(play.hand)

        if to_call >= play.cash/4 and curr >= great:
            random.seed(time.time())
            thingy = 4 - curr
            if thingy < 0:
                thingy = 0
            chck = (random.randint(0,thingy) == 0)
            sw = (random.randint(0,1) == 1)
            if chck:
                if not sw:
                    return "bet", 69696969
                else:
                    return "bet", round(starters*(percent/100)) * random.randint(1,2)
            else:
                return "fold", 0
            
        elif to_call >= play.cash/4 and curr < great:
            random.seed(time.time())
            thingy = 7 - curr
            other = (len(river)-2)
            if other < 0:
                other = 0
            thingy -= other
            if thingy < 0:
                thingy = 0
            chck = (random.randint(0,thingy) == 0)
            sw = (random.randint(0,5) == 1)
            if chck:
                if not sw:
                    return "bet", 69696969
                else:
                    return "bet", round(starters*(percent/100)) * random.randint(1,2)
            else:
                return "fold", 0
            
        elif curr >= great:
            sw = (random.randint(0,2) == 1)
            if not sw:
                return "bet", 69696969
            else:
                return "bet", round(starters*(percent/100)) * random.randint(1,2)
            
        if curr >= good:
            random.seed(time.time())
            chck = (random.randint(0,6) == 0)
            sw = (random.randint(0,3) == 1)            
            if chck:
                return "fold", 0
            
            else:
                if not sw:
                    return "bet", 69696969
                else:
                    return "bet", round(starters*(percent/100)) * random.randint(1,2)
            
        elif curr > bad:
            random.seed(time.time())
            chck = (random.randint(0,2) == 0)
            sw = (random.randint(0,4) == 1)
            if chck:
                return "fold", 0
            
            else:
                if not sw:
                    return "bet", 69696969
                else:
                    return "bet", round(starters*(percent/100)) * random.randint(1,2)
            
            
        else:
            random.seed(time.time())
            switch_ = 0
            if max([play.hand[0].rank,play.hand[1].rank]) >= 10:
                switch_ = 2
            else:
                switch_ = 4
            chck = (random.randint(0,switch_) == 1)
            sw = (random.randint(0,2) == 1)
            if not chck:
                return "fold", 0
            
            else:
                if not sw:
                    return "bet", 69696969
                else:
                    return "bet", round(starters*(percent/100)) * random.randint(1,2)
            
        
    if to_call == 0:
        # No idea why this if statement exists but too lazy to reformat :/
        if True:
            new = cb.Combos(river)
            curr, crd = new.evaluate(play.hand)

            if len(river) > 0:
                
                if curr >= great:
                    mult = 1
                    random.seed(time.time())
                    thingy = 0
                    if len(river) == 3:
                        thingy = 4
                    chck = (random.randint(0,4-thingy) == 0)
                    if not chck:
                        if random.randint(0,4) == 1:
                            random.seed(time.time())
                            mult = random.randint(3,4)
                        else:
                            random.seed(time.time())
                            mult = random.randint(1,2)
                        return "bet", round(starters*(percent/100)) * mult
                    else:
                        return "check", 0
                
                elif curr == good:
                    random.seed(time.time())
                    thingy = 0
                    if len(river) == 3:
                        thingy = 2
                    chck = (random.randint(0,2-thingy) == 0)
                    if chck:
                        return "check", 0
                    
                    else:
                        mult = 1
                        if random.randint(0,2) == 1:
                            random.seed(time.time())
                            mult = random.randint(3,4)
                        else:
                            random.seed(time.time())
                            mult = random.randint(1,2)
                        return "bet", round(starters*(percent/100)) * mult
                    
                elif curr > bad:
                    random.seed(time.time())
                    chck = (random.randint(0,3) == 0)
                    if not chck:
                        return "check", 0
                    
                    else:
                        mult = 1
                        if random.randint(0,3) == 1:
                            random.seed(time.time())
                            mult = random.randint(3,4)
                        else:
                            random.seed(time.time())
                            mult = random.randint(1,2)
                        return "bet", round(starters*(percent/100)) * mult
                    
                else:
                    random.seed(time.time())
                    thingy = 15 - max([play.hand[0].rank,play.hand[1].rank])
                    chck = (random.randint(0,thingy) == 0)
                    if not chck:
                        return "check", 0
                    
                    else:
                        mult = 1
                        thingy = max([play.hand[0].rank,play.hand[1].rank])
                        if random.randint(0,(14 - thingy) ) == 1:
                            random.seed(time.time())
                            mult = random.randint(3,4)
                        else:
                            random.seed(time.time())
                            mult = random.randint(1,2)
                        return "bet", round(starters*(percent/100)) * mult
                    

def set_blinds():
    """This method automatically handles blinds."""
    
    global starters
    global percent
    global players
    
    blinds_pos[0] = 0
    blinds_pos[1] = 1
    small = False
    big = False
    amt1 = round(starters*(percent/100))
    amt2 = round(starters*(percent/200))
    
    for key, p in enumerate(players):
        if not p.called and p.cash > 0:
            if not small:
                small = True
                print("\n\n> "+p.alias_+" is small blind, automatically posting bet.")
                blinds_pos[0] = key
                if amt2 >= p.cash:
                    p.all_in = True
                    p.called = True
                    pot[0] += p.cash
                    p.total_bet += p.cash
                    p.cash = 0
                else:
                    pot[0] += amt2
                    p.total_bet += amt2
                    p.cash -= amt2
            elif not big:
                big = True
                time.sleep(1)
                print("\n\n> "+p.alias_+" is big blind, automatically posting bet.\n")
                blinds_pos[1] = key
                if amt1 >= p.cash:
                    p.all_in = True
                    p.called = True
                    pot[0] += p.cash
                    p.total_bet += p.cash
                    p.cash = 0
                else:
                    pot[0] += amt1
                    p.total_bet += amt1
                    p.cash -= amt1


def all_tie_check(plars):
    """This method will return false if any non-tie is detected."""
    
    yes = False
    checker_array = []
    pl1 = 0
    pl2 = 0
    p1 = 0
    p2 = 0

    if len(plars) == 2:
        if plars[1].id in folded_players:
            return False

    # (Above) This code is the solution to the problem described below.
    # (Below) If there are two players left and the second player in the list has folded, this code may give a false positive.
    for p, v in enumerate(plars):
        if not (len(plars)-1 == p) and not (v.id in folded_players):
            pl1 = v.hand[0].rank
            pl2 = v.hand[1].rank
            
            new_iter_count = (len(plars)-1) - p
            index_offset = 0
            
            for num in range(new_iter_count):
                if num == 0:
                    continue
                if plars[p+num].id in folded_players:
                    index_offset += 1
                else:
                    break

            # (Below) Bad index error prevention.
            if (len(plars) - 1) < (p+1+index_offset):
                break
            
            p1 = plars[p+1+index_offset].hand[0].rank
            p2 = plars[p+1+index_offset].hand[1].rank
            
            # (Below) if both players have a pocket pair, and the summed cards don't complete a set (4,4,4,4), move on to next player.
            if pl1 == pl2 and p1 == p2 and pl1 == p1:
                yes = True
                continue
            elif pl1 == pl2 and p1 == p2 and not pl1 == p1:
                continue
            
            checker_array.clear()
            checker_array.append(pl1)
            checker_array.append(pl2)
            checker_array.append(p1)
            checker_array.append(p2)
            checker_array.sort()
            if checker_array[0] == checker_array[1] and checker_array[2] == checker_array[3]:
                yes = True
    return yes

def tie_check(plars):
    """This method will check if the last two players in line on the list are tied.
    ** For use exclusively with the recursive_check method. """
    
    if (plars[-1].hand[0].rank in plars[-2].tied_hand) and (plars[-1].hand[1].rank in plars[-2].tied_hand):
        return True
    else:
        return False

def crosscheck_three():
    """To check if there is only one player left who is not all in."""
    
    cntr = 0
    for elem in players:
        if not elem.all_in:
            cntr += 1
    if cntr == 1:
        return True
    else:
        return False

def crosscheck_two(pls):
    """If there is anyone left who hasn't folded (and also who hasn't called), this conditional will return False."""
    
    safe = True
    for p in pls:
        if (not p.id in folded_players) and not p.called:
            safe = False
    return safe

def crosscheck():
    cntr = 0
    for elem in players:
        if not elem.id in folded_players:
            cntr += 1
    if cntr == 1:
        return True
    else:
        return False

def recursive_check(plrs):
    """Evaluates combo ranks and eliminates lower ranking matchups from the player list until one player remains."""
    
    if not all_tie_check(plrs) and len(plrs) > 1:
        
        if len(plrs) != 1 and not tie_check(plrs):
            if plrs[-2].id in folded_players:
                plrs.pop(-2)
                recursive_check(plrs)# +1 depth
            if plrs[-1].id in folded_players:
                plrs.pop(-1)
                recursive_check(plrs)# +1 depth


            # The two above conditionals are detached from the main if/elif block, so if + return seen below will prevent further execution.
            if len(plrs) == 1:
                return plrs[0].id

            # (Below) checks for the highest combo rank, and if equal, the highest card rank of the combo.
            if plrs[-2].current_rank > plrs[-1].current_rank:
                plrs.pop()
                recursive_check(plrs)# +1 depth
            elif plrs[-2].current_rank < plrs[-1].current_rank:
                plrs.pop(-2)
                recursive_check(plrs)# +1 depth
            elif plrs[-2].card_rank > plrs[-1].card_rank:
                plrs.pop()
                recursive_check(plrs)# +1 depth
            elif plrs[-2].card_rank < plrs[-1].card_rank:
                plrs.pop(-2)
                recursive_check(plrs)# +1 depth
                
            # (Below) checks for a tie, or a high card of the players' hands.
            else:
                pl1 = plrs[-2].hand[0].rank
                pl2 = plrs[-2].hand[1].rank
                p1 = plrs[-1].hand[0].rank
                p2 = plrs[-1].hand[1].rank
                checker_array = []
                checker_array.append(pl1)
                checker_array.append(pl2)
                checker_array.append(p1)
                checker_array.append(p2)
                checker_array.sort()
            
                if (checker_array[0] == checker_array[1] and checker_array[2] == checker_array[3]) and not ((pl1 == pl2 and p1 == p2) and pl1 != p1):
                    tieS[0] = True
                    if len(plrs[-2].tied_hand) == 0:
                        plrs[-2].tied_hand.append(pl1)
                        plrs[-2].tied_hand.append(pl2)
                    if len(plrs[-1].tied_hand) == 0:
                        plrs[-1].tied_hand.append(pl1)
                        plrs[-1].tied_hand.append(pl2)
                    plrs.insert(0, plrs.pop(-1))
                    recursive_check(plrs)# +1 depth

                # If a tie is detected, kill this branch of recursion before it reads next code.
                if tieS[0]:
                    tieS[0] = False
                    return
                if tie_check(plrs):
                    return

                # (Below) checks for a high card.
                if (pl1 > p1 and  pl1 > p2) or (pl2 > p1 and pl2 > p2):
                    plrs.pop()
                    recursive_check(plrs)# +1 depth
                elif (checker_array[-1] == checker_array[-2]):
                    if pl1 == checker_array[-3] or pl2 == checker_array[-3]:
                        plrs.pop()
                        recursive_check(plrs)# +1 depth
                    else:
                        plrs.pop(-2)
                        recursive_check(plrs)# +1 depth
                else:
                    plrs.pop(-2)
                    recursive_check(plrs)# +1 depth

    tieS[0] = False
    return plrs[0].id


def find_winner(plrs, a_copy):
    """This method uses recursive_check to evaluate a winner, and makes payouts accordingly."""
    
    print("\n")
    for plr1 in plrs:
        cc = cb.Combos(river)
        plr1.current_rank, plr1.card_rank = cc.evaluate(plr1.hand)

    VAL = recursive_check(a_copy)
    ties = False

    # The code block below checks if there is more than one player left. Treated as a tie.
    if len(a_copy) > 1:
        split = round(pot[0]/len(a_copy))
        pot[0] = 0
        ties = True
        for p in a_copy:
            print ("\n"+p.alias_+" tied. Split: "+str(split))
            p.cash += split
    if ties:
        return

    reference = []
    for plr1 in plrs:
        if plr1.id == VAL:
            reference.append(plr1)
    print("\n"+reference[0].alias_+" wins!")
    che = ""
    if crosscheck():

        # Although input is printed for the user, it is arbitrary which user actually puts their input.
        che = input("\nShow cards? Type \'yes\', default no: ")
    print("\nPot: ["+str(pot[0])+"]")
    if che == "yes":
        reference[0].show_cards = True

    # If the winner went all in, the pot is going to be divided according to all in amounts.
    if reference[0].all_in:
        diff = (reference[0].total_bet + ((len(plrs)-1)*reference[0].total_bet)) - pot[0]
        
        # If the maximum return the winner can get is less than the total pot, the winner gets his max return (diff + pot[0]) back only.
        if diff < 0:
            reference[0].cash += pot[0] + diff
            pot[0] = 0 - diff
            place = round(pot[0]/(len(plrs)-1))
            taken_care = 0
            for p in plrs:
                if p != reference[0]:
                    if p.all_in and p.total_bet >= place:
                        p.cash += place
                        pot[0] -= place
                        taken_care += 1
                    elif p.all_in and p.total_bet < place:
                        p.cash += p.total_bet
                        pot[0] -= p.total_bet
                        taken_care += 1
            for p in plrs:
                if not p.all_in:
                    p.cash += round(pot[0]/(len(plrs)-(1+taken_care)))
                    pot[0] -= round(pot[0]/(len(plrs)-(1+taken_care)))
            pot[0] = 0
        # If the winner went all in, but their total bet is equal or higher than the other remaining player's total bet, pay whole pot.
        else:
            reference[0].cash += pot[0]
            pot[0] = 0
    # If the winner did not go all in, pay them the whole pot.
    else:
        reference[0].cash += pot[0]
        pot[0] = 0

    time.sleep(2)
        

def check_inputs(plrs):
    """Checks inputs for each player and handles all turn based betting and display of player stats for each player."""
    
    for p in plrs:
        if not p.all_in and not crosscheck_three():
            p.called = False
            
    has_bet = False
    bet_looper = True
    change = 0
    memory = 0
    amt = ""
    formatted = ""
    inp = ""
    plr_bets = []
    skip_count = 0

    for p in plrs:
        plr_bets.append(0)
        
    if blinds[0]:
        plr_bets[blinds_pos[0]] += round(starters*(percent/200))
        plr_bets[blinds_pos[1]] += round(starters*(percent/100))
        memory = round(starters*(percent/100))
        has_bet = True
        bet_looper = True

    # This loop will check necessary conditionals (see references), but its purpose is to wrap input checking to the first turn player if someone further down the line bet.
    while not ((crosscheck_three() and crosscheck_two(plrs)) or crosscheck_two(plrs) or crosscheck() or not bet_looper):
        
        for KEY, plr in enumerate(plrs):
            
            valid = False

            if blinds[0] and (KEY == blinds_pos[0] or KEY == blinds_pos[1]) and skip_count < 2: # blinds[0] references whether blinds are True for this round of input
                skip_count += 1
                continue

            if not ( plr.id in folded_players or crosscheck() or plr.called or plr.all_in or (crosscheck_three() and crosscheck_two(plrs)) ):
                input("\n"+plr.alias_+"\'s turn. Hit enter to show cards/allow input. ")

            # This loop maintains input feeding to the user being examined.
            # If the player did not provide a valid input, the loop will continue. If any of the other conditionals are true (see references for each), the loop ends.
            while not valid and not ( plr.id in folded_players or crosscheck() or plr.called or plr.all_in or (crosscheck_three() and crosscheck_two(plrs)) ):

                memory2 = memory - plr_bets[plrs.index(plr)]
                am_t = 0
                
                if not has_bet:

                    if not plr.is_ai:
                        # This input shows up if nobody has bet anything yet.
                        print("Action? Type \'check\', \'bet\', or \'fold\':")
                        app = Atrr(plr,river,pot[0]).test()
                        app.attributes('-topmost', True)
                        app.update()
                        app.mainloop()
                        inp = input("")
                    else:
                        inp, am_t = return_ai_response(["check","bet","fold"], 0, plr)
                else:

                    if not plr.is_ai:
                        # This input shows up if the player has yet to call a bet.
                        print("\nAction? Type \'fold\', or (\'bet\' to call or raise)(To call: "+str(memory2)+"): ")
                        app = Atrr(plr,river,pot[0]).test()
                        app.attributes('-topmost', True)
                        app.update()
                        app.mainloop()
                        inp = input("")
                    else:
                        inp, am_t = return_ai_response(["bet","fold"], memory2, plr)
                
                if inp == 'check' and not has_bet:
                    print("\n"+plr.alias_+" checked.")
                    bet_looper = False
                    valid = True
                    
                elif inp == 'bet' and plr.cash > 0:
                    TEM = True
                    
                    while TEM:
                        
                        try:
                            
                            if has_bet:
                                
                                # This input always shows up if the player has yet to call a bet.
                                amt = am_t
                                if not plr.is_ai:
                                    amt = input("\n(To call: "+str(memory2)+") Type \'call\' or type raise amount (Minimum raise is "+str(round(starters*(percent/100)))+"): ")
                                
                                if amt != "call" and amt != 69696969:
                                    if plr.is_ai:
                                        amt = am_t
                                    else:
                                        amt = int(amt)
                                    if amt < round(starters*(percent/100)):
                                        amt = round(starters*(percent/100))
                                    
                                    if amt + memory2 >= plr.cash and plr.cash >= memory2:
                                        memory += (plr.cash - memory2)
                                    elif amt + memory2 < plr.cash:
                                        memory += amt
                                    
                                    # If an amount is typed, player will bet the amount to call in addition to the amount they typed.
                                    amt = memory2 + amt
                                    
                                else:
                                    amt = memory2
                                allIN = False
                                
                                if amt >= plr.cash:
                                    allIN = True
                                    plr.all_in = True
                                    amt = plr.cash
                                    
                                pot[0] += amt
                                plr_bets[plrs.index(plr)] += amt
                                change = amt - memory2
                                plr.total_bet += amt
                                
                                if change < 0 and allIN:
                                    change = 0
                                if change == 0:
                                    print("\n"+plr.alias_+" called.")
                                    plr.called = True
                                else:
                                    print("\n"+plr.alias_+" raised by "+str(change)+".")
                                    
                                    for el in plrs:
                                        if not el.all_in:
                                            el.called = False
                                    plr.called = True
                                plr.cash -= amt
                                valid = True
                                
                                # Exit
                                TEM = False
                                
                                
                            else: # If no one has bet

                                # This input is for the initial better (if there is one) of every round.
                                amt = ""
                                if not plr.is_ai:
                                    amt = input("\nPlace bet amount (Minimum bet is "+str(round(starters*(percent/100)))+"): ")
                                    amt = int(amt)
                                else:
                                    amt = am_t

                                if amt < round(starters*(percent/100)):
                                    amt = round(starters*(percent/100))
                                
                                if amt >= plr.cash:
                                    plr.all_in = True
                                    amt = plr.cash
                                    
                                print("\n"+plr.alias_+" bet "+str(amt)+".")
                                pot[0] += amt
                                plr.called = True
                                memory = amt
                                plr.cash -= amt
                                plr.total_bet += amt
                                plr_bets[plrs.index(plr)] += amt
                                has_bet = True
                                bet_looper = True
                                valid = True
                                
                                # Exit
                                TEM = False
                                   
                        except:
                            
                            print("\nInvalid value! Please enter an integer.")
                            
                elif inp == 'fold':
                    
                    print ("\n"+plr.alias_+" folded.")
                    folded_players.append(plr.id)
                    valid = True
                    
        
def list_hands(plrs):
    """Prints each player's hand, in addition to the river."""
    
    chuck = 100
    print("\nRIVER: ")
    
    for crd in river:
        time.sleep(0.1)
        print("\n["+crd.name+"] of ["+crd.suit.upper()+"]")
    print("\n")
    
    if crosscheck():
        
        for p in plrs:
            
            if not p.id in folded_players:
                chuck = p.id # chuck variable stores the player id of the only player who didn't fold.
                
    for elem in plrs:

        time.sleep(0.1)
        print("\n"+elem.alias_+":\n")
        time.sleep(0.1)
        print("Cash: "+str(elem.cash))

        # (Below) Prints cards for those who didn't fold and if 'chuck' wants to show his cards.
        if (not elem.id in folded_players or elem.is_ai) and not (elem.id == chuck and not elem.show_cards):
            time.sleep(0.1)
            print("Hand rank: ",elem.current_rank," Card rank: ",elem.card_rank)
            
            for c in elem.hand:
                time.sleep(0.1)
                print(f"[{c.name}] of [{c.suit.upper()}]")

def choose_card_from_deck():
    """Returns a randomly chosen card, with the randomseed set to the current time when the method is called."""
    
    random.seed(time.time())
    crd = deck.pop(random.randint(0,len(deck)-1))
    
    return crd

def set_initial_river():
    """Handles the flop round."""
    
    random.seed(time.time())
    deck.pop(random.randint(0,len(deck)-1)) # Burn a card.
    
    for i in range(3):
        storage = choose_card_from_deck()
        river.append(storage)

def next_card():
    """Flips the next card."""
    
    random.seed(time.time())
    deck.pop(random.randint(0,len(deck)-1))
    storage = choose_card_from_deck()
    river.append(storage)

def main_loop():
    """This method handles the macro structure of the game."""

    global percent
    global percent_memory
    global rounds_counter
    
    river.clear()
    folded_players.clear()

    # Deal cards
    for p in players:
        
        p.hand.clear()
        p.hand.append(choose_card_from_deck())
        p.hand.append(choose_card_from_deck())

    # ********************************
    # DEBUGGER will force program to ignore usual game rules when set to True.
    if DEBUGGER:
        players[0].hand[0] = mod.Card('2','clubs')
        players[0].hand[1] = mod.Card('10','diamonds')
        players[1].hand[0] = mod.Card('2','hearts')
        players[1].hand[1] = mod.Card('queen','clubs')
        river.append(mod.Card('2','spades'))
        river.append(mod.Card('2','diamonds'))
        river.append(mod.Card('9','diamonds'))
        river.append(mod.Card('king','spades'))
        river.append(mod.Card('ace','hearts'))
    # ********************************

    blinds[0] = True
    
    if rounds_counter % 5 == 0:
        percent += percent_memory
        print("\n\n\nBIG BLIND HAS BEEN CHANGED TO "+str(round(starters*(percent/100)))+". BLINDS CHANGE EVERY 5 ROUNDS.\n\n\n")
        
    set_blinds() #                      1. PRE FLOP
    check_inputs(players) #                             1) Player Input
    blinds[0] = False

    print("\nPot: "+str(pot))

    if not DEBUGGER:
        set_initial_river() #           2. FLOP
    
    check_inputs(players) #                             2) Player Input

    print("\nPot: "+str(pot))

    if not DEBUGGER:
        next_card() #                   3. RIVER

    check_inputs(players) #                             3) Player Input

    print("\nPot: "+str(pot))

    if not DEBUGGER:
        next_card() #                   4. RIVER

    check_inputs(players) #                             4) Player Input

    print("\n")
    for a in range(4):
        txt = "> Finding the winner" + ('.' * a)
        print(txt, end="\r")
        time.sleep(0.8)

    find_winner(players, players.copy()) # LOCATE WINNER

    list_hands(players)

    # (Below) Rotates the order. First is now last, second is now first.
    players.append(players.pop(0))



def repopulate_deck():
    """This method clears the (ref) deck (ref) data structure and repopulates it with 52 unique playing cards."""
    
    deck.clear()
    suit = ""
    
    for i in range(4): # 4 sets of suits for all 52 cards.
        
        if i == 0:
            suit = "spades"
        elif i == 1:
            suit = "clubs"
        elif i == 2:
            suit = "hearts"
        elif i == 3:
            suit = "diamonds"

        for x in range(14): # 13 cards per suit.
            
            if x < 9:
                deck.append( mod.Card(str(x+2),suit) )
            elif x == 10:
                deck.append(mod.Card('jack',suit))
            elif x == 11:
                deck.append(mod.Card('queen',suit))
            elif x == 12:
                deck.append(mod.Card('king',suit))
            elif x == 13:
                deck.append(mod.Card('ace',suit))




# The code below handles game set up by user input, and then starts the main loop.

# Tournament style poker. The program will end once only one player is left standing.

if __name__ == '__main__':
    TE = True

    if input("Tournament style (y/n)? ") == "y":
        TOURNAMENT_STYLE = True
    if input("Computer or Player mode (c/p)? ") == "c":
        AI_ON = True
    
    while TE: # The game setup loop.
        
        try:
            amt = input("\nType number of players participating in game: ")
            amt = int(amt)
            if amt < 2:
                int("a")
            amt2 = input("\nType start cash for each player: ")
            amt2 = int(amt2)
            if amt2 < 50:
                amt2 = 50
            starters = amt2
            
            for i in range(amt):
                players.append(plr.Player(amt2))
                ali = input("Enter alias for player "+str(i)+": ")
                players[i].id = i
                players[i].alias_ = ali
                if AI_ON and i > 0:
                    players[i].is_ai = True
                
            highest_id = amt - 1

            # Exit
            TE = False
            
        except:
            print("\nInvalid value! Please enter an integer.")

    TE = True

    local_count = 0
    
    while TE: # The main gameplay loop.

        
        for p in players: # Clear any leftover player stats from the previous round.     
            p.current_rank = 0
            p.card_rank = 0
            p.total_bet = 0
            p.all_in = False
            p.called = False
            p.show_cards = False
            p.tied_hand.clear()

            if p.cash < 1:
                p.cash = 0
            if p.cash <= 0:
                players.remove(p)
                
        if len(players) <= 1:
            print("\n\n\nGame Over! "+players[0].alias_+" has won the game!\n\n\n")

            # Exit
            TE = False
            
        if TE:
            local_count += 1
            prompt = ""
            if local_count % 2 == 0 and not TOURNAMENT_STYLE:
                prompt = input("\nWould you like to add more players to the table? Type \'yes\', dafault is no (hit enter): ")
            if prompt == 'yes':
                
                while True:
                    try:
                        
                        amt = input("\nType number of players to add: ")
                        amt = int(amt)
            
                        for i in range(amt):
                            players.append(plr.Player(starters))
                            ali = input("Enter alias for player "+str(highest_id+i+1)+": ")
                            players[-1].id = highest_id+i+1
                            players[-1].alias_ = ali
                        highest_id += amt
                        break
                    
                    except:
                        print("\nInvalid value! Please enter an integer.")
                        

            rounds_counter += 1
            print("\n\n\nRound "+str(rounds_counter)+". Players left: "+str(len(players))+"\n")
            # Shuffle
            repopulate_deck()
            input("Hit enter when you want to begin the next round.")
            # (Below) THIS IS THE MAIN ENTRY POINT OF THE NESTED GAMEPLAY HANDLING
            main_loop()








            
