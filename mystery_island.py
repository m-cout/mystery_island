# the legendary mystery island mini-text adventure game!

from sys import exit

# triggered after victory
def win():
    print("Congratulations! You won!")
    print("You probably avoided the extinction of the human race.")
    print("")
    print("This game was developed by Marcus Couto.")
    print("twitter.com/marcvs")
    print("mvcoutob@gmail.com")
    print("github.com/m-cout")
    print("")
    print("Play again?")
    while True:
        choice = input('> ')

        if 'yes' in choice.lower():
            start()
        elif 'no' in choice.lower():
            print("Thanks for playing! See you soon!")
            exit(0)
        else:
            print("Yes or No?")

# triggered in case of death
def die():
    print("That's it. You are dead.")
    print("")
    print("This game was developed by Marcus Couto.")
    print("twitter.com/marcvs")
    print("mvcoutob@gmail.com")
    print("github.com/m-cout")
    print("")
    print("Play again?")
    while True:
        choice = input('> ')

        if 'yes' in choice.lower():
            house()
        elif 'no' in choice.lower():
            print("Thanks for playing! See you soon!")
            exit(0)
        else:
            print("Yes or No?")

def start():
# these are the items collected through the game
    global flash
    flash = False
    global knife
    knife = False
    global bamboo
    bamboo = False
    global vine
    vine = False
    global board
    board = False
    global rope1
    rope1 = False
    global rope2
    rope2 = False
    global hook
    hook = False
    global moss
    moss = False
    global aquatic_plant
    aquatic_plant = False
    global mushroom
    mushroom = False
    global key
    key = False
    global gun
    gun = False
# these variables check if some items have already been seen by the player in certain scenarios
    global skeleton_seen
    skeleton_seen = False
    global pond_plant_seen
    pond_plant_seen = False
    global moss_seen
    moss_seen = False
    global mushroom_seen
    mushroom_seen = False
# these variables check the status of some interactions of the player with the scenario
    global release_boat
    release_boat = False
    global river_crossed
    river_crossed = False
    print("""
Welcome to the Mystery Island™ text adventure game!
Move across the exotic scenarios and interact with them by typing your actions: always a VERB followed by a NOUN.
Examples: 'Go North', 'Go South' or 'Climb Mountain'.
Good luck with your exploration! And be careful...

...

You are resting after a day of fishing at the sea when suddenly a bright flash comes from the island not far from the coast.
It looks like something exploded near the old lighthouse.""")
    house()

def house():
    print("You are in front of your small wooden house.")
    while True:
        choice = input('> ')

        if 'go north' in choice.lower():
            beach()
        elif 'go east' in choice.lower():
            print("The path goes east and then turns north until you get to the beach.")
            beach_east()
        elif 'go west' in choice.lower():
            print("The path goes west and then turns north until you get to the beach.")
            beach_west()
        elif 'go south' in choice.lower():
            print("It's your wooden house. You have no time for a nap now...")
        elif 'climb house' in choice.lower():
            print("No time for fooling around.")
        else:
            print("Try something else.")

def beach():
    print("You are at the beach.")
    print("The moon is full and bright.")
    print("The sea seems tranquil.")
    while True:
        choice = input('> ')

        if 'go north' in choice.lower():
            print("You need a boat to get to island!")
        elif 'go east' in choice.lower():
            beach_east()
        elif 'go west' in choice.lower():
            beach_west()
        elif 'go south' in choice.lower():
            house()
        else:
            print("Try something else.")

def beach_west():
    global release_boat
    print("This is the west side of the beach, where the pier was built years ago.")
    print("You see your old boat tied to the pier.")
    print("The sea seems tranquil.")

    while True:
        choice = input('> ')

        if 'use boat' in choice.lower() and release_boat == False:
            print("The boat is tied with a rope.")
        elif 'go north' in choice.lower() and release_boat == False:
            print("You could do that using the boat.")
        elif 'go west' in choice.lower():
            print("A rocky elevation prevents you from going beyond.")
        elif 'go south' in choice.lower():
            house()
        elif 'go east' in choice.lower():
            beach()
        elif 'untie boat' in choice.lower() and release_boat == False:
            release_boat = True
            print("You release the boat!")
        elif 'untie rope' in choice.lower() and release_boat == False:
            release_boat = True
            print("You release the boat!")
        elif 'untie boat' in choice.lower() and release_boat == True:
            print("The boat is already released!")
        elif 'untie rope' in choice.lower() and release_boat == True:
            print("The boat is already released!")
        elif 'use boat' in choice.lower() and release_boat == True:
            print("You are ready to go!")
            print("You cross the calm waters of the bay without problems.")
            island_beach()
        else:
            print("Try something else.")

