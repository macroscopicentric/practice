import random
import sys

#input_format takes the input (a string) and turns it into a list.
def input_format():
    input = raw_input(">").lower().split(" ")
    if "." in input[-1]:
        detail = input.pop().split(".").pop(0)
        input.append(detail)
    #Can I get it to respond to general input? Some simple, like a print response, and some
    #more complicated that might need functions (ie, inventory).
    return input

#Asks if the user wants to restart after winning or dying.
def restart():
    print """
            Restart? Y/N"""
    restart = input_format()

    if "y" in restart or "yes" in restart:
        a_game.play()
    elif "n" in restart or "no" in restart:
        sys.exit()
    else:
        print "DOES. NOT. COMPUTE."
        self.restart()

#Superclass (vocab?) of scenes. Prints error if scene isn't properly defined.
class Scene(object):

    def enter(self):
        print "Error: scene not defined."
        sys.exit(1)

class Engine(object):

    #Copied this from his example. Still don't understand inits.
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

#Death scene == failed adventure and restart game.
class Death(Scene):

    def enter(self):
        print """
            Congratulations! You're so clever that you killed yourself. Next
            time, try to be a little less clever and you might get a little
            less dead."""
        restart()

#Finished is just so the Engine/Map aren't confused when the game returns
#'finished'. (Just restarts the game using the function above.)
class Finished(Scene):
    def enter(self):
        restart()

#Beginning is for people unfamiliar with text adventures and how they work.
class Beginning(Scene):
    def enter(self):
        print """
            This is a very simple text adventure, based off of Zed A. Shaw's Learn Python
            the Hard Way. Here's how it works: the game will describe a scenario/room to you,
            then it will ask for your input. You can type in anything your heart desires,
            although the game won't always understand it. Type in whatever you want, then press
            ENTER. You don't have to type complete sentences, or even use capital letters.

            Ready? Y/N
        """
        tutorial = input_format()
        if "y" in tutorial or "yes" in tutorial:
            return 'central_corridor'
        elif "n" in tutorial or "no" in tutorial:
            return self.enter()
        else:
            print "DOES. NOT. COMPUTE."
            return self.enter()

#room1
class CentralCorridor(Scene):

    def joke_time(self):
        joke = input_format()
        tickled = random.randrange(0, 2)
        # tickled = 1
        if "tell" in joke and "joke" in joke:
            if tickled == 0:
                print """
            The Gothon stands there blankly. I guess he didn't enjoy your joke
            very much. He decides that anyone as unfunny as you doesn't deserve
            to live. He draws his Super Duper LaZer Gun (TM) and shoots you dead.
                """
                return 'death'
            else:
                print """
            The Gothon laughs heartily. It sounds rather like an ape smashing slugs
            with a rock. It's fairly unpleasant, and you're relieved when he stops.
            Because he liked your joke so much, the Gothon decides to step aside
            and allows you to pass unharmed.
                """
                return 'laser_weapon_armory'
        elif "shoot" in joke or "gun" in joke:
            print """
            You don't have a gun! You're completely unarmed, so I guess you'll have
            to find a non-violent solution. Try again.
            """
            return self.joke_time()
        elif "run" in joke:
            print """
            Where are you going to run to? You're in a dead-end! Try again.
            """
            return self.joke_time()
        elif "punch" in joke or "attack" in joke or "kill" in joke:
            print """
            Yeah, Gothons are nine feet tall. Good luck with that.
            (Spoiler: It doesn't go well. You die.)
            """
            return 'death'
        else:
            print """
            DOES. NOT. COMPUTE."""
            try = 0
            try += 1
            if try >= 3:
                print 'Hint: Try typing "tell a joke" and then pressing enter.'
            return self.joke_time()

    def enter(self):
        print """
            You're standing in the central corridor of a giant Gothon
            spaceship. There's a Gothon standing in front of you. He's waiting
            for a battle of wits. Try telling him a joke.
            """
        return self.joke_time()

