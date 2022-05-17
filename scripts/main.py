from codecs import BOM_BE
from mimetypes import guess_type
from operator import is_


class Card:
    def __init__(self):
        self.number = 0
        self.suit = "undef"
    '''def __init__(self,n,s):
        self.number = n
        self.suit = s
    '''
    def print_card(self):
        print (str(self.number) + " of " + self.suit)
class Player:
    name = "undeclared"
    deck = []
    busted = False

global_deck = []
dealer_deck = []
suits = ["hearts", "diamonds", "clubs", "spades"]
player = Player()
player.name = "bob"

def generate_cards():
    for num in range(1,13):
        for suit in range(len(suits)):
            new_card = Card()
            new_card.number = num
            new_card.suit = suits[suit] 
            global_deck.append(new_card)
            
def shuffle_deck():
    pass

def distribute_cards():       #give player 2 cards and dealer 2 cards
    player.deck.append(global_deck[0])
    global_deck.pop(0)
    player.deck.append(global_deck[0])
    global_deck.pop(0)

    dealer_deck.append(global_deck[0])
    global_deck.pop(0)
    dealer_deck.append(global_deck[0])
    global_deck.pop(0)
    

def show_dealer_card(index):
    dealer_deck[index].print_card()

def hit(cards):
    print ("Hitting...")
    cards.append(global_deck[0])
    global_deck[0].print_card()
    global_deck.pop(0)
    return cards

def stand():
    pass

def double_down(cards):
    hit(cards)
    return cards

def check_is_bust(cards):
    sum = 0
    for card in cards:
        sum += card.number
    if sum > 21:
        return True
    return False

def sum_deck(cards):
    sum = 0
    for card in cards:
        sum += card.number
    return sum
    

def check_is_over_threshold(cards,threshold=17):
    sum = 0
    for card in cards:
        sum += card.number
    if sum > threshold:
        return True
    return False

def did_player_win(player_cards):
    player_sum = sum_deck(player_cards)
    dealer_sum = sum_deck(dealer_deck)
    if player_sum >= dealer_sum:
        return True
    return False

valid_commands = ["s", "h", "d"]

def player_logic():          #takes input of player hit, stand, or doubledown
    is_double_down = False
    while not check_is_bust(player.deck) and not is_double_down:
        print("my cards are")
        print("_________________________")
        for card in player.deck:
            card.print_card()
        print("_________________________")
        com = input("Enter (S)Stand, (H)Hit, (D)Double Down")
        com = com.lower()
        if not com in valid_commands:
            continue 
        if com == "s":
            stand()
            return
        elif com == "h":
            player.deck = hit(player.deck)
        else:
            player.deck =double_down(player.deck)
            is_double_down = True
    if check_is_bust(player.deck):
        print ("You Busted!")
        player.busted = True
        return
    if is_double_down:
        return

def dealer_logic(dealer_deck):
    show_dealer_card(1)
    while not check_is_over_threshold(dealer_deck,17):
        dealer_deck = hit(dealer_deck)
    if check_is_bust(dealer_deck):
        if player.busted:
            print ("Player Loses!")
        else:
            print ("Player Wins!")
    else:
        if player.busted:
            print ("Player Loses!")
        elif did_player_win(player.deck):
            print("Player Wins!")
        else:
            print("Player Loses!")

generate_cards()
shuffle_deck()
distribute_cards()
show_dealer_card(0)
player_logic()
dealer_logic(dealer_deck)

