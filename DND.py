xp = 0
dead = False

answer = input("What class do you want to be?  (F = Human Fighter, W = Human Wizzard, D = Dwarf Rogue)")

if answer == "F":
    Class = "F"
    name = "Ander"
    health = 10
    intel = 6
    strength = 8
    speed = 30
    
    print("You chose Fighter who is fighting with a longsword and shortbow")
    print("Your name is " + name)
    print("Health = " +str(health))
    print("Intelligence = " + str(intel))
    print("Strength = " + str(strength))
elif answer == "W":
    Class = "W"
    name = "Jandar"
    health = 6
    intel = 10
    strength = 4
    speed = 20
    print("You chose Wizzard who is fighting with a Quarterstaff and Darts")
    print("Your name is " + name)
    print("Health = " +str(health))
    print("Intelligence = " + str(intel))
    print("Strength = " + str(strength))
elif answer == "D":
    Class = "R"
    name = "Darrak"
    health = 10
    intel = 4
    strength = 10
    speed = 15
    print("You chose Dwarf who is fighting with a Battleaxe and Crossbow")
    print("Your name is " + name)
    print("Health = " +str(health))
    print("Intelligence = " + str(intel))
    print("Strength = " + str(strength))
else:
    print("Could not recognize your response")
    print("The default is Fighter")
    Class = "F"
    name = "Ander"
    health = 10
    intel = 6
    strength = 8
    speed = 30
    
    print("You chose Fighter who is fighting with a longsword and shortbow")
    print("Your name is " + name)
    print("Health = " +str(health))
    print("Intelligence = " + str(intel))
    print("Strength = " + str(strength))

print("")
print("THE STORY BEGINS")
print("***********************")
print("")
story = """You are teleported to the entrance of a large tower.  You are told by a mysterious voice that you will face the gauntlet.A path of challenges that will either make you more experienced or kill you.  If you make it to the end, you win."""
print(story)
      
answer = input("There are three paths.  (U = Up the Stairs, D = Down the Stairs, S = Straight down the hallway)")