def beach_east():
    print("This is the east side of the beach, where the sand strip ends in a rocky elevation.")
    while True:
        choice = input('> ')
        if 'go west' in choice.lower():
            beach()
        elif 'go north' in choice.lower():
            print("You need a boat to get to the island!")
        elif 'go south' in choice.lower():
            house()
        elif 'go east' in choice.lower():
            print("A rocky elevation prevents you from going beyond.")
        else:
            print("Try something else.")

def island_beach():
    global flash
    global bamboo
    global vine
    global board
    print("You arrive at the island's beach.")
    print("The sand is white and reflects the light of the moon.")
    print("You see the old lighthouse at the distance, on the top of a rocky hill.")
    print("A dense forest separates the beach from the lighthouse.")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            print("There is a huge rock that prevents you from entering the island at this point of the beach.")
        elif 'search boat' in choice.lower():
            flash = True
            print("You find your old flashlight inside the boat.")
            print("It never fails you.")
        elif 'go west' in choice.lower():
            island_beach_west()
        elif 'go east' in choice.lower():
            island_beach_east()
        elif 'search sand' in choice.lower():
            print("You find nothing but sand, shells and aquatic plants.")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else")

def island_beach_west():
    global flash
    global bamboo
    global vine
    global board
    print("This is the west side of the island's beach.")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower() and flash == True:
            print("With the flashlight in hand you are able to find your way into the forest.")
            skeleton()
        elif 'go north' in choice.lower() and flash == False:
            print("It's too dark in the forest. You need a light source.")
        elif 'go south' in choice.lower():
            print("It's the sea!")
        elif 'go west' in choice.lower():
            print("You've reached the end of the beach")
        elif 'go east' in choice.lower():
            island_beach()
        elif 'search sand' in choice.lower():
            print("You find nothing but sand and shells.")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else")

def island_beach_east():
    global flash
    global bamboo
    global vine
    global board
    global rope1
    print("This is the east side of the island's beach.")
    print("You see the remains of a shipwreck very close to the beach.")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower() and flash == True:
            print("With the flashlight in hand you are able to find your way into the forest.")
            monkey()
        elif 'go north' in choice.lower() and flash == False:
            print("It's too dark in the forest. You need a light source.")
        elif 'search sand' in choice.lower():
            print("You find nothing but sand and shells.")
        elif 'go south' in choice.lower():
            print("It's the sea!")
        elif 'go east' in choice.lower():
            print("You've reached the end of the beach")
        elif 'go west' in choice.lower():
            island_beach()
        elif 'search ship' in choice.lower() and rope1 == False:
            print("There's not too much to see here. Just the remains of an old boat of medium size; the name written in the wood seems to be of Nordic origin.")
            print("You find a piece of rope in the middle of the wrecks. It's now in your inventory.")
            rope1 = True
        elif 'search ship' in choice.lower() and rope1 == True:
            print("There's not too much to see here. Just the remains of an old boat; the name written in the wood seems to be of Nordic origin.")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else")

