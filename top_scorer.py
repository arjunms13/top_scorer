"""
Top scorer is a game played by rolling die. The number shown in the die is equivalent to scores and the winner
is the one who scores the most after the certain number of rolls.
"""
import random
ROLL = 6
def main():
    # Game description
    print("\nTop scorer is a game played by rolling die. The number shown in the die is equivalent to scores and "
          "the winner \nis the one who scores the most after the certain number of rolls.")

    # List & dictionary of players
    players_list = ['Mehran', 'Chris', 'Lauren', 'Karel']
    players_intro = { 'Mehran' : 'current leader of the Jedi order.', 'Chris' : ' proud buddy of Simba.',
                'Lauren': ' most patient section leader.','Karel': ' soft spoken robot.'}

    # Name of the user.
    your_name = input("\nEnter your name : ")

    # Number of players playing against.
    num_of_players = int(input("\nEnter the numbers of players you want to play against (1-4) : "))

    # Print the name of opponents.
    for i in range(num_of_players):
        print("\nThe player " + str (i+1) + " is " + players_list[i] + ".")

    # Asking for intro and printing it.
        know_more = str(input("\nPress enter key to know more about " + players_list [i] + ": "))
        print(players_list[i] + " is the " + players_intro.get(players_list[i]))

    # Putting 0 score for players who are not playing.
    if num_of_players < len(players_intro):
        for i in range (len(players_intro) - num_of_players):
            players_intro[players_list[(i+num_of_players)]]=0

    # The number of times the die is rolled.
    times = int(input("\nEnter the number of die rolls: "))

    # The score each opponent has scored.
    for i in range(num_of_players):
        opponent_score = int(times * random.uniform(1,ROLL))
        players_intro[players_list[i]] = opponent_score
        print(players_list[i] + " has scored " + str (opponent_score) +".")

    # Getting all the scores.
    all_scores = players_intro.values()

    # Score to beat.
    score_to_beat = int(max(all_scores)) + 1
    print(str(your_name) + "," + " you need " + str(score_to_beat) + " to be the top scorer.")
    total = 0

    # Rolls the die for given times.
    for i in range(times):
        input("Press enter key to roll die : ")

        # Roll_dice generates a random dice roll.
        roll_dice = random.randint(1,ROLL)
        print("You rolled " + str(roll_dice)+".")

        # Add the score
        total+= roll_dice
        print("Your total Score is " + str(total) + ".")

        # Match ends scenario 1
        if total >= (max(all_scores)+1) :
            print("Well done " + str(your_name) + ", you are the top scorer.")
            break

        # Score required from remaining rolls.
        else:
            # Avoiding the print statement when there are no rolls remaining.
            if (times-(i+1)) != 0:
                print("You need " + str((max(all_scores)+1)-total) + " from " + str(times -(i+1)) + " rolls.")

    # Match ends scenario 2
    if total < (max(all_scores)):
        print("Hard Luck " + str(your_name) +"," + str(max(players_list,key=players_intro.get)) + " is the top scorer"
                                                                                                  " this time.")

    # Match ends scenario 3
    if total == max(all_scores):
        print("The scores are tied! Both you & " + str(max(players_list,key=players_intro.get)) + "are top scorers!")




if __name__ == '__main__':
    main()
