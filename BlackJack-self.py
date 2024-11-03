import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 40


def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card


def calculatePoint(cards):
    return sum(cards)


def main():
    user_cards, banker_cards = list(), list()

    # init cards
    for _ in range(2):
        user_cards.append(deal_card())
        banker_cards.append(deal_card())

    print(f'莊家的明牌：{banker_cards[1]}')
    print(f"玩家的牌：{user_cards}，總共點數為:{calculatePoint(user_cards)}")