def skeleton():
    global knife
    global bamboo
    global vine
    global board
    global skeleton_seen
    print("After walking a while you reach a clearing in the forest.")
    print("You hear night birds singing an eerie melody.")

    while True:
        choice = input('> ')

        if 'go north' in choice.lower():
            water_fall()
        elif 'go south' in choice.lower():
            island_beach_west()
        elif 'go west' in choice.lower():
            print("There's no path at this side of forest.")
        elif 'go east' in choice.lower():
            totem()
        elif 'search clearing' in choice.lower():
            print("Nothing but leaves on the ground...")
        elif 'search leaves' in choice.lower():
            print("Wow! You find the skeleton of a dead explorer! RIP.")
            skeleton_seen = True
        elif 'search skeleton' in choice.lower() and skeleton_seen == True and knife == False:
            print("You find a big knife with the skeleton! You now have a sharp blade in your inventory.")
            knife = True
        elif 'search skeleton' in choice.lower() and skeleton_seen == True and knife == True:
            print("There's nothing else useful here. Just the bones of a dead explorer.")
        elif 'search skeleton' in choice.lower() and skeleton_seen == False:
            print("Which skeleton?")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def totem():
    global bamboo
    global vine
    global board
    global moss
    global moss_seen
    print("You arrive at a large clearing in the forest.")
    print("In the middle of it there's a huge eagle-shaped wooden totem.")
    print("It must be around 3 meters tall.")
    print("It seems to have been built many years ago.")
    print("You're probably on sacred ground.")
    while True:
        choice = input('> ')

        if 'search totem' in choice.lower():
            print("It's an eagle-shaped wooden totem")
            print("3 meters tall.")
            print("It's body is full of green moss.")
            moss_seen = True
        elif 'pick moss' in choice.lower() and knife == True and moss_seen == True:
            print("You are able to collect some of the moss with the help of the knife. It's now in your inventory.")
            moss = True
        elif 'take moss' in choice.lower() and knife == True and moss_seen == True:
            print("You are able to collect some of the moss with the help of the knife. It's now in your inventory.")
            moss = True
        elif 'collect moss' in choice.lower() and knife == True and moss_seen == True:
            print("You are able to collect some of the moss with the help of the knife. It's now in your inventory.")
            moss = True
        elif 'get moss' in choice.lower() and knife == True and moss_seen == True:
            print("You are able to collect some of the moss with the help of the knife. It's now in your inventory.")
            moss = True
        elif 'pick moss' in choice.lower() and knife == False and moss_seen == True:
            print("You need some instrument to help you with that.")
        elif 'take moss' in choice.lower() and knife == False and moss_seen == True:
            print("You need some instrument to help you with that.")
        elif 'collect moss' in choice.lower() and knife == False and moss_seen == True:
            print("You need some instrument to help you with that.")
        elif 'get moss' in choice.lower() and knife == False and moss_seen == True:
            print("You need some instrument to help you with that.")
        elif 'go west' in choice.lower():
            skeleton()
        elif 'go north' in choice.lower():
            bamboo_scene()
        elif 'go east' in choice.lower():
            monkey()
        elif 'go south' in choice.lower():
            print("The path is blocked by a huge rock.")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def monkey():
    global knife
    global bamboo
    global vine
    global board
    global hook
    print("A large tree emerges from the ground at this point of the forest. It's really beautiful and tall.")
    print("You hear a strange sound coming from the top.")
    nest_seen = False
    climb = False
    while True:
        choice = input('> ')

        if 'climb tree' in choice.lower() and climb == False:
            climb = True
            nest_seen = True
            print("The tree has many branches, it's easy to climb it.")
            print("After some climbing you see a strange creature!")
            print("It's a monkey-bird hybrid. It has the head of a monkey, but the body of a tropical bird!")
            print("He seems scared, and flies away from his nest after noticing your presence.")
        elif 'climb tree' in choice.lower() and climb == True:
            print("You're already on the top of the tree!")
        elif 'search nest' in choice.lower() and nest_seen == True:
            hook = True
            print("You find a large metal hook while searching the monkey-bird's nest.")
            print("It's now in your inventory!")
        elif 'search nest' in choice.lower() and nest_seen == False:
            print("Which nest?")
        elif 'climb down' in choice.lower():
            climb = False
            print("You're back to the ground level.")
        elif 'go down' in choice.lower():
            climb = False
            print("You're back to the ground level.")
        elif 'go north' in choice.lower() and climb == True:
            print("First you must go back to the ground!")
        elif 'go south' in choice.lower() and climb == True:
            print("First you must go back to the ground!")
        elif 'go west' in choice.lower() and climb == True:
            print("First you must go back to the ground!")
        elif 'go east' in choice.lower() and climb == True:
            print("First you must go back to the ground!")
        elif 'go north' in choice.lower() and climb == False:
            vine_scene()
        elif 'go south' in choice.lower() and climb == False:
            island_beach_east()
        elif 'go west' in choice.lower() and climb == False:
            totem()
        elif 'go east' in choice.lower() and climb == False:
            print("There's no path at this side of the forest.")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        elif 'go back' in choice.lower():
            island_beach
        else:
            print("Try something else.")

