import random

print("BLACKJACK\n")


card_colors = ['clubs', 'spades', 'hearts', 'diamonds']
card_faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_name_and_value_pairs = dict(zip(card_faces, card_values))



class Card:
    def __init__(self, face, color):
        self.color = color
        self.face = face
        self.value = card_name_and_value_pairs[face]
        self.name = str(face) + ' of ' + str(color)


class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.wager = 0
        self.hand = []
        self.score = 0


deck = [Card(face, color) for face in card_faces for color in card_colors]


player_name = input("What is your name?: ")

player = Player(player_name)

dealer = Player("Dealer")


def bet(jatekos):
    print(f"\nBalance: {jatekos.balance}")
    wannabet = input("Would you like to place a bet?(y/n): ").lower()
    if wannabet == 'y':
        howmuch = input("How much would you like to bet?: ")
        if int(howmuch) <= jatekos.balance:
            print("Bet placed!")
            jatekos.wager = int(howmuch)
            jatekos.balance -= int(howmuch)
            print(f"Remaining balance: {jatekos.balance}")

    else:
        print("No bet placed")






def gameplay():
    deck_copy = deck
    random.shuffle(deck_copy)

    def card_draw():
        run = True
        while run:

            if not deck_copy:
                print("\nOut of cards!")
                quit()

            else:
                drawn_card = deck_copy.pop(0)
                return drawn_card

    def draw_phase(player_or_dealer):
        if player_or_dealer == dealer:
            print(f"\nDealer's hand({hand_value(dealer)}):\n")
            for cards in dealer.hand:
                print(f" * {cards.name} ({cards.value})")

            dealer_score = []
            for cards in dealer.hand:
                dealer_score.append(cards.value)

            if 21 >= sum(dealer_score) > player.score:
                print(f"\nBet lost! Dealer wins!")
                return
        
        while True:
            h_or_s = "h"
            if player_or_dealer == player:
                h_or_s = input("\nHit or Stay? (h/s): ").lower()
            if h_or_s == "h":
                new_card = card_draw()
                player_or_dealer.hand.append(new_card)
                print(f"\n{player_or_dealer.name} draws:\n * {new_card.name}, ({new_card.value})")
                if player_or_dealer == player:
                    player_hand = []
                    for cards in player.hand:
                        player_hand.append(cards.value)
                    if sum(player_hand) > 21:
                        if 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                    print(f"\nPlayer hand: {sum(player_hand)}")
                    
                    if sum(player_hand) == 21:
                        print("Player wins")
                        player.balance += player.wager * 2
                        return True
                    if sum(player_hand) > 21:
                        print(f"\n You lost!")
                        return True

                    continue
                if player_or_dealer == dealer:
                    dealer_hand = []
                    for cards in dealer.hand:
                        dealer_hand.append(cards.value)
                    print(f"\nDealer hand: {sum(dealer_hand)}")

                    if sum(dealer_hand) == 21:
                        print("Dealer wins")
                        break

                    if sum(dealer_hand) > 21:
                        if 11 in dealer_hand:
                            dealer_hand.remove(11)
                            dealer_hand.append(1)
                            continue
                        else:
                            print("Dealer busts! You win!")
                            player.balance += player.wager * 2
                            break
                    if sum(dealer_hand) > player.score:
                        print("Dealer wins!")
                        break
                    continue

            if h_or_s == "s":
                player_score = []
                for cards in player.hand:
                    player_score.append(cards.value)

                player.score = sum(player_score)
                return False


    def hand_value(player_or_dealer):
        list_of_values = []

        for cards in player_or_dealer.hand:
            list_of_values.append(cards.value)

        if sum(list_of_values) == 2:
            list_of_values.pop(0)
            list_of_values.append(11)

            
        if sum(list_of_values) > 2:
            if 1 in list_of_values:
                for cards in player_or_dealer.hand:
                    if cards.value == 1:
                        cards.value = 11
                list_of_values.remove(1)
                list_of_values.append(11)


        return sum(list_of_values)


    dealer.hand.append(card_draw())
    dealer.hand.append(card_draw())

    print(f"Dealer hand:\n\n * {dealer.hand[0].name} ({dealer.hand[0].value})")
    print(" * Unknown")

    bet(player)

    player.hand.append(card_draw())
    player.hand.append(card_draw())
    print(f"\n{player.name}'s hand({hand_value(player)}):\n")
    for card in player.hand:
        print(f" * {card.name} ({card.value})")

    did_i_just_lost = draw_phase(player)

    if did_i_just_lost is False:
        draw_phase(dealer)


def game(jatekos, oszto):
    jatekos.balance = 1000

    while True:
        start = input("Would you like to playa new game? y/n: ")
        if start == "y":
            gameplay()
            jatekos.score = 0
            jatekos.hand = []
            jatekos.wager = 0
            oszto.score = 0
            oszto.hand = []

        elif start == "n":
            quit()

        else:
            continue


game(player, dealer)

