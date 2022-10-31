import random
import cards

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extention = 'png'
    else:
        extention = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extention}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = f"cards/{str(card)}_{suit}.{extention}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card of the top of deck
    next_card = deck.pop(0)
    # add it back to the deck
    deck.append(next_card)
    # add image to label and display
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    # calc the score of all cards in the hand
    # only one ace can have the score 11 rest are 1 if it goes over 21
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we go over 21 check ace and then subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Its a Draw")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if bust and theres an ace then -10
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # print(locals())


def init_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def restart():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, bg='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, bg='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    # list of dealers & players cards
    dealer_hand = []
    player_hand = []
    init_deal()


def shuffle():
    random.shuffle(deck)


def play():
    init_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry('1280x720')
mainWindow.configure(bg='green')
mainWindow['padx'] = 20

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken',
                           borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background="green",
              foreground='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green',
              foreground='white').grid(row=1, column=0)

# frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background='green',
              fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green',
              fg='white').grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, bg='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

newGame = tkinter.Button(button_frame, text="New Game", command=restart)
newGame.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)
print(cards)

# create a new deck of cards and shuffle em
deck = list(cards)
shuffle()
# list of dealers & players cards
dealer_hand = []
player_hand = []


if __name__ == "__main__":
    play()