def water_fall():
    global knife
    global bamboo
    global vine
    global board
    global rope
    global pond_plant_seen
    global aquatic_plant
    print("The forest suddenly opens in a large clearing where a small waterfall fills a beautiful pond.")
    while True:
        choice = input('> ')
        if 'search pond' in choice.lower():
            print("The pond's surface is covered by beautiful floating aquatic plants.")
            pond_plant_seen = True
        elif 'search waterfall' in choice.lower():
            print("The water is cold...")
        elif 'enter water' in choice.lower():
            print("It's too cold... You don't want to swim right now.")
        elif 'pick plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'collect plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'get plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'take plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'pick aquatic plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'collect aquatic plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'get aquatic plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'take aquatic plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == False:
            aquatic_plant = True
            print("You get some of the aquatic plants.")
        elif 'pick plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == True:
            print("You have enough.")
        elif 'collect plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == True:
            print("You have enough.")
        elif 'get plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == True:
            print("You have enough.")
        elif 'take plant' in choice.lower() and pond_plant_seen == True and aquatic_plant == True:
            print("You have enough.")
        elif 'go north' in choice.lower():
            upper_w_corner()
        elif 'go west' in choice.lower():
            print("There's no path at this side of the forest.")
        elif 'go east' in choice.lower():
            bamboo_scene()
        elif 'go south' in choice.lower():
            skeleton()
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def bamboo_scene():
    global knife
    global bamboo
    global vine
    global board
    print("You reach a clearing in the forest.")
    print("You can hear a strange noise among the bamboo trees. Maybe an animal?")
    while True:
        choice = input('> ')

        if 'cut bamboo' in choice and bamboo == False and knife == True:
            bamboo = True
            print("You cut some pieces of the bamboo trees and keep them with you.")
        elif 'cut bamboo' in choice.lower() and bamboo == True:
            print("You have enough.")
        elif 'search bamboo' in choice.lower():
            print("The creature flees when you get closer to the trees.")
        elif 'cut bamboo' in choice and knife == False:
            print("You lack a sharp blade to do that!")
        elif 'go north' in choice.lower():
            print("A large boulder blocks your way north.")
        elif 'go west' in choice.lower():
            water_fall()
        elif 'go east' in choice.lower():
            vine_scene()
        elif 'go south' in choice.lower():
            print("There's no path at this side of the forest")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def vine_scene():
    global knife
    global bamboo
    global vine
    global board
    print("This part of the forest is full of strong vines falling from the trees, but you are able to move through.")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            upper_e_corner()
        elif 'go south' in choice.lower():
            monkey()
        elif 'go east' in choice.lower():
            print("There's no path at this side of the forest.")
        elif 'go west' in choice.lower():
            bamboo_scene()
        elif 'cut vines' in choice.lower() and vine == False and knife == True:
            vine = True
            print("You cut some of the vines and keep them with you.")
            print("Maybe they are useful somewhere.")
        elif 'cut vines' in choice.lower() and vine == True:
            print("You have enough.")
        elif 'cut vines' in choice.lower() and vine == False and knife == False:
            print("How woud you do that?")
        elif 'inspect vines' in choice.lower():
            print("They seem pretty strong!")
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def upper_w_corner():
    global knife
    global bamboo
    global vine
    global board
    print("You hear the sound of a river flowing nearby. The forest is really dense here!")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            print("The path is blocked by a huge rock.")
        elif 'go west' in choice.lower():
            print("There's no path at this side of the forest.")
        elif 'go south' in choice.lower():
            water_fall()
        elif 'go east' in choice.lower() and knife == False:
            print("It seems there was a trail on this direction, but it's now covered by dense vegetation.")
        elif 'go east' in choice.lower() and knife == True:
            print("The trail is covered by dense vegetation, but you are able to use the knife to clear the way!")
            river_south()
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You are able to use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def upper_e_corner():
    global knife
    global bamboo
    global vine
    global board
    print("You hear the sound of a river flowing nearby. The forest is really dense here!")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            print("The path is blocked by a huge rock.")
        elif 'go east' in choice.lower():
            print("There's no path at this side of the forest.")
        elif 'go west' in choice.lower() and knife == False:
            print("It seems there was a trail on this direction, but it's now covered by dense vegetation.")
        elif 'go west' in choice.lower() and knife == True:
            print("The trail is covered by dense vegetation, but you are able to use the knife to clear the way!")
            river_south()
        elif 'go south' in choice.lower():
            vine_scene()
        elif 'build board' in choice.lower() and bamboo == True and vine == True:
            board = True
            print("You use the bamboo and the vines to create a strong wooden board!")
        elif 'build board' in choice.lower() and bamboo == True and vine == False:
            print("You need something to keep the bamboos together.")
        elif 'build board' in choice.lower() and bamboo == False and vine == True:
            print("How would you do that? Something is missing.")
        else:
            print("Try something else.")

