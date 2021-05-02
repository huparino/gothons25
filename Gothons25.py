import random

class Scene(object):

    # call the appropriate enter function per scene
    def enter(self):
        pass


class Engine(object):

    #? specify the room via scene_map
    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    # handle the start and end of the game
    def play(self):
        while a_map.start_scene is not None:
            if a_map.start_scene == 'first_central_corridor':
                a_map.opening_scene()
            else:
                a_map.next_scene(a_map.start_scene)

        print("GAME OVER")

        pass


class Death(Scene):

    def enter(self, origin):

        if origin == 'first':
            print("The Gothon, not amused, uses its backside tentacles to rip your arms out of your sockets and slap you with your own hands. You fall to your knees, thick red blood pools under you, and consciousness fades.")

        if origin == 'laser':
            print("Panic washes over you as you open the door. There is a gaping hole where an escape pod used to be, and you are immediately sucked out into the freezing void. What will kill you first, the lack of oxygen or the low Kelvin temps?\n")

        if origin == 'bridge':
            print("The Gothons feast on your flesh tonight. Humanity is doomed!")

        # extra conditional for result of guessing which pod
        if origin == 'escape':
            print("Exhausted, you strap yourself into the harness and await the automatic launch sequence while peering out the hull window, thinking about the pale blue dot. As the pod ejects you glance at the control panel to see the destination coordinates are already locked in for the forbidden planet Gauranth Prime!! A certain, quick death is all you can hope for... Ooh, so close. Thanks for playing!")

        print("YOU DIED.")

        # clean up with a string method?
        if input("Would you like to play again?") in ['yes' , 'y' , 'Yes' , 'YES']:
            a_map.start_scene = 'first_central_corridor'
            a_map.bomb = False
            a_map.boss = False
        else:
            a_map.start_scene = None

        pass


class FirstCentralCorridor(Scene):

    def enter(self):
        a_game.scene_map = 'first'
        print("""
        Just as you are about to lurch forward a slimy Gothon appears out of nowhere and blocks your path.
        The beast lurches toward you and then suddenly stops and turns its head inquisitively.
        You remember your study of Goth culture and figure you'll try a joke to break the ice.
        """)

        joke = input("Tell the Gothon a joke.\n>")
        if len(joke.split()) >= 5:
            result = True
        else:
            result = False

        if result is True:
            print("""
            The Gothon rears it's ugly neck back and let's out a gurgly shriek of laughter, and then, suddenly, vanishes....
            Your instinct tells you that you haven't seen the last of that beast.
            Well, time to get to work, saving the world.
            """)
            a_map.start_scene = input("Which door do you chose?\n laser : Laser Weaponry Armory\n bridge: The Bridge\n escape: Escape Pod Control\n>")

        else:
            a_map.start_scene = 'death'

        pass


class CentralCorridor(Scene):

    # print some description and instrucitons--> if then return results for next scene
    def enter(self):
        a_map.start_scene = input("You are back in the central hallway. Which door do you chose?\n laser : Laser Weaponry Armory\n bridge: The Bridge\n escape: Escape Pod Control\n>")
        # try:
        #     a_map.start_scene in ['laser' , 'bridge' , 'escape', 'central']
        # except ValueError:
        #     return None
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        a_game.scene_map = 'laser'

        if a_map.bomb is False:

            print("""
            You enter the Laser Weapon Armory.
            There is an airtight titanium case with a number pad with the numbers 0-4 etched onto the keys.
            You must guess the correct passcode to unlock the neutron bomb.
            If you guess incorrectly 3 times, the code will re-randomize.
            """)

            nums = []
            while len(nums) < 3:
                nums.append(str(random.randint(0, 4)))
            passcode = ''
            passcode = passcode.join(nums)
            # print(passcode)

            attempts = 0
            win = False
            while attempts < 3 and win is False:
                guess = input("ENTER PASSCODE: _ _ _\n>")
                if guess == passcode:
                    win = True
                else:
                    print("EHH. ACCESS DENIED. Please try again.\nHINT: _ " + nums[1] + " _\n")
                    attempts += 1

                if 1 < attempts < 3:
                    print("EHH. ACCESS DENIED. Please try again.\nHINT: " + nums[0] + nums[1] + " _\n")


            if win is True:
                print("PSHHH. The airtight container releases its lock and you take the bomb. It is strangely cold to the touch...and pulsating.")
                a_map.bomb = True

            elif win is False:
                print("TOO MANY FAILED ATTEMPTS. Please try again later.\n")
                a_map.start_scene = 'central'

            if a_map.start_scene == 'escape':
                a_map.start_scene = 'death'

        a_map.start_scene = input("There is a door to your right with no markings. Could it be a shorcut to the Escape Pod Control room?\nWhich door do you chose?\n central : Central Corridor\n escape : ?\n>")


