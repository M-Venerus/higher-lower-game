from assets import data
from random import randint

def greeting():
    print("Welcome to celebrity guessing game!\n\nYou have to guess which celebrity has more followers!")

def selection():
    data_index = randint(0, len(data) - 1)
    celeb = data[data_index]
    data.pop(data_index)
    return celeb

def compare(celeb_1, celeb_2):
    print(f"Celebrity 1: {celeb_1['name']}, a {celeb_1['description']}, from {celeb_1['country']}.")
    print("VS")
    print(f"Celebrity 2: {celeb_2['name']}, a {celeb_2['description']}, from {celeb_2['country']}.")
    if celeb_1['follower_count'] == celeb_2['follower_count']:
        return 0
    if celeb_1['follower_count'] > celeb_2['follower_count']:
        return 1
    if celeb_1['follower_count'] < celeb_2['follower_count']:
        return 2

def guess(celeb_better):
    user_guess = int(input("Which celebrity has more followers? Type '1' or '2': "))
    if celeb_better == 0:
        return True
    elif user_guess == celeb_better:
        return True
    else:
        return False 

def display_score(score, celeb_1, celeb_2):
    print(f"\nYou're right! {celeb_1['name']} has {celeb_1['follower_count']},000 followers, while {celeb_2['name']} has {celeb_2['follower_count']},000 followers.")
    score += 1
    print(f"Current score: {score}.")
    return 1

def end_game(score, celeb_1, celeb_2):
    print(f"\nSorry, that was incorrect. {celeb_1['name']} has {celeb_1['follower_count']},000 followers, while {celeb_2['name']} has {celeb_2['follower_count']},000 followers.")
    print(f"Final score = {score}.")
    

def main():
    greeting()
    celeb_1 = selection()
    game_running = True
    score = 0

    while game_running:
        celeb_2 = selection()
        celeb_better = compare(celeb_1, celeb_2)
        right_or_wrong = guess(celeb_better)
        if right_or_wrong:
            score += display_score(score, celeb_1, celeb_2)
            celeb_1 = celeb_2
        else:
            game_running = False
    end_game(score, celeb_1, celeb_2)

main()

       

