#Possible additional future use; for now only appears in final message should the player achieve the good ending
name = input("Enter your name: ")

#Main() function. Contains nearly all text that the player will see in the game, and calls the functions for each choice
def main():
    print('\nWelcome to "Actual Cannibal Shia Labeouf":\nA text based adventure game by Joshua Capron.\nBased on the song by Rob Cantor.')
    print("\nA few things to keep in mind:\nEach choice requires only a one or two-word input\nYou have unlimited chances to input something valid; you'll only get game over if you make a wrong choice\nIf you're familiar with the original song, then you should do well.\nNow let's see if you can survive.")
    print("\nYou're walking in the woods. There's no one around, and your phone is dead.")
    segment1()
    print("He's following you, about thirty feet back.\nHe gets down on all fours and breaks into a sprint.\nHe's gaining on you!\nShia Labeouf.")
    print("You're looking for your car but you're all turned around.\nHe's almost upon you now\nAnd you can see there's blood on his face.\nMy gosh, there's blood everywhere!")
    segment2()
    print("Now it's dark, and you seem to have lost him\nBut you're hopelessly lost yourself\nStranded, with a murderer\nYou creep silently through the underbrush\nAha! In the distance\nA small cottage with a light on\nHope!\nYou move stealthily toward it\nBut your leg!\nAh!\nIt's caught in a bear trap!")
    segment3()
    print("Now you're on the doorstep\nSitting inside\nShia Labeouf\nSharpening an axe\nIt's Shia Labeouf\nBut he doesn't hear you enter\nShia Labeouf")
    segment4()
    print("Fighting for your life\nwith Shia Labeouf\nWrestling a knife\nfrom Shia Labeouf\nStab him in his kidney\nSafe at last from Shia Labeouf")
    segment5()
    print("\nHis head topples to the floor, expressionless\nYou fall to your knees and catch your breath\nYou're finally safe from Shia Labeouf\n")
#used exit() instead of print() so that the game could be forced ended once this line is read; used to fix a rare
#bug where certain lines of main() would be reread after the good ending is achieved for unknown reasons.
    exit(f"Congratulations {name}! You've completed the game and escaped alive!")
    
#each of the functions below represent the individual choices in the game. Main() calls all of them as the player
#progresses, and their separation into functions allows for the game_over() function to recall any of them.
def segment1():
    choice = input("\nYou feel a presence behind you.\n")
#there will be a copious amount of "correct inputs" for each choice to account for most things that players may think of
    if choice.lower() == "turn around" or choice.lower() == "turn" or choice.lower() == "look back" or choice.lower() == "pivot" or choice.lower() == "turn back":
        print("\nOut of the corner of your eye, you spot him.\nShia Labeouf.")
    else:
        print("You cannot do that right now.")
        segment1()

def segment2():
    choice = input("\nYou can feel your fight or flight responses kicking in. Which one will you heed?\n")
    if choice.lower() == "flight" or choice.lower() == "run" or choice.lower() == "run away" or choice.lower() == "flee" or choice.lower() == "escape":
        print("\nRunning for your life\nFrom Shia Labeouf\nHe's brandishing a knife\nIt's Shia Labeouf\nLurking in the shadows\nHollywood superstar Shia Labeouf\nLiving in the woods\nShia Labeouf\nKilling for sport\nShia Labeouf\nEating all the bodies\nActual Cannibal Shia Labeouf\n")
    elif choice.lower() == "fight" or choice.lower() == "hold ground" or choice.lower() == "stand ground" or choice.lower() == "raise fists" or choice.lower() == "attack" or choice.lower() == "fight him" or choice.lower() == "fight shia" or choice.lower() == "attack shia" or choice.lower() == "attack him":
        print("\nYou try to stand your ground. But once he reaches you, you are no match for his immense strength.\nHe forces you to the ground, and your weak body loses consciousness as you are eaten alive.\nGAME OVER\n")
        game_over(segment2)
    else:
        print("You cannot do that right now.")
        segment2()

def segment3():
    choice = input("\nYou don't have much time to escape.\n")
    if choice.lower() == "eat leg" or choice.lower() == "eat" or choice.lower() == "gnaw leg" or choice.lower() == "gnaw" or choice.lower() == "bite leg" or choice.lower() == "bite" or choice.lower() == "chew leg" or choice.lower() == "chew":
        print("\nGnawing off your leg\nQuiet quiet\nLimping to the cottage\nQuiet quiet")
    elif choice.lower() == "open trap" or choice.lower() == "pry trap" or choice.lower() == "free self" or choice.lower() == "free myself" or choice.lower() == "release trap" or choice.lower() == "release leg" or choice.lower() == "free leg":
        print("\nYou try to pry open the trap with your bare hands. It is much too tight, and you cannot do it alone.\nAfter trying for too long, you hear the cracking of a branch just in front of you. You look up to see him.\nShia Labeouf.\nHe approaches you with an axe in hand as you are helpless to escape.\nGAME OVER\n")
        game_over(segment3)
    else:
        print("You cannot do that right now.")
        segment3()

