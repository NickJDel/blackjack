import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

game_active = True
player_turn = True
dealer_turn = True
replay = False
 
def add_card(card_list):

                card_list.append(random.choice(cards))

 
def hand_count(hand):

    count = 0

    for card in hand:

                    count += card

    return count


while game_active:

    player_hand = []
    dealer_hand = []
    player_count = 0
    dealer_count = 0
    add_card(player_hand)
    add_card(player_hand)
    add_card(dealer_hand)
    print(player_hand)
    print(dealer_hand)             

    while player_turn:

        card_draw = input("Type Y for another card, or anything else to stand")
        if card_draw.lower() == "y":
            add_card(player_hand)
            print(player_hand)
            player_count = hand_count(player_hand)
            print(player_count)
            if player_count > 21:
                print("Your hand is a bust, the Dealer wins!")
                game_active = False
                player_turn = False
        elif card_draw.lower() == "n":
            player_count = hand_count(player_hand)
            player_turn = False

    while dealer_turn:

        add_card(dealer_hand)
        dealer_count = hand_count(dealer_hand)
        print(dealer_hand)
        if dealer_count > 21:

            print("Dealer has gone bust, Player wins!")
            game_active = False
            dealer_turn = False

        elif dealer_count > player_count:

            print("Dealer wins!")
            game_active = False
            dealer_turn = False
        elif dealer_count == player_count:
            print("Dealer wins on a draw!")
            game_active = False
            dealer_turn = False
    print(f"Player: {player_count} Dealer: {dealer_count}")
    replay_input = input("Y to play again or N to exit")
    if replay_input.lower() == "y":
        game_active = True
        player_turn = True
        dealer_turn = True
        #else:

            #print("Player Wins!")
            #game_active= False
            #dealer_turn = False