def river_south():
    global bamboo
    global vine
    global board
    global river_crossed

    if river_crossed == False:
        print("The trail leads you to the south bank of a river of dark waters.")
        print("There seems to be no way around it.")
        while True:
            choice = input('> ')

            if 'go north' in choice.lower() and board == True:
                print("You use the wooden board to cross the river safely!")
                river_crossed = True
                river_north()
            elif 'cross river' in choice.lower() and board == True:
                print("You use the wooden board to cross the river safely!")
                river_crossed = True
                river_north()
            elif 'cross river' in choice.lower() and board == False:
                print("Right before entering the river you notice the carcass of a dead monkey floating not far from the river bank.")
                print("It's being eaten by hungry piranhas!")
                print("There must be a way to cross the river safely.")
            elif 'go north' in choice.lower() and board == False:
                print("Right before entering the river you notice the carcass of a dead monkey floating not far from the river bank.")
                print("It's being eaten by hungry piranhas!")
                print("There must be a way to cross the river safely.")
            elif 'go east' in choice.lower():
                upper_e_corner()
            elif 'go west' in choice.lower():
                upper_w_corner()
            elif 'go south' in choice.lower():
                print("A large boulder blocks your way south.")
            elif 'build board' in choice.lower() and bamboo == True and vine == True:
                board = True
                print("You use the bamboo and the vines to create a strong wooden board!")
            elif 'build board' in choice.lower() and bamboo == True and vine == False:
                print("You need something to keep the bamboos together.")
            elif 'build board' in choice.lower() and bamboo == False and vine == True:
                print("How would you do that? Something is missing.")
            else:
                print("Try something else.")
    else:
        print("You are on the south bank of the river.")
        while True:
            choice = input("> ")

            if 'go north' in choice.lower():
                print("You cross the river with your wooden board.")
                river_north()
            elif 'cross river' in choice.lower():
                print("You cross the river with your wooden board.")
                river_north()
            elif 'go east' in choice.lower():
                upper_e_corner()
            elif 'go west' in choice.lower():
                upper_w_corner()
            elif 'go south' in choice.lower():
                print("A large boulder blocks your way south.")
            else:
                print("Try something else.")

def river_north():
    print("You are now on the north bank of the river.")
    while True:
        choice = input("> ")

        if 'go north' in choice.lower():
            wall_base()
        elif 'cross river' in choice.lower():
            print("You cross the river with your wooden board.")
            river_south()
        elif 'go east' in choice.lower():
            print("There's no path at this side of the island.")
        elif 'go west' in choice.lower():
            print("There's no path at this side of the island.")
        elif 'go south' in choice.lower():
            print("You cross the river with your wooden board.")
            river_south()
        else:
            print("Try something else.")

def wall_base():
    global rope1
    global rope2
    global hook
    print("You get to the base of a huge limestone wall.")
    print("Maybe you could climb it with the proper equipment.")
    while True:
        choice = input('> ')

        if 'go north' in choice.lower() and rope1 == False and rope2 == False and hook == False:
            print("The wall is too steep and you have nothing to climb it with.")
        elif 'go north' in choice.lower() and rope1 == True and rope2 == False and hook == False:
            print("You don't have enough rope, and you also need some object to put the rope on the top of the wall!")
        elif 'go north' in choice.lower() and rope1 == True and rope2 == False and hook == True:
            print("You have the hook and a piece of rope, but you need a little more rope to complete the climb!")
        elif 'go north' in choice.lower() and rope1 == False and rope2 == False and hook == True:
            print("You have the hook, but you need a rope to complete the climb!")
        elif 'go north' in choice.lower() and rope1 == False and rope2 == True and hook == True:
            print("You have the hook and a piece of rope, but you need a little more rope to complete the climb!")
        elif 'go north' in choice.lower() and rope1 == False and rope2 == True and hook == False:
            print("You don't have enough rope, and you also need some object to put the rope on the top of the wall!")
        elif 'go north' in choice.lower() and rope1 == True and rope2 == True and hook == False:
            print("You have enough rope, but you need some object to put the rope on the top of the wall!")
        elif 'go north' in choice.lower() and rope1 == True and rope2 == True and hook == True:
            print("Great! You throw the metal hook to the top of the wall and it gets stucked there.")
            print("Using your rope you are able to climb it easily.")
            wall_top()
        elif 'climb wall' in choice.lower() and rope1 == False and rope2 == False and hook == False:
            print("The wall is too steep and you have nothing to climb it with.")
        elif 'climb wall' in choice.lower() and rope1 == True and rope2 == False and hook == False:
            print("You don't have enough rope, and you also need some object to put the rope on the top of the wall!")
        elif 'climb wall' in choice.lower() and rope1 == True and rope2 == False and hook == True:
            print("You have the hook and a piece of rope, but you need a little more rope to complete the climb!")
        elif 'climb wall' in choice.lower() and rope1 == False and rope2 == False and hook == True:
            print("You have the hook, but you need a rope to complete the climb!")
        elif 'climb wall' in choice.lower() and rope1 == False and rope2 == True and hook == True:
            print("You have the hook and a piece of rope, but you need a little more rope to complete the climb!")
        elif 'climb wall' in choice.lower() and rope1 == False and rope2 == True and hook == False:
            print("You don't have enough rope, and you also need some object to put the rope on the top of the wall!")
        elif 'climb wall' in choice.lower() and rope1 == True and rope2 == True and hook == False:
            print("You have enough rope, but you need some object to put the rope on the top of the wall!")
        elif 'climb wall' in choice.lower() and rope1 == True and rope2 == True and hook == True:
            print("Great! You throw the metal hook to the top of the wall and it gets stucked there.")
            print("Using your rope you are able to climb it easily.")
            wall_top()
        elif 'search wall' in choice.lower():
            print("It's a steep limestone wall.")
            print("You find a note stuck in on of the rocks.")
        elif 'read note' in choice.lower():
            print("'Personal reminder: ask the Crown for more money the next time they send you on a crazy exploration on a far exotic dangerous island!'")
        elif 'go south' in choice.lower():
            river_north()
        elif 'go east' in choice.lower():
            camp()
        elif 'go west' in choice.lower():
            graveyard()
        else:
            print("Try something else")

