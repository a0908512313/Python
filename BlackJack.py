import random

# all cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4


# deal card
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card


# calculate points
def calculate_points(cards):
    total_points = sum(cards)
    return total_points

    # 2 card
    if len(cards) == 2:
        return total_points

    if total_points > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
    return total_points


# game program
def play_jackblack():

    # define card
    dealer_cards = []
    user_cards = []

    # first deal card
    for i in range(2):
        dealer_cards.append(deal_card())
        user_cards.append(deal_card())
    print(f"莊家的明牌：{dealer_cards[1]}")
    print(f"玩家的牌：{user_cards}，總共點數為:{calculate_points(user_cards)}")
    while 11 in user_cards:
        eleven_one_ask = input('抽到11了!輸入11，A當11 ; 輸入1，A當1:')
        if eleven_one_ask == "11":
            print(f"玩家的牌：{user_cards}，總共點數為:{calculate_points(user_cards)}")
            break
        elif eleven_one_ask == "1":
            user_cards.remove(11)
            user_cards.append(1)
            print(f"玩家的牌：{user_cards}，總共點數為:{calculate_points(user_cards)}")
            break
        else:
            print("請重新輸入")
            print('輸入11，A當11 ; 輸入1，A當1:')

    # player
    ask_for_card = " "
    while ask_for_card != "n":
        ask_for_card = input('輸入y加牌，輸入n看結果:')

        if ask_for_card == "y":
            b = deal_card()
            user_cards.append(b)
            while b == 11:
                eleven_one_ask = input('抽到11了!輸入11，A當11 ; 輸入1，A當1:')
                if eleven_one_ask == "11":
                    print(f"玩家的牌：{user_cards}，總共點數為:{
                          calculate_points(user_cards)}")
                    break
                elif eleven_one_ask == "1":
                    user_cards.remove(11)
                    user_cards.append(1)
                    print(f"玩家的牌：{user_cards}，總共點數為:{
                          calculate_points(user_cards)}")
                    break
                else:
                    print("請重新輸入")
                    print('輸入11，A當11 ; 輸入1，A當1:')
            user_points = calculate_points(user_cards)
            if user_points > 21:
                if 11 in user_cards:
                    user_cards.remove(11)
                    user_cards.append(1)
                else:
                    ask_for_card = "n"
            elif user_points == 21:
                ask_for_card = "n"
            else:
                print(f"玩家的牌:{user_cards}，總共點數為:{
                      calculate_points(user_cards)}")

        elif ask_for_card == "n":
            user_points = calculate_points(user_cards)
            print(f"玩家的牌:{user_cards}，總共點數為:{calculate_points(user_cards)}")
        else:
            print("請重新輸入，輸入y加牌，輸入n看結果")

    # dealer
    dealer_points = calculate_points(dealer_cards)
    while dealer_points < 12:
        # deal card
        dealer_cards.append(deal_card())
        dealer_points = calculate_points(dealer_cards)

        if user_points > 21:
            if 11 in dealer_cards:
                dealer_cards.remove(11)
                dealer_cards.append(1)
            break

        while 11 in dealer_cards:
            y = deal_card()
            deal_card.append(y)
            cards.remove(y)
            dealer_points = calculate_points(dealer_cards)
            if dealer_points > 21:
                dealer_cards.remove(11)
                dealer_cards.append(1)
        dealer_points = calculate_points(dealer_cards)

    # user & dealer points display
    print("")
    print(f"莊家的牌:{dealer_cards}，總共點數為:{dealer_points}")
    print(f"玩家的牌:{user_cards}，總共點數為:{user_points}")

    # chech win or lose
    if user_points > 21:
        print("你輸了")
    elif dealer_points > 21:
        print("你贏了")
    elif user_points == dealer_points:
        print("平手")
    elif user_points > dealer_points:
        print("你贏了")
    else:
        print("你輸了")


# main
play_game = True
print("歡迎來到21點遊戲(若抽到A則當下必須選擇當1或當11，選擇後不得更改!!!)")
play_jackblack()

while play_game == True:
    print("=======================================")
    user_input = input("輸入y繼續，輸入n結束:")
    if user_input == "y":
        play_jackblack()
    elif user_input == "n":
        play_game = False
        print("bye~")
    else:
        continue
