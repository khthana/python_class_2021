import random
#* โปรแกรมแสดงหน้าไพ่
#* https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
#* 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
#* 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
#* 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
#* 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'

def display_card():
        suit = ("\u2660", "\u2665", "\u2666", "\u2663")
        #rank = 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
        rank = list("A23456789") + ["10"] + list("JQK")
        deck = []
        for s in suit:
                for r in rank:
                        deck.append(r + s)
        return deck

d = display_card()
print(d)
random.shuffle(d)
print(d)
p = random.sample(d, 3)
print(p)