def wall_top():
    print("You are now on the top of the limestone wall.")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            shaman()
        elif 'go south' in choice.lower():
            print("You climb down the wall.")
            wall_base()
        elif 'go east' in choice.lower():
            print("The way east is too dangerous! You could fall and get hurt badly.")
        elif 'go west' in choice.lower():
            print("The way west is too dangerous! You could fall and get hurt badly.")
        else:
            print("Try something else.")

def camp():
    global rope2
    print("Someone camped here a long time ago.")
    print("There are remains of a tent and of what looks like a fire pit.")
    while True:
        choice = input('> ')
        if 'search tent' in choice.lower():
            rope2 = True
            print("You find a piece of rope! It's now in your inventory.")
        elif 'search fire' in choice.lower():
            print("You find nothing interesting here.")
        elif 'go north' in choice.lower():
            print("There's no path at this side of the island.")
        elif 'go east' in choice.lower():
            print("You can't go further east. There's no path at this side of the island.")
        elif 'go south' in choice.lower():
            print("You can't get to the river from this point, the forest is too dense!")
        elif 'go west' in choice.lower():
            wall_base()
        else:
            print("Try something else.")

def graveyard():
    global mushroom
    print("You arrive at a area of the forest where the ground is filled with colored stones, animal feathers and shells.")
    print("It's an ancient burial ground.")
    while True:
        choice = input('> ')
        if 'search stone' in choice.lower():
            print("You see stones of all kind of shapes, sizes and colors.")
            print("Some of them are home to a purple fungus.")
            mushroom_seen = True
        elif 'pick fungus' in choice.lower() and mushroom_seen == True:
            print("You pick some of the fungus.")
            mushroom = True
        elif 'get fungus' in choice.lower() and mushroom_seen == True:
            print("You pick some of the fungus.")
            mushroom = True
        elif 'collect fungus' in choice.lower() and mushroom_seen == True:
            print("You pick some of the fungus.")
            mushroom = True
        elif 'take fungus' in choice.lower() and mushroom_seen == True:
            print("You pick some of the fungus.")
            mushroom = True
        elif 'search tomb' in choice.lower():
            print("You see stones of all kind of shapes, sizes and colors.")
            print("Some of them are home to a purple fungus.")
            mushroom_seen = True
        elif 'go north' in choice.lower():
            print("You can't go further north. There's a huge rocky formation in your way.")
        elif 'go west' in choice.lower():
            print("You can't go further west. The forest is too dense.")
        elif 'go south' in choice.lower():
            print("You can't go further south. The forest is too dense.")
        elif 'go east' in choice.lower():
            wall_base()
        else:
            print("Try something else.")

