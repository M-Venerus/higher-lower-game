from assets import data
from random import randint

def greeting():
    """Generate initial game greeting."""
    print("Welcome to celebrity guessing game!\n\nYou have to guess which celebrity has more followers!")

def selection():
    """Select and return a random dictionary from data list. Removes the dictionary from the list once selected."""
    data_index = randint(0, len(data) - 1)
    celeb = data[data_index]
    data.pop(data_index)
    return celeb

def compare(celeb_1, celeb_2):
    """Compare follower count between celebrity 1 and celebrity 2, and return appropriate result."""
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
    """Prompt user for input of guess for celebrity with more followers and compare the guess. Return True or false based on if user is correct."""
    user_guess = int(input("Which celebrity has more followers? Type '1' or '2': "))
    if celeb_better == 0:
        return True
    elif user_guess == celeb_better:
        return True
    else:
        return False 

def display_score(score, celeb_1, celeb_2):
    """Notify user of their correct answer along with information pertaining to why (celebrity follower numbers). Update score and print new score."""
    print(f"\nYou're right! {celeb_1['name']} has {celeb_1['follower_count']},000 followers, while {celeb_2['name']} has {celeb_2['follower_count']},000 followers.")
    score += 1
    print(f"Current score: {score}.")
    return 1

def end_game(score, celeb_1, celeb_2):
    """Notify user of their incorrect answer along with information pertaining to why (celebrity follower numbers). Display final score."""
    print(f"\nSorry, that was incorrect. {celeb_1['name']} has {celeb_1['follower_count']},000 followers, while {celeb_2['name']} has {celeb_2['follower_count']},000 followers.")
    print(f"Final score = {score}.")
    

def main():
    """Main function to run game."""
    greeting()
    celeb_1 = selection()
    game_running = True
    score = 0

    while game_running:
        celeb_2 = selection()
        celeb_better = compare(celeb_1, celeb_2)
        user_is_right = guess(celeb_better)
        if user_is_right:
            score += display_score(score, celeb_1, celeb_2)
            celeb_1 = celeb_2
        else:
            game_running = False
    end_game(score, celeb_1, celeb_2)

main()

       