class TheBridge(Scene):

    def enter(self):
        a_game.scene_map = 'bridge'

        if a_map.boss is True:
            print("You enter the bridge, where you overcame the Gothons. The Neutron bomb is blinking and beeping, a reminder that you need to get to the Escape Pod Control room!")
            a_map.start_scene = input("There is only one way out, through the Central Corridor. Which door do you chose?\n central : Central Corridor\n>")

        elif a_map.boss is False:

            if a_map.bomb is False:
                print("You don't have the Neutron bomb yet so there is nothing to do here. Come back when you have the bomb.")
                a_map.start_scene = 'central'

            elif a_map.bomb is True:

                print("""
                You enter the Bridge. The stench of rotting flesh and spoiled milk almost makes you vomit.
                At the center of the room, the central processing unit is still intact. If you can place the bomb there, it will vaporize the entire ship.
                Just as you are about to become a hero, two beastly figures emerge from the shadows, drooling and gurgling heavily.
                It's the Gothon from the hallway, and another, much larger Gothon!
                "NOT FUNNY", shrieks the smaller beast as it swings at you with meaty, sharp claws, but you drop the bomb and duck just in time.
                The larger Gothon has circled you and is now in between you and the blast door opening. You're trapped!
                """)

                win = False

                choice = input("""
                No time to waste; What will you do?

                1) Try to quickly place the neutron bomb
                2) Tell another joke to smol boy

                >""")

                if choice == '1':

                    place = input("""
                Using your Science skills, you are able to place and arm the bomb, but not without losing a limb.
                The small Gothon is feasting on your arm, while the larger one roars and lunges at you.

                What will you do?

                1) Bop smol boy on the head with your flashlight
                2) Tell the greatest and best joke in the world

                >""")

                    if place == '1':
                        print("Come on, you gotta do better than that. The Gothons maul you and eat the bomb.")
                        win = False

                    elif place == '2':
                        tribute = input("""
                You have told the greatest and best joke in the world (tribute)!
                Small Gothon recoils in horror, then suddenly bursts into flames.
                Success! One down.

                Now what?

                1) Try to reason with big boy.
                2) Muster your greatest Science aptitude....

                >""")

                        if tribute == '1':
                            print("Nope. The Large Gothon is just too Goth. It subsumes your place in timespace and walks out the other side.")
                            win = False
                        elif tribute == '2':
                            print("SCIENCE! Your knowledge of the Gothons is deep. There is no Gothon. The larger Gothon cannot hold its illusion any longer and de-materializes before you. Whew, that was close! You set the bomb to detonate 1 minute after the next escape pod departs. You look down at your arm that you thought you lost. Let's get out of here! Get to Escape Pod Control.")
                            win = True

                elif choice == '2':

                    joke = input("""
                The smaller Gothon, looks up, confused by your precarious wit, and starts to flicker and distort in place.
                Yeah, like an old analog CRT televsion. Which is...very strange.
                Before you can rationalize what you just saw, the largest Gothon you've ever seen is on you.
                Flailing, you grab the Neutron bomb to sheild yourself from the Gothon.
                It thrashes and claws at the bomb, carving divets into its outer shell.

                This is not good. What are you going to do?

                1) Remember your research paper on hypo-gauranth projection.
                2) Remember your martial arts training.

                >""")

                    if joke == '1':
                        projection = input("""
                The Gothon continues to shriek and thrash.
                It has now completely destroyed the bomb and sliced a 4-inch wide gash in your abdomen.
                You are in shock as you feel warm liquid gushing out of you.

                You are about to lose consciousness. What is next?

                1) Place the bomb carefully.
                2) Destroy the emergency panel to your left with what is left of the bomb.

                >""")

                        if projection == '1':
                            print("""
                A calm washes over you. The Gothon stops its thrashing and looks at you with mounting anxiety.
                You have transcended the hypo-gauranthian projection. Smol boi has dissapeared.
                You get to your feet slowly, feel your way through Big boi, crawl over to the CPU and start the detonation program.
                Your physical wounds will still need time to heal, but your mind is sound. The Gothon's projection can't fool you any longer.
                Time to get the hell of this damned ship! Get to Escape Pod Control!""")
                            win = True

                        elif projection == '2':
                            print("You run over to the emergency panel and thrust the bomb with all your might. It falls far short a foot in front of you. You collapse, clinging to your innards so they don't fall out. The Gothons take each of your remaining limbs, one per hand and the last thing you see is shiny Gothon teeth.")
                            win = False

                    elif joke == '2':
                        print("You headbut Gothon and squirm out of its grasp into your martial arts stance. Suddenly, smol boi stops flickering and impales you from behind with its scaly tale. You fall to your nees and see Big boi chuckling as your life fades.")
                        win = False


                if win is True:
                    a_map.start_scene = input("There is only one way out, through the Central Corridor. Which door do you chose?\n central : Central Corridor\n>")
                    a_map.boss = True

                elif win is False:
                    a_map.start_scene = 'death'

        if a_map.start_scene in ['laser' , 'escape']:
            print("A distant, faulty airlock door quickly opens, you are thrust back into the central hallway, and the door closes. That was weird....")
            a_map.start_scene = 'central'


