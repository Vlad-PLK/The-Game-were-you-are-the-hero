import sys
import random

print("welcome to my first game ")
name = input("What is your name ? ")
age = int(input("What is your age? "))
health = 10

monster_health = random.randint(1,10)


if age >= 18 :
    print("You are old enough to play! ")
    start = input("Do you want to play? ").lower()
    if start == "yes":
        print(f"You are staring with : {health} health \nLet's play")
        first_choice = input("First Choice... Left or Right? ").lower()
        if first_choice == "left":
            ans = input("You noticed a river and a bridge far from it, do you want to swim across or to go to the bridge ").lower()
            if ans == "across":
                health -= 5
                print("You decided to go across and you got stung by a jellyfish : health -5")
                print(f"{health} health left")
            elif ans == "bridge":
                print("Good choice dude, you lost a little bit of time but you managed to cross the river without issues")

            ans = input("Now you see a strange and dilapidated house, do you want to go into or to go around? (house, around) ").lower()
            if ans == "house":
                spider = input("As soon as you walked into it, a huge spider appears in front of you! Do you want "
                      "to fight this monster or to run away ? (fight, leave) ")
                if spider == "fight":
                    if health >= monster_health:
                        print("You run forward and smashed the spider like a boss, YOU WON THIS FIGHT ")
                    elif health < monster_health:
                        print("You smash the spider but it bit you with his poisonous fangs, YOU WON THIS FIGHT BUT AT WHAT COST...  \n "
                              f"Lose {monster_health - health} health  ")
                        if health <= 0:
                            print("You now have 0 health, game over...")

            elif ans == "around":
                around = input("You're too old for this shit, you passed your way")


        else:
            print("Wrong choice, you fell down and lost...")

    else:
        print("The game is closed")
        sys.exit()