if answer == "U":
    print("You went up the stairs")
    print("*********************")
    print("You encounter a Rat.  It seems that it has not seen you.")
    ratHealth = 1
    answer = input("Do you wish to A = Attack, or R = Run?")
    if answer == "A":
        while ratHealth > 0:
            attack = input("R = Ranged Attack, M = Melee Attack")
            if attack == "R":
                if Class == "W":
                    roll = input("Roll a D-4 and enter it here")
                elif Class == "F":
                    roll = input("Roll a D-6 and enter it here")
                elif Class == "R":
                    roll = input("Roll a D-8 and enter it here")
            elif attack == "M":
                if Class == "W":
                    roll = input("Roll a D-6 and enter it here")
                elif Class == "F" or Class == "R":
                    roll = input("Roll a D-8 and enter it here")
            ratHealth = ratHealth - int(roll)
        print("Excellent! You killed a rat and gained +25xp")
        xp += 25
    elif answer == "R":
        print("Run Away!")
    else:
        print("You ran")
    print("**************************************")
    print("Continuing up the stairs")
    print("Out of no where you are attacked by a Ghoul.  It attacks first with its claws")
    roll = input("Roll a D-4 and enter it here")
    health = health - int(roll)
    print("Your health is now " + str(health))
    answer = input("What do you do?  A = Melee Attack, R = Run Away, S = Spell (wizzards only)")
    GhoulHealth = 22
    if answer == "R":
        print("You can't run away, it is too fast.  You must attack")
        answer = "A"
    elif answer == "S" and Class != "W":
        print("You try a spell but you are not a wizzard.  You are forced to attack.")
        answer = "A"
    elif answer == "S" and Class == "W":
        spell = input("Which spell to cast? C = Cure Wounds, R = Ray of Frost, P = Poison Spray, M = Minor Illusion")
        if spell == "C":
            roll = input("Roll a D-8 and enter it here")
            health = health + int(roll)
            print("Your health increased to " + str(health))
            print("Now you must attack")
            answer = "A"
        elif spell == "R":
            roll = input("Roll a D-8 and enter it here")
            GhoulHealth = GhoulHealth - int(roll)
            print("The Ghoul took some damage but you must continue your attack")
            answer = "A"
        elif spell == "P":
            print("Spell has no affect, you must attack")
            answer = "A"
        elif spell == "M":
            print("The illusion creates a large booming sound. The ghoul is scared away.  You continue on your journey.")
    else:
        print("Incorrect response.  You are forced to attack")
        answer = "A"
    if answer == "A":
        while GhoulHealth > 0:
            if Class == "W":
                roll = input("Roll a D-6 and enter it here")
            elif Class == "F" or Class == "R":
                roll = input("Roll a D-8 and enter it here")
            GhoulHealth = GhoulHealth - int(roll)
            if GhoulHealth <= 0:
                print("You killed the Ghoul! You gained 200XP!")
                xp += 200
            else:
                print("The Ghoul is down to " + str(GhoulHealth) + " Health")
                print("The Ghoul attacks with its claws")
                roll = input("Roll a D-4 and enter it here")
                health = health - int(roll)
                if health <= 0:
                    print("You died, try again")
                    dead = True
                    break
                else:
                    print("Your health is now " + str(health))
                
        
    print("****************************")
    print("You continue to the roof of the tower.  You notice an imprint in the floor.  It is giant webbed footprint.")
    answer = input("Do you wish to track down the monster or run? A = Attack, R = Run")
    if answer == "A" or answer != "R":
        FrogHealth = 18
        print("The footprint was produced by a GIANT FROG!  You get the first attack.")
        if strength >= 10:
            print("You see a large hammer and pick it up.")
            roll = input("Roll a D-20 and enter the result")
            if roll == "20" or roll =="19" or roll == "18":
                print("You instantly kill the frog with a deadly hammer hit!  Gain 100 XP!")
                xp += 100
            elif int(roll) < 5:
                print("You missed the frog completely with the hammer.")
            else:
                FrogHealth -= int(roll)
                print("You hit the frog with the hammer doing good damage but the hammer disintegrates.")
                print("The frog has "+ str(FrogHealth) + " health.  You will need to attack again.")
        while FrogHealth>0:
            answer = input("R = Ranged, M = Melee, S = Spell (wizzards only)")
            
            if answer == "S" and Class != "W":
                print("You try a spell but you are not a wizzard.  Your only option is to Melee")
                answer = "M"
            if answer == "S" and Class == "W":
                spell = input("Which spell to cast? C = Cure Wounds, R = Ray of Frost, P = Poison Spray, M = Minor Illusion")
                if spell == "C":
                    roll = input("Roll a D-8 and enter it here")
                    health = health + int(roll)
                    print("Your health increased to " + str(health))
                    print("Now you must attack")
                    answer = "M"
                elif spell == "R":
                    roll = input("Roll a D-8 and enter it here")
                    FrogHealth = FrogHealth - int(roll) - 2
                    print("The Frog took some damage but you must continue your attack")
                    answer = "M"
                elif spell == "P":
                    FrogHealth -= 10
                    print("The Frog took some damage but you must continue your attack")
                    answer = "M"
                elif spell == "M":
                    print("The illusion creates a large booming sound. The Frog is not Scared. You must continue your attack")
                    answer = "M"
                    
            if answer == "R":
                if Class == "W":
                    roll = input("Roll a D-4 and enter it here")
                elif Class == "F":
                    roll = input("Roll a D-6 and enter it here")
                elif Class == "R":
                    roll = input("Roll a D-8 and enter it here")
                answer = "M"
                FrogHealth = FrogHealth - int(roll)
            if answer == "M":
                print("The Frog is slow to react.  You are able to get off a Melee attack before it pounces.")
                if Class == "W":
                    roll = input("Roll a D-6 and enter it here")
                elif Class == "F" or Class == "R":
                    roll = input("Roll a D-8 and enter it here")
                FrogHealth = FrogHealth - int(roll)
            if FrogHealth > 0:
                print("The frog extends its wet tongue.  It wraps around you.  As it pulls you in, you wonder if it can swallow you whole.")
                if Class == "R":
                    print("The frog swallows you whole.  Unfortunately no one is available to get you out.  You are stuck in the gauntlet forever.")
                    dead = True
                else:
                    print("The frog can only bite you")
                    roll = input("Roll a D-4 and enter it here")
                    health -= int(roll)
                if health <=0:
                    dead = True
            else:
                print("You managed to kill the frog!  You gain 100XP!")
                xp += 100
                    
    elif answer == "R":
        print("You hear a loud 'Ribbit' followed by a huge mass leaping through the air.  The monster is 50 feet away.")
        distance = 50
        for step in range(3):
            roll = input("Roll a D-4 to create a speed burst.  Enter result here")
            if roll == "1":
                print("You stumble and fall while the frog jumps towards you")
                distance = distance -20
            elif roll == "4":
                print("You sprint beyond your abilities while the frog jumps towards you")
                distance = distance + speed + 5 -20
            else:
                print("You sprint while the frog jumps towards you.")
                distance = distance + speed -20
        
            if distance <=0:
                print("You were eaten by the frog and never made it out of the Gauntlet.  Try again")
                dead = True
                break
            else:
                print("Your distance from the frog is " + str(distance))
    print("***************************")
    
    if dead == False:
        input("Hit Enter to Continue")
        print("A large beam of light illuminates the room.  You are temporarily blinded.  You lose track of space and time.")
        input("Hit Enter to Continue")
        print("You find yourself safe at home.  You realize that you are alive and that you have made it through the gauntlet.")
        print("The experience has made you a stronger character.")
        print("You have gained " + str(xp) +" XP.")
        if xp > 300:
            print("You have leveled up! +2 proficiency to spend on any of your attributes")
    
elif answer == "D":
    print("You went down the stairs")
elif answer == "S":
    print("You went straight")
else:
    print("incorrect input")