class EscapePod(Scene):

    def enter(self):
        a_game.scene_map = 'escape'
        print("""
        You enter the Escape Pod Control Room. There are 3 airlock doors.
        That familiar hum fills your heart with warmth.\n""")

        if a_map.boss is False:
            print("You can't escape yet, there are bombs to place and Gothons to kill!")
            a_map.start_scene = input("There is only one way out, through the Central Corridor. Which door do you chose?\n central : Central Corridor\n>")

        elif a_map.boss is True:

            choice = input("OK let's blow this spaceship! One of the pods will take you to victory. Which door will you choose?\n>")

            if choice == '1':
                win = False
                a_game.scene_map = 'laser'

            if choice == '2':
                win = False

            if choice == '3':
                win = True

            if win is False:
                a_map.start_scene = 'death'

            elif win is True:
                a_map.start_scene = None
                print("""
        You escape with your supreme wits and amazing Science skills!
        About a minute later you see a silent but brilliant, elliptical orb of light in the space behind you.
        You have beaten the Gothons with your research intact!
        That familiar pale blue dot is getting bigger in the distance and you remember a poem by Bukowski:


            Roll the Dice

            if you’re going to try, go all the
            way.
            otherwise, don’t even start.

            if you’re going to try, go all the
            way. this could mean losing girlfriends,
            wives, relatives, jobs and
            maybe your mind.

            go all the way.
            it could mean not eating for 3 or
            4 days.
            it could mean freezing on a
            park bench.
            it could mean jail,
            it could mean derision,
            mockery,
            isolation.
            isolation is the gift,
            all the others are a test of your
            endurance, of
            how much you really want to
            do it.
            and you’ll do it
            despite rejection and the
            worst odds
            and it will be better than
            anything else
            you can imagine.

            if you’re going to try,
            go all the way.
            there is no other feeling like
            that.
            you will be alone with the
            gods
            and the nights will flame with
            fire.

            do it, do it, do it.
            do it.

            all the way
            all the way.
            you will ride life straight to
            perfect laughter,
            it’s the only good fight
            there is.


        Thanks for playing Gothons From Planet Percal #25.

        Adventure game by Alan Angell, inspired by Zed Shaw
        """)

        if a_map.start_scene in ['laser' , 'bridge']:
            print("You need to get your bearings back, so you return to the central hallway.")
            a_map.start_scene = 'central'


class Map(object):

    # specify the starting room (from previous choice/action)
    def __init__(self, start_scene, bomb, boss):
        self.start_scene = start_scene
        self.bomb = bomb
        self.boss = boss
        pass

    # based on actions from each room, move to the next room
    # use dict to map room to start_scene
    def next_scene(self, start_scene):
        rooms = {'central' : CentralCorridor() , 'laser' : LaserWeaponArmory() , 'escape' : EscapePod() , 'bridge' :  TheBridge() , 'first_central_corridor' : FirstCentralCorridor() , 'death' : Death()}
        next_room = rooms[start_scene]
        if start_scene == 'death':
            next_room.enter(a_game.scene_map)
        else:
            next_room.enter()


    def opening_scene(self):
        print("""
        "Gothons From Planet Percal #25"

        You are a scientist on a research mission to the Gauran system aboard the The U.S.S. Expedition.
        On your way back to home base in the Sun star system, the ship was attacked by Gothons, a species of insect-like barbarians from planet Percal #25.
        The Gothons claimed that your crew stole a sacred artifact from their holy temple at Halegauranthia.
        However, your mission was relegated to observations from orbit, and everyone on-board had no knowledge of such artifact.
        The Gothons have killed everyone on board and have threatened to follow your ship's flight plan home and continue their search in your home system.
        You, the sole survivor, armed only with your wit and research information, must subvert the Gothon's plans and escape with your life.
        """)

        # Then drop the player into the frist room (given by first instance of Map)
        input("Press Enter to begin the game.")
        print("""
        You awaken back to consciousness...
        There is a long hallway in front of you. To your left is a door with a sign partially covered in blood: 'L-ser Wea--- --mory'
        Further down the hall and to the right, the blast doors to the Bridge are destroyed and flickering light emanates from the room.
        You hear a faint gurgling in the shadows.
        At the end of the hall is the ship's Escape Pod control room.
        """)

        while input("Say anything to continue: ") is '':
            print("If you can't follow directions you won't win this game! Try typing anything again.")

        a_map.next_scene(self.start_scene)


# why not define a function for this? -- said "a_map" not defined?
a_map = Map('first_central_corridor', False, False)
a_game = Engine(a_map)
a_game.play()