def segment4():
    choice = input("\nThis could be your chance! But your stump leg leaves you in a weakened state. Is it worth it?\n")
    if choice.lower() == "yes" or choice.lower() == "sneak" or choice.lower() == "sneak up" or choice.lower() == "sneak attack" or choice.lower() == "fight" or choice.lower() == "fight him" or choice.lower() == "fight shia" or choice.lower() == "attack" or choice.lower() == "attack him" or choice.lower() == "attack shia" or choice.lower() == "strangle him" or choice.lower() == "strangle shia":
        print("\nYou're sneaking up behind him\nStrangling superstar Shia Labeouf")
    elif choice.lower() == "no" or choice.lower() == "run" or choice.lower() == "run away" or choice.lower() == "flee" or choice.lower() == "escape":
        print("\nAs you try to leave, you step on an uneven floorboard that makes an obvious creaking noise.\nThe killer looks up from his whetstone and catches you.\nYour stump leg doesn't allow you to travel very fast, and he easily catches up to you before taking a swing with his axe.\nGAME OVER\n")
        game_over(segment4)
    else:
        print("You cannot do that right now.")
        segment4()

def segment5():
    choice = input("\nAs you begin to leave the scene, you notice his axe left on the floor.\nYour stalker may be defeated, but you never know what else is out there.\nBut will your stump leg allow you to carry such a weapon?\n")
    if choice.lower() == "yes" or choice.lower() == "take axe" or choice.lower() == "grab axe" or choice.lower() == "acquire axe" or choice.lower() == "take":
        print("\nAxe added to inventory.")
        print("\nYou limp into the dark woods\nBlood oozing from your stump leg\nYou've beaten Shia Labeouf\n")
        print("Wait! He isn't dead!\nShia surprise\nThere's a gun to your head\nAnd death in his eyes\nBut you can do jiu-jitsu\nBody slam superstar Shia Labeouf\n")
        print("Legendary fight with Shia Labeouf\nNormal Tuesday night for Shia Labeouf\nYou try to swing an axe at Shia Labeouf\nBut the blood is draining fast from your stump leg\n")
        print("He's dodging every swipe\nHe parries to the left\nYou counter to the right\nYou catch him in the neck\nYou're chopping off his head now\nYou have just decapitated Shia Labeouf")
#easily the most detailed bad ending; attempted to use the same rhythm as the real ending but with different lyrics
#to instead portray a gruesome fate for the player
    elif choice.lower() == "no" or choice.lower() == "leave" or choice.lower() == "leave axe" or choice.lower() == "escape" or choice.lower() == "ignore" or choice.lower() == "ignore axe":
        print("\nYou leave the axe behind.")
        print("\nYou limp into the dark woods\nBlood oozing from your stump leg\nYou've beaten Shia Labeouf\n")
        print("Wait! He isn't dead!\nShia surprise\nThere's a gun to your head\nAnd death in his eyes\nBut you can do jiu-jitsu\nBody slam superstar Shia Labeouf\n")
        print("Legendary fight with Shia Labeouf\nNormal Tuesday night for Shia Labeouf\nYou failed to grab the axe from Shia Labeouf\nAnd the blood is draining fast from your stump leg\n")
        print("He's dodging every blow\nHe parries to the left\nYou miss a larger throw\nHe grabs you by the neck\nHe's forcing you to the ground\nYou are being pummeled now by Shia Labeouf\n")
        print("As you witness your sight fade, into darkness\nYou know there is nothing you can do\nYou couldn't escape from Shia Labeouf\nGAME OVER\n")
        game_over(segment5)
    else:
        print("You cannot do that right now.")
        segment5()

#game_over() is an independent function that can either redo the most recent choice or restart the game; only called
#when the player makes a wrong choice and dies.
def game_over(segment):
    choice = input("You died.\nType REDO to return to your last choice, or RESTART to start over from the beginning.\n")
    if choice.lower() == "redo":
        segment()
    elif choice.lower() == "restart":
        main()
    else:
        print("Invalid input.\n")
        game_over(segment)

#calls the main() function to officially begin the program.
main()