#room2
class LaserWeaponArmory(Scene):

    def num_test(self, riddle):
        number = input_format()
        
        if "0001" in number or "001" in number or "01" in number or "1" in number:
            print """
            Impressive!
            
            The plasma shimmers and disappears, so you reach through and grab the
            neutron bomb, then leave the room the same way you came in."""
            return 'the_bridge'
        elif "2403" in number:
            print "No, smartypants. It's a trick question."
            print riddle
            return self.num_test(riddle)
            #Can I adjust this code so it doesn't print out the riddle every time?
        else:
            print """
            That wasn't the correct answer. Did I mention that plasma is highly
            volatile? The keypad beeps angrily at you, and you promptly explode
            in a shiny beam of light."""
            return 'death'
            
    def enter(self):
        riddle = """
            As I was going to St Ives
            I met a man with seven wives
            Every wife had seven sacks
            Every sack had seven cats
            Every cat had seven kits
            Kits, cats, sacks, wives
            How many were going to St Ives?"""
            
        print '''
            You enter the next room and see that it's filled with laser weapons
            covering all the walls and even the ceiling. On the opposite wall
            from where you came in, there's a plasma cage with a neutron bomb
            inside. You realize that the neutron bomb is just the thing to blow
            up this whole spaceship full of invading Gothons. The only problem
            is, the plasma cage has a keypad to unlock it, and you don't know
            the code.
            
            But as you step closer, you see that someone has taped a small piece
            of paper (how antiquated!) above the keypad. It says:
        
            %s
            
            What would you like to type into the keypad?''' % (riddle)
        return self.num_test(riddle)

#room3
class TheBridge(Scene):

    def bridge_action(self):
        action = input_format()

        if "gently" in action or "carefully" in action or "roll" in action and "bomb" in action:
            print """
            You can't throw a neutron bomb gently, sorry. It doesn't work. You TRY to throw the
            bomb in a gentle underhand, and it bounces a few feet then comes to a stop
            halfway between you and the Gothon. When it goes off, you both die."""
            return 'death'
        elif "throw" in action or "toss" in action and "bomb" in action:
            print """
            You throw the bomb and then duck. The bomb sails over the Gothon's head
            and explodes behind him. His death is messy and you look down to find
            that you're now wearing some Gothon bits. Don't think about it too hard.
            The good news is that you've now successfully crippled the ship. No
            Gothon invasions from THIS ship!"""
            return 'escape_pod'
        elif "run" in action:
            print """
            You try to flee, but the only way to go is back into the laser weapon
            armory. As soon as you've gone three steps, the Gothon shoots you in the
            back. You fall, and drop the neutron bomb. It rolls into the armory and
            explodes. You're dead AND you failed to stop the Gothons from invading."""
            return 'death'
        elif "tell" in action and "joke" in action:
            print """
            This Gothon seems to be less enthusiastic about jokes. He rolls his eyes,
            pulls out his Super Duper LaZer Gun (TM) and shoots you. You drop the bomb
            as you collapse, and the whole ship explodes around you."""
            return 'death'
        elif "high" in action and "five" in action:
            print """
            Unfortunately, Gothons only have three fingers and a thumb. The Gothon doesn't
            seem to know what a high five is, and stares at you blankly when you hold your
            hand up. Try something else."""
            return self.bridge_action()
            #Can either do above or have a Boolean like left_bridge = 0, and have a while loop.
        else:
            print "DOES. NOT. COMPUTE."
            try = 0
            try += 1
            if try >= 3:
                print 'Hint: Try typing "throw the bomb" and then pressing enter.'
            return self.bridge_action()

    def enter(self):
        print """
            You enter the bridge and find another Gothon in front of you, barring
            your way. Like the first Gothon, he's wearing a Super Duper LaZer Gun (TM),
            but you've surprised him, so he hasn't drawn it yet. He sees that you're
            carrying a neutron bomb, however, and he raises his hands in the air.
        
            What will you do?"""
        return self.bridge_action()

