from DeckOfCards import *
import time
import sys
# show cards and shuffle cards

deck.print_deck()

deck.shuffle_deck()
play_again = "y"
while play_again == "y":
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")


    deck.print_deck()
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("-------------")
    print("Welcome! Get ready to play Blackjack!")
    time.sleep(2)

    print("Let me deal the hands...")
    time.sleep(2)


    # deal hands
    Userhand = []
    Househand = []

    Userhand.append(deck.deck.pop(0))
    Userhand.append(deck.deck.pop(0))

    Househand.append(deck.deck.pop(0))
    Househand.append(deck.deck.pop(0))


    # make it so we can see the scores of both the house and user

    def get_card_value(card):

        if card.face == "2":
            card_value = 2

        elif card.face == "3":
            card_value = 3

        elif card.face == "4":
            card_value = 4

        elif card.face == "5":
            card_value = 5

        elif card.face == "6":
            card_value = 6

        elif card.face == "7":
            card_value = 7

        elif card.face == "8":
            card_value = 8

        elif card.face == "9":
            card_value = 9

        elif card.face == "10":
            card_value = 10

        elif card.face == "Jack":
            card_value = 10

        elif card.face == "Queen":
            card_value = 10

        elif card.face == "King":
            card_value = 10

        elif card.face == "Ace":
            card_value = 11

        return card_value

    def get_hand_value(hand):
        hand_value = 0 
        for i in hand:
            hand_value += get_card_value(i)
        Ace_count = 0
        for i in hand:
            if i.face == "Ace":
                Ace_count += 1
        while hand_value > 21 and Ace_count > 0:
            hand_value = hand_value - 10
            Ace_count = Ace_count - 1
        return hand_value



    userscore = get_hand_value(Userhand)
    housescore =get_hand_value(Househand)
    print("I have now delt the hands here is your hand")
    def print_hand_and_score(hand):
        for card in hand:
            time.sleep(1)
            print(card.face, "of", card.suit)
            time.sleep(1)
        hand_value = get_hand_value(hand)
        print("Current score is", hand_value)


    def finding_hand_ending_score(Househand):
        housescore = get_hand_value(Househand)

        print("The House's turn...")
        time.sleep(2)

        print_hand_and_score(Househand)

        while housescore < 17:
            time.sleep(2)
            print("The House hits!")
            
            Househand.append(deck.deck.pop(0))
            housescore = get_hand_value(Househand)

            time.sleep(1)
            print_hand_and_score(Househand)
        return housescore

    def playing_game_function():
        Hit_or_pass = "y"
        while Hit_or_pass == "y":
            print_hand_and_score(Userhand)
            Hit_or_pass = input("would you like to Hit? (y/n)")
            if Hit_or_pass == "y":
                Userhand.append(deck.deck.pop(0))
                if get_hand_value(Userhand) > 21:
                    print("You lose your score is over 21!!!!")
                    return

            else:
                print("Alright let's see what the House score and hand is.")

                house_end_score = finding_hand_ending_score(Househand)
                User_end_score = get_hand_value(Userhand)

                if User_end_score > 21:
                            print("The House wins! You busted.")

                elif house_end_score > 21:
                            print("You win! The House busted.")

                elif User_end_score > house_end_score:
                            print("You win!")

                elif house_end_score > User_end_score:
                            print("The House wins!")

                else:
                            print("It's a tie!")

    playing_game_function()
    play_again = input("Would you like to play again? (y/n)")