# the shaman scenario
def shaman():
    global moss
    global aquatic_plant
    global mushroom
    print("After walking for a while over a rocky terrain, you get to some kind of ceremonial site.")
    print("There are over six large rocks forming a circle.")
    print("In the middle of this structure you see an old man without clothes, his body covered in painting.")
    print("He holds an object that looks like a mix of walking stick and spear.")
    print("There are beautiful bird feathers on his head, and a large necklace made of bones hangs from his neck.")
    print("He stands besides a boiling cauldron cooking over a fire pit.")
    print("The Shaman asks with a powerful voice: \"Who are you stranger?\"")
    name = input('> ')
    print(f"\"{name}... What a strange name... \nWell, I am Shumaya, the holy Shaman of Goky Island.")

    if moss == True and aquatic_plant == True and mushroom == True:
        print("Oh... I see you have all the ingredients I've looking for my latest creation.")
        print("The great Alyzhoma, Orghraxxa and Marxyla... Thank you!")
        print("Now we may talk...")
        print(f"I must inform you {name} that I am allowed by the spirits of the island to let you pass only if you answer correctly to the following question:")
        print("""    From me the entire universe emerged countless aeons ago.
    I could dissolve the whole of men wickedness with a smile.
    Yet I am present in the pure sight of a child.
    Who am I???""")
        print("You only have three chances to get it right...\"")
        chances = 3
        while True:
            enigma_answer = input('> ')
            if 'love' in enigma_answer.lower():
                print("\nWise! The spirits allow you to continue on your path. Good luck in your journey...\"")
                print("")
                print("You leave the Shaman behind and after walking through a rocky ascending path you finally arrive at the old lighthouse!")
                light_house_south()
            elif chances > 2:
                chances -= 1
                print(f"\"That's wrong! You still have {chances} chances!\"")
            elif chances > 1:
                chances -= 1
                print(f"\"That's wrong! You have one last chance!\"")
            else:
                print("\"That's wrong... Your chances are over. I must take your soul to the spirits!\"")
                die()
    elif moss == False and aquatic_plant == False and mushroom == False:
        print("I don't have time to speak to you now... I'm working on a new potion, but I'm lacking important ingredients.")
        print("Come back if you find these:")
        print("- The great Alyzhoma which grows with Elypshzanma, Queen of Airs.")
        print("- Orghraxxa, companion of those who are gone.")
        print("- Marxyla, or water-bed.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == True and aquatic_plant == False and mushroom == False:
        print("Oh, I see you have the great Alyzhoma with you!")
        print("That's great, but I still need:")
        print("- Orghraxxa, companion of those who are gone.")
        print("- Marxyla, or water-bed.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == True and aquatic_plant == True and mushroom == False:
        print("Oh, I see you have the great Alyzhoma and Marxyla with you!")
        print("That's great, but I still need:")
        print("- Orghraxxa, companion of those who are gone.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == True and aquatic_plant == False and mushroom == True:
        print("Oh, I see you have the great Alyzhoma and Orghraxxa with you!")
        print("That's great, but I still need:")
        print("- Marxyla, or water-bed.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == False and aquatic_plant == True and mushroom == False:
        print("Oh, I see you have Marxyla with you!")
        print("That's great, but I still need:")
        print("- The great Alyzhoma which grows with Elypshzanma, Queen of Airs.")
        print("- Orghraxxa, companion of those who are gone.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == False and aquatic_plant == True and mushroom == True:
        print("Oh, I see you have Marxyla and Orghraxxa with you!")
        print("That's great, but I still need:")
        print("- The great Alyzhoma which grows with Elypshzanma, Queen of Airs.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    elif moss == False and aquatic_plant == False and mushroom == True:
        print("Oh, I see you have Orghraxxa with you!")
        print("That's great, but I still need:")
        print("- The great Alyzhoma which grows with Elypshzanma, Queen of Airs.")
        print("- Marxyla, or water-bed.")
        print("Now please go away... It's hard to concentrate with such noise.\"")
        wall_top()
    else:
        print("How did you get here?")
        exit()

def light_house_south():
    print("This is the south side of the lighthouse – an old, tall building pointing to the black sky.")
    print("Oddly, its light is off.")
    print("From where you are, you can see no entrance.")
    while True:
        choice = input('> ')

        if 'go east' in choice.lower():
            light_house_east()
        elif 'go west' in choice.lower():
            light_house_west()
        elif 'go north' in choice.lower():
            light_house_north()
        elif 'go south' in choice.lower():
            print("You don't want to meet the Shaman again...")
        elif 'search lighthouse' in choice.lower():
            print("It's the old lighthouse. Its light is off. Strange...")
        else:
            print("Try something else.")

def light_house_west():
    global key
    print("From the west side of the lighthouse you have a beautiful view of the island at night.")
    print("The moon shines over the calm waters of a dark sea.")
    print("But you can see no entrance to the lighthouse here.")
    print("If you had more time you could easily sit here on the grass to contemplate the landscape.")
    while True:
        choice = input('> ')

        if 'go north' in choice.lower():
            light_house_north()
        elif 'go south' in choice.lower():
            light_house_south()
        elif 'go west' in choice.lower():
            print("You can't go further west.")
        elif 'go east' in choice.lower():
            light_house_east()
        elif 'search lighthouse' in choice.lower():
            print("It's the old lighthouse. Its light is off. Strange...")
        elif 'search grass' in choice.lower():
            print("You find a small metal key on the grass.")
            print("Someone must have dropped it here while watching the sunset.")
            key = True
        else:
            print("Try something else.")

def light_house_east():
    print("At the east side of the lighthouse you see a big metal object, the size of a car, but with an oval shape, partially buried under the floor!")
    print("There's still smoke from the impact.")
    print("It looks like some kind of alien egg-ship crashed here!")
    while True:
        choice = input('> ')
        if 'go north' in choice.lower():
            light_house_north()
        elif 'go east' in choice.lower():
            print("You can't go further east.")
        elif 'go west' in choice.lower():
            light_house_west()
        elif 'go south' in choice.lower():
            light_house_south()
        elif 'search ship' in choice.lower():
            print("There's a strange vibe coming from the ship. Better to keep a distance.")
        elif 'search lighthouse' in choice.lower():
            print("It's the old lighthouse. Its light is off. Strange...")
        else:
            print("Try something else.")

def light_house_north():
    global key
    print("This is the north face of the lighthouse.")
    print("You can see a metal door into the lighthouse.")
    while True:
        choice = input('> ')

        if 'open door' in choice.lower() and key == False:
            print("The door is locked.")
        elif 'open door' in choice.lower() and key == True:
            print("You open the door with the metal key and enter in the old lighthouse.")
            light_house_floor()
        elif 'enter lighthouse' in choice.lower():
            print("How would you do that?")
        elif 'go north' in choice.lower():
            print("You can't go further north.")
        elif 'go east' in choice.lower():
            light_house_east()
        elif 'go west' in choice.lower():
            light_house_west()
        elif 'go south' in choice.lower():
            light_house_south()
        elif 'search lighthouse' in choice.lower():
            print("It's the old lighthouse. Its light is off. Strange...")
            print("You can see a door here.")
        else:
            print("Try something else.")

def light_house_floor():
    global gun
    print("It's dark here...")
    while True:
        choice = input('> ')
        if 'use flashlight' in choice.lower():
            print("Now you can see!")
            print("There's been a fight here!")
            print("You see a broken table, chairs on the floor.")
            print("There's also blood... near a ruined wardrobe.")
            print("The blood trail continues to a rusty spiral staircase that seems to lead to the top floor.")
            print("An old phone lies on the floor.")
            while True:
                choice = input('> ')

                if 'search wardrobe' in choice.lower():
                    print("Just a pile of old men's clothes.")
                elif 'open wardrobe' in choice.lower():
                    print("Just a pile of old men's clothes.")
                elif 'search clothes' in choice.lower() and gun == False:
                    print("You find a shotgun!")
                    print("It's now in your inventory.")
                    print("Someone must have been hurt while trying to reach the gun...")
                    gun = True
                elif 'search clothes' in choice.lower() and gun == True:
                    print("There's nothing else here.")
                elif 'use phone' in choice.lower():
                    print("It's broken.")
                elif 'search table' in choice.lower():
                    print("A ruined table.")
                elif 'search chair' in choice.lower():
                    print("A ruined chair.")
                elif 'search blood' in choice.lower():
                    print("There's a lot of blood here.")
                    print("It leads to the top floor.")
                elif 'use stair' in choice.lower():
                    print("You follow the blood trail...")
                    light_house_top()
                else:
                    print("Try something else!")
        elif 'go back' in choice.lower():
            light_house_north()
        else:
            print("It's too dark! You need some light source here.")

def light_house_top():
    global gun
    print("There's another metal door at the staircase's end.")
    print("You hear the sounds of some kind of mechanical instrument coming from the other side.")
    print("The blood trail continues beyond the door...")
    while True:
        choice = input('> ')
        if 'open door' in choice.lower():
            final_room()
        elif 'go back' in choice.lower():
            light_house_floor()
        elif 'go down' in choice.lower():
            light_house_floor()
        else:
            print("Try something else")

def final_room():
    global gun
    print("You finally get to the top of the lighthouse!")
    print("The room is covered in darkness – someone broke the light!")
    print("Some kind of lab was installed here, with strange mechanical instruments all over the floor.")
    print("Also on the floor, the corpse of a dead headless man!")
    print("A strange tall, skinny creature, apparently naked, sits near the body, using some of the equipment to join the head of a monkey to the dead man's neck!")
    print("The creepy alien notices you, and moves to attack!")
    chances = 3
    while True:
        if chances >= 1:
            choice = input('> ')
            if 'use shotgun' in choice.lower() and gun == True:
                print("You point and shoot right in the head of the alien!")
                print("It falls lifeless.")
                print("You killed it!")
                win()
            elif 'use gun' in choice.lower() and gun == True:
                print("You point and shoot right in the head of the alien!")
                print("It falls lifeless.")
                print("You killed it!")
                win()
            elif 'attack alien' in choice.lower():
                print("How would you do that?")
                chances -= 1
                print("The alien is getting closer!")
            elif 'use knife' in choice.lower():
                print("The knife won't help you here! You need something bigger.")
                chances -= 1
                print("The alien is getting closer!")
            elif 'kill alien' in choice.lower() and gun == True:
                print("How would you do that?")
                chances -= 1
                print("The alien is getting closer!")
            else:
                chances -= 1
                print("The alien is getting closer!")
        else:
            print("You didn't act fast enough.")
            print("The alien rips your head off with his weird saw.")
            die()

start()