#room4
class EscapePod(Scene):

    def enter(self):
        print """
            You finally reach the escape pods after leaving death and destruction
            in your wake. But there are three escape pods to choose from! Which
            do you choose? (Pick a number.)"""
        pod = input_format()
        rand_pod = random.randrange(0,3)
        #rand_pod = 0
        return_value = '0'

        def success():
            print """
            You step into the only non-broken shuttle and launch into space. You
            turn to look back, and the spaceship explodes gracefully behind you.
            Congratulations! You saved earth.
            
            FIN.
                """
            return 'finished'

        def failure():
            print """
            You picked the wrong shuttle! When the door finally swooshes open, you
            realize that the inside of the shuttle is full of broken parts and an
            inch of dust covering everything. Tragically, you've now run out of time
            and the whole ship explodes around you. You die.
            """
            return 'death'

        if "1" in pod or "first" in pod or "one" in pod or "left" in pod:
            if rand_pod == 0:
                return_value = success()
            else:
                return_value = failure()
        elif "2" in pod or "second" in pod or "two" in pod or "middle" in pod:
            if rand_pod == 1:
                return_value = success()
            else:
                return_value = failure()
        elif "3" in pod or "third" in pod or "three" in pod or "right" in pod:
            if rand_pod == 2:
                return_value = success()
            else:
                return_value = failure()
        else:
            print "DOES. NOT. COMPUTE."
            return self.enter()

        return return_value 

class Map(object):

    #Copied all text below from his example. I don't understand a lot of it.
    #Creating a dictionary for which variable maps to which room. Had to use a string,
    #otherwise it gave an error that the variable was undefined.
    #Why __init__ AND opening_scene?
    #"This is also why the map comes after the scenes because the dictionary has to
    #refer to them so they have to exist."
    #Keep in mind that the instance of the map is different than the class Map, so technically you don't need to worry about the above quote.
    
    scenes = {
        'beginning' : Beginning(),
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }

    #Above is creating instances of each object with new names. Don't need that much inheritance.
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        #Called when an instance of the object is created. Creates and then initializes
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

#pdb (below) is a debugger.
#import pdb
#pdb.set_trace()
a_map = Map('beginning')
a_game = Engine(a_map)
a_game.play()


#Current bugs:
#SOLVED: Exit doesn't exit the entire program, just the thread (Restart and Scene object).
#SOLVED: Moving to next scenes (Death and TheBridge) in LaserWeaponArmory doesn't work.
#SOLVED: Typing "1" in the LaserWeaponArmory and then trying gibberish just repeats the "1"
#elif statement actions. Maybe it's because I'm calling a function within itself?
#SOLVED: WHY DOES SYS.EXIT() WORK WHEN I STUCK IT IN ELIF "1" BUT NOT IN RESTART.
#Solution: because it wasn't registering my input correctly.
#SOLVED: LaserWeaponArmory Death scene is successful, but TheBridge isn't.
#SOLVED: Picking numbers in EscapePod isn't working correctly. Unsure where exactly the error is,
#but I think it's like my issue in LaserWeaponArmory. There were many issues, including spaces
#vs. tabs, the return value not carrying through, having extra lines between my conditionals,
#and formatting both conditionals (in pod and rand_pod ==) incorrectly.
#SOLVED: Typing in 2403 and THEN the solution throws an error. Ditto with TheBridge. Had to
#return the function in the else statement.

#Better text adventure:
#Remember where you were? So don't have to repeat.
#Respond to general commands (type them in at any level and get the same response)? This would
#allow an inventory, and things like "hello!"
#Expand number of rooms.
#Can you have a function that increments a different variable from different parent functions?

#Pip
#Control D exits any python thing, PDB = n (next) and s (step), c to continue.