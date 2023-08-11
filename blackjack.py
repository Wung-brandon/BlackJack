import random

#a function that takes a list of cards as inputs and returns the sum 
def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    #card = random.choice(cards)
    card = random.sample(cards,2)
    #print(card)
    return card
    
def calculate__score(cards):
    #check for a blackjack (a hand with only 2 carsds: ace + 10) and return 0 instead of the actual score . 0 will represent a blackjack in our game
    #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #check for an ace(11). if the score is already above 21, remove 11 and replace it with a 1. you might use the append() and remove() functions
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)
    

user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    print(user_cards)
    computer_cards.append(new_card)
    print(computer_cards)
is_game = False

user_score = calculate__score(user_cards)
computer_score = calculate__score(computer_cards)
print(f'Your card: {user_cards} and curreent score: {user_score}')
print(f'computer card: {computer_cards[0]} and curreent score: {computer_score}')

if user_score == 0 or computer_score == 0 or user_score > 21: 
    is_game = True
#call the calculate_score function when the computer or user has a blackjack (0) or if the user's score is over 21 the game ends


""" user_cards = random.sample(cards,2) #picks random 2 numbers
computer_cards = random.sample(cards,2)
print(f'user card is {user_cards}')
print(f'computer card is {computer_cards}')


user_score = sum(user_cards)
commuter_score = sum(computer_cards)
print(f'user score is {user_score}')
print(f'computer score is {commuter_score}')

if user_score == commuter_score:
    print(f'Both scores {user_score} are the same. Its a draw!')
elif user_score == 20:
    print(f"You have a blackjack of {user_score} so you win!")
elif commuter_score == 20:
    print(f"computer have a blackjack of {commuter_score} so you lose!")
elif user_score > 21:
    print(f"You lose! {user_score} is over 21 ") """

    
