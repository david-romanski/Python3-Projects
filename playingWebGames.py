# David Romanski
# Started 04/22/2020
# Playing Web Games
# Comments: This program includes the walkthrough to a text adventure/interactive fiction game.
# It runs though the game, hopefully to completion.
# This automaton is 'blind' in that it doesn't look at any responses from the website

import time
import selenium
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('http://www.web-adventures.org/cgi-bin/webfrotz?s=Jigsaw')

def loadWalkthrough():
	walkthrough = [	
# ------------------------------------------------------------------------
#                        JIGSAW by Graham Nelson
#                        Solution and Walkthrough
#                         Gareth Rees, July 1995
# ------------------------------------------------------------------------


# PROLOGUE: CENTURY PARK
# ----------------------

# The prologue to "Jigsaw", like the prologue to "Adventure", is a matter
# of collecting equipment and finding your way into the rest of the game.
# But it's not just an object-finding exercise, it's a matter of
# collecting the major themes of the game: is it the end of the twentieth
# century, and the game will explore the whole of twentieth-century
# history; there are fifteen minutes to go before midnight, and each
# remaining minute corresponds to one of the fifteen remaining episodes in
# the game; and you get to see the traces left by Grad Kaldecki and the
# stranger in black (who you will be trailing after for the rest of the
# game).  But enough fore-shadowing, on with the game.  First is a light
# source...

	'east',
   	'get sparkler',
   	'south',

# ... and a clue to a hidden location behind the tent.

   	'west',
   	'get jigsaw piece',
    'southeast',
	'get rucksack',
	'examine crate',
	'get key,device',
	'examine rucksack',
	'examine key',
	'examine device',

# The description of the rucksack is an allusion to "Curses", hinting that
# the protagonist of "Jigsaw" is the same as the Meldrew heir in Graham's
# earlier game (though nothing else is made of this hint).  The
# significance of marking "A.4" will become apparent later.  It is not a
# coincidence that the reading "99" on the curious device is the same as
# the last two digits of the current year.  The inscription "tempora
# mutantur, nos et mutamur in illis" means "times change, and we change
# with the times".

    'northwest',
	'northeast',
	'east',
	'examine statue',

# Grad Kaldecki's motto "felix qui potuit rerum cognoscere causas" means
# "happy is he who is able to know the cause of things.  Ironic, because
# one of the morals of "Jigsaw" is that causes are very uncertain things
# indeed.

	'east',
	'open stool',
	'get sketch book',
	'look under stool',
	'get pencil',
	'west',
	'west',
	'sketch nightjar',

# The significance of the sketchbook won't become apparent until the very
# end of the game.  But for now, all you need to know is that sketching
# animals is a useful thing to do.

	'southwest',
	'west',
	'up',
	'light fuse',
	'down',
	'enter pyramid',
	'south',
	'examine case',
	'open case',

# Leave the case for later.  You appear to be trapped inside the pyramid,
# so let's hope you've done everything from the prologue.

	'east',
	'look under table',
	'get jigsaw piece',
	'examine it',
	'examine table',
	'clean table',
	'examine board',

# Now some of the mysteries are reasonably clear: the game is going to
# involve a jigsaw-piece-collecting exercise, with the end of the game on
# completion of the jigsaw.  The marking "A.4" on the crate suggests that
# the corner piece goes at location a4 (you may have to "turn corner
# piece" a few times to get it the right way round), and the pencilled
# "Southwest?" on the centre piece suggests it goes southwest of the centre,
# namely at c2 (again, you may have to try it in several orientations
# before it fits).  Luckily, the board itself tells you when a piece fits.

# Note that the status line has changed; the mysterious numbers are your
# score, the number of jigsaw pieces successfully entered into the board,
# and the number of turns so far.

	'put corner piece at a4',
	'put centre piece at c2',
	'get clock',
	'turn hand to 59',

# The pyramid and jigsaw turn out to be a baroque time machine, and the
# clock is the device for controlling it.  You are advised to experiment
# for yourself, but in summary: turning the clock's hand lights up the
# board; if the alarm is on and the clock reaches 0, then you are
# transported back to the pyramid from whatever time zone you are in.  So,
# off you go:

	'press a4',
	'press c2',


# CHAPTER 1: RICOCHET
# -------------------

	'examine device',
	'examine street',
	'examine cafe',

################################# TESTING ##################################
	'turn hand to 59',
	'press a4',
	'press c2',
	'examine device',
	'examine street',
	'examine cafe',
################################# TESTING ##################################

# It's June 1914, and you're in Sarajevo.  What could be more ominous?
# And then Black enters.  Black is a strange character, partly villain,
# and partly love-interest.  You'll find as you progress, that you are
# doomed to trail around history in Black's wake, fixing the problems left
# behind.  But you had better be polite to start with.

#    'shake hands',
#    'examine black',
#    'z.z',
#    'say no to black',
#    'unlock dresser with key',
#    'open dresser',
#    'get jigsaw piece from dresser',
#    'sketch horses',
#    'ask black about sarajevo',
#    'ask black about kaldecki',
#    'ask black about archduke',
#    'examine rifle',
#    'turn safety off',
#    'ask black about pyramid',
#    'examine student',
#    'z.z.z.z.z',

# Black's plan is to assassinate the student, thus preventing World War I.
# Might that not be a good thing?  Millions of men died in savage and
# futile battles in the fields of northern France.  But it turns out that
# you have no choice here: you must preserve the course of your own
# history, regardless of how bloody, brutal and senseless it is.  This
# attitude to history is a strange one: on the one hand history is so
# fragile and contingent that the slightest push can topple it into chaos,
# and on the other, there is only one true version of history that must be
# preserved at all costs.

#    'shoot archduke',
#    'z.z.z.z.z',

# The deed is done, history is safe, and you have a plot and some clues.
# Black intends to improve history; you know however that this cannot
# work.  When a crisis in history has been resolved, a "cloud of disturbed
# air" appears, and with the aid of the curious device it is possible to
# condense this cloud into a time window (the black sphere) and enter a
# mysterious realm called "the Land".  But without the device, you cannot
# go there yet, and must resort to the clock.

#    'turn clock to 1',
#    'wait',
#    'examine disc',
#    'northwest',
#    'get curious device',
#    '[put the edge piece at c1]',
#    'turn clock off',
#    'turn clock to 59',
#    'press c1',


# CHAPTER 2: ICY CALM
# -------------------

#    'get times, note',
#    'read times',
#    'read note',
#    'southwest',
#    'north',

# You turned the clock off because you'll be spending more than an hour in
# this time zone.  The note is addressed to "White", which must be you
# (the good one, as opposed to the villain Black).  Where are you?  It is
# 1912, you are on an ocean liner, the notepaper is "White Star Line", and
# you have just collided with an iceberg.  Could it be that you are on
# board the H.M.S. Titanic?

#    'south',
#    'east',
#    'up',
#    'read notice',
#    'west',
#    'get jacket',
#    'wear jacket',
#    'east',
#    'down',
#    'west',
#    'south',
#    'west',
#    'north',
#    'open box',
#    'get syrup',
#    'west',

# The Titanic appears to be sinking as expected, despite the calm of the
# passengers and crew.  How could the course of history be affected?  If
# you wait near Benjamin Guggenheim (disguised as an officer), you will
# eventually receive a secret letter to deliver.  But of course, you'll be
# leaving the ship by time-travel, not by lifeboats, so you'd better find
# someone to act as courier for you.

#    '[repeatedly wait until Guggenheim gives you the letter]',
#    'examine secret letter',
#    'west',
#    'examine ouija board',
#    'say hello to miss shutes',
#    'give secret letter to miss shutes',
#    'look',
#    'get jigsaw piece',

# The jigsaw piece must be very big to have passed as a ouija board!  The
# clue here is that anything square and coloured white or grey is probably
# a jigsaw piece, so you had better be on the lookout.  Now you need to
# find your way into Black's cabin:

#    'east',
#    'east',
#    'up',
#    'move chairs',
#    "get boy's book",
#    "read boy's book",
#    'again',
#    'get door key',
#    'down',
#    'south',
#    'east',
#    'north',
#    'east',
#    'remove jacket',
#    'east',
#    'say hello to captain smith',
#    'ask captain smith about titanic',
#    'ask captain smith about lifeboats',
#    'unlock door with door key',
#    'open door',
#    'east',
#    'get long barrelled key',
#    'look under wardrobe',
#    'read second note',
#    'examine kaldecki detector',
#    'spin it',

# The Kaldecki detector is a device that detects jigsaw pieces; it rings
# the bell when you haven't found all the jigsaw pieces in the time zone.
# Luckily, the missing piece is close at hand:

#    'open window',
#    'get jigsaw piece',
#    'spin kaldecki detector',

# So there are no more to find here.  What about that towel you saw the
# stewardess take away, the one with all the mathematics on it?

#    'west',
#    'stewardess, give me the towel',
#    'examine towel',

# The towel tells you when and where the time window will open.  Remember
# this information.  Now you must make sure that the secret letter gets to
# safety by ensuring that the S.S. Carpathia is around to pick up the
# lifeboats.  Recall from reading the "Boy's Book of the Sea" that the
# distress prosign is CQD (actually, by the voyage of the Titanic, the
# International Maritime Convention had agreed on the new prosign SOS -
# but the radio operator on the Titanic sent both).

#    'west',
#    'up',
#    'unlock door with long key',
#    'open door',
#    'wear jacket',
#    'east',
#    'examine charts',
#    'dah.dit.dah.dit',
#    'dah.dah.dit.dah',
#    'dah.dit.dit',

# You have now saved history from disaster.  If you want to visit the Land
# now, then go to the place written on the towel, wait for the right time
# (just before the ship sinks) and activate the curious device.  However,
# there'll be plenty of time to visit the Land later in the game, so you
# can escape using the clock instead:

#    'turn clock on',
#    'turn clock to 1',
#    'wait',
#    'northwest',
#    '[put the edge piece at b1]',
#    '[put the corner piece at a1]',
#    'turn clock off',
#    'turn clock to 59',
#    'press a1',


# CHAPTER 3: AND ONE PERCENT LUCK
# -------------------------------

# Actually, there's no particular reason to choose A1 rather than B1;
# Jigsaw has few dependencies between its time zones, so you have a lot of
# freedom about which order to visit them in.  This solution chooses one
# ordering; there's no reason why you shouldn't choose a different one.
# It's a good idea to spin the Kaldecki detector at the start of a time
# zone to see if you need to search for jigsaw pieces, and to spin it
# after you pick up each jigsaw piece to see if there are any more.

#    'examine device',
#    'spin kaldecki detector',
#    'open upper door',
#    'open lower door',
#    'down',
#    'sketch mice',
#    'north',
#    'examine bell jar',
#    'look under bell jar',
#    'read typed note',

# It's 1928, and Alexander Fleming is about to discover penicillin.  With
# your help, that is.

#    'south',
#    'east',
#    'up',
#    'get certificate',
#    'get jigsaw piece',
#    'spin kaldecki detector',
#    'search dishes',
#    'get mouldy dish',

# Fleming should have come in by now and deposited his suitcase (if not,
# wait a bit).  He doesn't appear to be a very observant man, as he's
# missed both you, and the mouldy petri dish.  How to bring it to his
# attention?  He would notice something as large as a suitcase in the
# wrong place:

#    'examine suitcase',
#    'push suitcase east',
#    'put dish on suitcase',
#    '[wait until Fleming finds the mouldy dish]',
#    '[wait until the disturbed air appears]',
#    'press white button',
#    'enter black ball',
#    'z.z',

# And now you're in the Land.  The Land is a four-by-four grid of
# locations, each one corresponding to a square on the jigsaw board.  The
# locations covered in thick mist correspond to the jigsaw pieces that you
# haven't placed in the board yet.  There's nothing much to do here at the
# moment, though it's mostly harmless to explore (but if you go southeast,
# then east three times, you'll regret it).

#    'southeast',
#    'southeast',
#    'northwest',
#    '[put centre piece at c3]',
#    'turn clock to 59',
#    'press b1',


# CHAPTER 4: TEMPS PERDU
# ----------------------

#    'examine device',
#    'spin kaldecki detector',
#    'south',
#    'get coin',
#    'north',
#    'north',
#    'get figaro',
#    'read le figaro',
#    'north',

# It's 1922; Proust is soon to die in Paris, and the manuscript of "A la
# Recherche de Temps Perdu", one of the greatest novels of the twentieth
# century, is almost finished.  (If Proust was searching for his lost
# time, what are you and Black searching for?)

# Now you are lost in a maze, but fear not! it isn't difficult.  Wait for
# a while, and you'll see various authentic Parisian characters go past.
# Which way are they all going?

#    '[follow the Parisiens until you find the absinthe]',
#    'get absinthe',
#    'drink absinthe',
#    'dance',
#    'south',
#    'south',
#    'get coin',
#    'north',
#    'open door',
#    'east',
#    'enter lift',
#    'give coin to boy'
#    'boy, u.u.u.u',
#    'boy, u.u.u.u',
#    'get centre piece',
#    'spin kaldecki detector',
#    'boy, d.d.d',
#    'get out',
#    'east',
#    'read invitation',
#    'get madeleine',
#    'eat madeleine',
#    'get tea tray',
#    'get edge piece',
#    'spin kaldecki detector',

# A crucial passage of "A la Recherche" has escaped; clearly you must find
# it or else history will be wrecked for lack of it.  (Perhaps not every
# reader of Jigsaw will have quite such a high regard for Proust's novel
# as Mr Nelson clearly has.)

#    'west',
#    'enter lift',
#    'boy, down',
#    'get out',
#    'west',
#    'south'
#    'west',
#    'get paperole',
#    'drink tea',
#    'put madeleine in tea',
#    'eat madeleine',
#    'swing pendulum',
#    'get paperole',
#    'drink tea',
#    'east',
#    'north',
#    'east',
#    'enter lift',
#    'boy, up',
#    'get out',
#    'east',
#    'drop paperole',

# History is safe, yet again.  Note that here is wasn't Black who
# interfered, but you, because you were desperate to collect all the
# jigsaw pieces.

#    'wait',
#    'press white button',
#    'enter black ball',
#    'z.z',
#    'east',
#    'southeast',
#    'northwest',
#    '[put the edge piece at b4]',
#    '[put the centre piece at b2]',
#    'turn clock to 59',
#    'press c3',


# CHAPTER 5: NO COMPROMISE
# ------------------------

#    'examine device',
#    'spin kaldecki detector',
#    'get pravda',
#    'read pravda',

# It is April 1917.  The Russian Revolution is in full swing, Lenin is on
# his way to Moscow, and Black plans to delay or stop him.  Once again,
# the right thing to do is debatable.  Stalin killed or exiled millions of
# his countrymen; might it not have been better if the Revolution had been
# stopped, or diverted?  But you have little choice in the matter.

#    'east',
#    'get british army uniform',
#    'examine trunk',
#    'open trunk',
#    'search trunk',
#    'west',
#    'unlock door with little key',
#    'open door',

# No doubt the tied-up British officer is the work of Black.  You
# shouldn't wear the British army uniform quite yet, because the soldiers
# won't talk to you when you're wearing it.  Now a couple of get-x-give-x
# puzzles follow:

#    'west',
#    'examine man',
#    'search man',
#    'east',
#    'south',
#    'get pashka',
#    'ask soldiers about pashka',
#    'get pashka',
#    'ask soldiers about lenin',
#    'ask soldiers about russia',
#    'ask soldiers about train',
#    'north',
#    'remove sixth officers jacket',
#    'wear british army uniform',
#    'north',
#    'examine lenin',
#    'northeast',
#    'get blank paper',
#    'give pashka to mischa',
#    'get blank paper',
#    'southwest',
#    'give blank paper to lenin',

# The signed chit give you permission to use the smoking compartment and
# have a cigarette.

#    'northwest',
#    'z.z.z.z.z',
#    'z.z.z.z.z',
#    'get tray',

# You have a jigsaw piece.  But it's not so easy to keep it, because if
# you leave the smoking compartment carrying it, the angry passengers
# relieve you of it (even if you hide it in your backpack).  You could of
# course escape using the clock, but it's cleverer to find another way of
# disposing of it - which incidentally reveals Black's dastardly plan -
# and the "lack of ventilation" is a clue.

#    'look under bed',
#    'open grille',
#    'put jigsaw piece in grille',
#    'south',
#    'northeast',
#    'north',
#    'get jigsaw piece',
#    'spin kaldecki detector',
#    'get bomb',
#    'examine bomb',

# The bomb is clearly the work of Black, but it's not clear in what way
# history was supposed to have been changed.  But still, it's easy to save
# Lenin:

#    'throw bomb from train',
#    'south',
#    'remove british army uniform',
#    'z',
#    'press white button',
#    'enter ball',
#    'z.z',
#    'northwest',
#    'northwest',
#    '[put the edge piece at a2]',
#    'turn clock to 59',
#    'press a2',


# CHAPTER 6: WISH YOU WERE HERE
# -----------------------------

#    'examine device',
#    'spin kaldecki detector',
#    'examine window',
#    'look through window',
#    'examine young men',

# It is August 1967 and the Beatles are having trouble with their latest
# album.  Black intends to ruin the fabric of the British musical industry
# by planting 1970s progressive rock tunes into the fertile soil of
# psychedelic rock-and-roll.  Since violence is not an option, there is
# clearly only one way of stopping up Black's mouth:

#    'kiss black',
#    'z.z.z',
#    'press white button',
#    'enter ball',
#    'z.z',
#    'south',
#    'southeast',
#    'northwest',
#    'turn clock to 59',
#    'press b4',


# CHAPTER 7: IN THE WILDERNESS
# ----------------------------

#    'wait',
#    'examine device',
#    'spin kaldecki detector',

# It's 1975 and we're somewhere in North America: probably Canada or
# Alaska.  It's in such wildernesses as this that the USA keeps its
# nuclear deterrent, pointed across the north pole at the cities and
# military bases of the Soviet Union.  Black's clearly been up to no good,
# but whatever cunning plans were hatched have gone wrong.  Perhaps you
# can right them?

#    'examine snow goose',
#    'sketch snow goose',
#    'east',

# The snow goose isn't the only wild animal around here.  If you wander
# around in the forest, then eventually a snow leopard will stalk up to
# you, and wait around while you draw its portrait (but they don't have
# snow leopards in Canada...).

#    '[find the snow leopard]',
#    'sketch snow leopard',
#    '[find the Tundra again]',
#    'up',
#    'get cable',
#    'down',
#    'west',
#    'examine nest',

# The nest is clearly another jigsaw piece.  To get it you need to use the
# cable, but you also need to distract the snow goose.

#    'southwest',
#    'get broom',
#    'get seed',
#    'northeast',
#    'east',
#    'drop seed',
#    'west',
#    'throw cable at nest',
#    'pull cable',
#    'pull cable',
#    'get jigsaw piece',
#    'spin kaldecki detector',
#    'east',
#    'up',
#    'get cable',
#    'down',
#    'down',
#    'brush snow',
#    'look',
#    'tie cable to ring',
#    'down',
#    'examine missile',
#    'open hatch',
#    'enter missile',

# The moral of this episode seems to be that fooling around in time can
# create crises where there were none to start with.  Is this your fault,
# or Black's?  But you have a quest to find the jigsaw pieces, so you have
# no choice but the create the crisis and then avert it:

#    'press green button',
#    'press blue button',
#    'out',
#    'get jigsaw piece',
#    'up',
#    'z.z.z.z',
#    'z.z.z',
#    'press white button',
#    'enter ball',
#    'z.z',
#    'west',
#    'southwest',
#    'northwest',
#    '[put corner piece at d4]',
#    '[put edge piece at c4]',
#    'turn clock to 59',
#    'press b2',


# CHAPTER 8: 59 SECONDS, 852 FEET
# -------------------------------

#    'examine device',
#    'spin kaldecki detector',
#    'get paper dart',
#    'open paper dart',
#    'read herald',
#    'east',
#    'wait',
#    'wait',
#    'get bottle',
#    'west',
#    'west',
#    'examine flyer',
#    'examine crowd',
#    'examine dog',
#    'sketch dog',  

# In 1903 the Wright brothers made the first powered heavier-than-air
# flight.  It seems as though Black has decided not to interfere here, but
# you still need to help the brothers along a bit, because the aileron
# from the "Flyer" is another jigsaw piece, and they're hardly likely to
# let you just walk off with a piece of their plane, unless the flight
# were a success and they'd all run off to town to telegraph the news.

#    'east',
#    'get anemometer',
#    'get corn bread',
#    'in',
#    'get mandolin',
#    'play mandolin',
#    'again',
#    'again',
#    'again',
#    'out',
#    'north',
#    'examine anemometer',
#    'again',
#    'again',
#    'again',
#    'again',
#    'again',

# The wind speed in Dune Valley varies in a cycle of five turns, and the
# brothers try out the flyer once every five turns.  Unfortunately, the
# two cycles are synchronised so that the brothers launch just one turn
# too late to get the strongest headwind.  If only you could delay them
# for three turns, they'd have a chance.  Luckily Orville is fond of music,
# so wait until Orville has landed here (now, for example, if you're
# following the walkthrough exactly), and then:

#    'play mandolin',
#    'again',
#    'again',
#    'z.z.z.z.z',
#    'north',
#    'examine flyer',
#    'get aileron',
#    'spin kaldecki detector',
#    'up',
#    'in',
#    'examine heater',
#    'get lid',

# The second jigsaw piece is the lid of the heater, but it's not easy to
# get.  If you could put out the fire, perhaps the lid would cool, so maybe
# there's a way to stop up the air holes.

#    'put corn bread in air holes',

# Well, it almost worked.  Perhaps you can deal with the mouse.

#    'east',
#    'put bread in trap',
#    '[wait until the mouse pauses, inspecting the trap]',
#    'sketch mouse',

# But the mouse is quite capable of avoiding the trap.  But you can prevent
# the mouse from entering the kitchen by finding the evil-smelling
# mosquito powder in the attic:

#    'west',
#    'up',
#    'get book',
#    'read it',
#    'get cap',
#    'get box',
#    'examine box',
#    'down',
#    'shake box',
#    'get corn bread',
#    'put corn bread in holes',
#    'get jigsaw piece',
#    'west',
#    'west',
#    'press white button',
#    'enter ball',
#    'z.z',
#    'southeast',
#    'northwest',
#    '[put the edge piece at d3]',
#    '[put the centre piece at b3]',
#    'turn clock to 59',
#    'press c4',


# CHAPTER 9: THE HIGH POINT
# -------------------------

#    'examine device',
#    'spin kaldecki detector',

# Now the rules have been changed.  Black is not interfering with an event
# from the history you know, but from some other history.  How can this
# be?  Perhaps Black is from some alternate present.  Might it be
# conceivable that Black's present is a disaster, and that Black's clumsy
# muddlings in history are an attempt to produce something better?  This
# would give Black a more honourable motive than seems plausible from what
# has happened so far, but on the other hand it's very hard indeed to
# believe that our own present is the best of all possible worlds.

#    'get rukl',
#    'read rukl',
#    'examine black',
#    'look up littrow valley in rukl',

# Black has mixed up the coordinates for Littrow Valley, so you had better
# make sure that Black sees the correct ones.

#    'give rukl to black',
#    'ask black about astronauts',
#    'ask black about disaster',
#    'ask black about othello',
#    'z.z.z',
#    'down',
#    'enter rover',
#    'turn joystick on',
#    'southeast',
#    'get gnomon',
#    'examine gnomon',

# As well as being used by astronaut Schmitt, the pun is of course also a
# reference to Infocom's game "Trinity" (though that was a different kind
# of gnomon).

#    'northwest',
#    'north',
#    'north',
#    'get green clod',
#    'examine green clod',
#    'north',
#    'examine challenger',
#    'read plaque',
#    'north',
#    'get foil',
#    'east',
#    'climb boulder',
#    'examine pod',
#    'open pod',
#    'press button',

# The pod has three buttons; coincidentally the gnomon has three legs.

#    'open pod with gnomon',
#    'get waldo',
#    'examine waldo',

# The word "Waldo" to refer to a teleoperated device comes from the Robert
# Heinlein novel of that name, about a severely physically handicapped
# genius who attempted to rule the world by remote control.  Waldo was
# also the name of one of the teleoperated robots in the Infocom game
# "Suspended".

#    'get checklist',
#    'read checklist',
#    'southwest',
#    'enter rover',
#    'west',
#    'south',
#    'west',
#    'get out',
#    'examine reactor',
#    'examine cable',
#    'pull cable',
#    'open reactor',
#    'examine rod',

# You can't take the fuel rod without dying from radiation poisoning (and
# no doubt giving the Apollo 17 astronauts a shock when they find your
# body).  But you can make it a bit less likely to break by bandaging it:

#    'wrap rod with foil',
#    'drop all',
#    'get rod',
#    'put rod in reactor',
#    'drop rod',
#    'get all except rod',

# No doubt you will suffer nasty cancer of the hands in later life from
# handling the plutonium rod, but for now you don't seem to be suffering
# radiation poisoning.  However, you can't hold the rod and open the door
# at the same time, so you need some help.  Luckily Waldo can come to the
# rescue.  The puzzles involving Waldo are great fun, and you would do
# well to experiment with the robot before coming back to the solution.
# You need to be in the "Othello" to program it; simply "type x y", where
# "x" is a command (rturn, lturn, forward, sample) and "y" is the number
# of times the actions should be repeated.

# However, it's a bad idea to solve the reactor puzzle straight away,
# because when you do that, the time crisis will be resolved, and Black
# will steal your spacesuit, leaving you unable to find the jigsaw piece.
# So you should find the jigsaw piece first, and then come back to the
# reactor.

#    'enter rover',
#    'west',
#    'southwest',
#    'get out',
#    'southwest',
#    'examine astronauts',
#    'examine rover',

# The Apollo 17 rover's fender is a jigsaw piece, but you can't approach
# it without revealing yourself to the astronauts.  Perhaps it's possible
# to distract them; since they're looking for interesting geological
# samples, perhaps they would appreciate the green clod?

#    'throw green clod at astronauts',

# Since sound does not travel in vacuum, the astronauts don't hear the
# thud of the rock landing.  But you still can't approach the rover.
# However, Waldo is smaller than the crater rim, so if you can program
# Waldo to walk round the crater, get the piece (using its sampling arm)
# and return, you could get away without alerting the astronauts to your
# presence.

#    'northeast',
#    'enter rover',
#    'northeast',
#    'east',
#    'east',
#    'south',
#    'south',
#    'south',
#    'get out',
#    'up',
#    'type forward 2',
#    'type rturn 2',
#    'type forward 2',
#    'type sample 1',
#    'type rturn 4',
#    'type forward 2',
#    'type lturn 2',
#    'type forward 2',
#    'down',
#    'enter rover',
#    'north',
#    'north',
#    'north',
#    'west',
#    'west',
#    'southwest',
#    'get out',
#    'southwest',
#    'look',
#    'drop waldo',

# Waldo needs to be facing south for this program to work, so:

#    'turn waldo',
#    'again',
#    'again',
#    'again',
#    'press pink button',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z.z.z',
#    'get jigsaw piece',

# Now its safe to go back and solve the reactor puzzle.  First you need to
# re-program Waldo:

#    'get waldo',
#    'northeast',
#    'enter rover',
#    'northeast',
#    'east',
#    'east',
#    'south',
#    'south',
#    'south',
#    'get out',
#    'up',
#    'type clear',
#    'type forward 2',
#    'down',
#    'enter rover',
#    'north',
#    'north',
#    'north',
#    'west',
#    'get out',
#    'drop all',
#    'attach cable to waldo',
#    'examine waldo',
#    'press pink button',
#    'get rod',
#    'put rod in reactor',
#    'unplug cable',

# Oops.  Now Waldo appears to be stuck: you can't pull out the cable
# without slamming the reactor door.  But Waldo is still programmed, so
# you simply turn it round and set it going again.

#    'turn waldo',
#    'again',
#    'again',
#    'again',
#    'press button',
#    'wait',
#    'unplug cable',
#    'get all',
#    'enter rover',
#    'east',
#    'south',
#    'south',
#    'south',
#    'get out',
#    'up',
#    'z.z.z',
#    'press white button',

# It might be interesting at this point to look up all the places you have
# been in the lunar atlas.  The atlas understands: Bear Mountain, Emory
# Crater, Horatio Crater, Lara Crater, Mare Serenitas, North Massif,
# Sculptured Hills, Shorty Crater, South Massif, Taurus-Littrow Valley,
# Tortilla Flats, Tycho Crater, Velikovsky Crater, Victory Crater,
# Vitruvius Mountain, and Wessex Cleft.

#    'enter ball',
#    'z.z',
#    'west',
#    'northwest',
#    'northwest',
#    '[put edge piece at a3]',
#    'turn clock to 59',
#    'press b3',


# CHAPTER 10: THE GHOST OF THE B-29
# ---------------------------------

# You're on board a B-29 bomber, flying over the north Pacific ocean.
# Somehow, the left engine has become damaged (perhaps the bomber was
# fired upon, or perhaps it was just an accidental engine failure).  The
# crew have parachuted out, and taken all the parachutes with them.  Your
# only hope is to land the plane, but you don't have enough fuel to make
# it back to the USA, and will have to attempt a landing on Soviet soil.

# This puzzle is difficult.  If you've failed to solve it so far, and need
# some help, read the following.

# The last two indicators on the status line of the cockpit are the
# plane's bearing in degrees (clockwise from north) and its position
# (x,y).  The buttons which you can use are AUT/P (autopilot), CUTENG/L
# (turn off the left engine), CUTENG/R (turn off the right engine),
# LOWER/U (lower the undercarriage) and REL/B (open the bomb bay doors).
# If you need more fuel, then you should cut the left engine, go to the
# west side bomb bays, and press the RES/F (reserve fuel) button.  You can
# do this as often as you need to.

# The radio in the navigators chair is picking up a signal from a Russian
# base.  The radio has a three-figure display, showing the bearing of the
# plane from the base; you should head in the direction 180 degrees from
# this bearing.  Finally, if you clean the pinup of Diana Durbin, you'll
# find a secret message.  If that doesn't help, try heading for the
# position (1945,1970); an error of +-100 is acceptable.

# Finally, if even the above doesn't help, here's an example walkthrough:

#    'north',
#    'push throttle',
#    'turn aut/p on',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z.z',
#    'press cuteng/l',
#    'south',
#    'southwest',
#    'west',
#    'press res/f',
#    'east',
#    'northeast',
#    'north',
#    'turn aut/p off',
#    'pull throttle',
#    'pull throttle',
#    'turn aut/p on',
#    'push column right',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z',
#    'push column',
#    'again',
#    'again',
#    'again',
#    'again',
#    'again',
#    'again',
#    'z.z.z.z',
#    'z.z.z.z',
#    'z.z.z',
#    'press lower/u',
#    'land',

# You've landed the B-29, but the crisis isn't over; you've merely arrived
# in the right place.  Black has been double-dealing with the Soviets and
# the Americans, for the usual convoluted reasons.  You must make sure
# that Black and all other traces of the future are removed before the
# Soviets get their hands on them.  You will notice (if you type `out')
# that you won't be able to get back into the plane if you get out.  So
# first, you need to get the heavy safe out of the plane so you can deal
# with it on the ground.

#    'put all in sack',
#    'drop sack',
#    'south',
#    'southwest',
#    'examine locker',
#    'get safe',
#    'west',
#    'drop safe',
#    'east',
#    'northeast',
#    'north',
#    'get sack',
#    'press rel/b',

# Now you can leave the plane.  But you must be quick, the Soviet army
# will arrive soon and take you prisoner.

#    'out',
#    'again',
#    'east',
#    'examine chute',

# The gadget is a magical device for opening locked boxes of any kind.
# The "RZ-ROV" appellation is a reference to the "rezrov" spell in
# Infocom's game "Enchanter" (and sequels) which had much the same effect.

#    'west',
#    'put gadget on safe',
#    'open safe',
#    'get beige folder',
#    'examine beige folder',
#    'examine safe',
#    'get shelf',
#    'put all in sack',

# Now you're in captivity, and Black has clearly been interrogated under
# sedation.  What can he have told his captors?  You must hope that they
# don't believe him.

#    'black, hello',
#    'z.z.z.z.z',
#    'north',
#    'get sack',
#    'south',
#    'press white button',
#    'put drugged body of black in ball',
#    'get beige folder',
#    'get gadget',
#    'enter ball',
#    'z.z',
#   'southwest',
#    'northwest',
#    '[put jigsaw piece at d2]',

# Now you only have one jigsaw piece missing, and it's time to remember
# the glass case in the entrance to the pyramid.  You couldn't open it
# earlier, but now you have the RZ-ROV gadget.

#    'west',
#    'put gadget on case',
#    'get gadget',
#    'examine case',
#    'get jigsaw piece',
#    'east',
#    '[put jigsaw piece at d1]',
#    'turn clock to 59',
#    'press d3',


#CHAPTER 11: BANBURISMUS
#-----------------------

#    examine soldiers

#The rules have been changed yet again.  Now you are in the past in a
#ghostly form, unable to do anything except move around, examine things,
#and (taking advantage of your incorporeality) jump, and fly.  The
#information to be gained here is quite important, so remember everything
#you see here, especially the first two numbers on the paper (call these
#numbers X and Y).

#    in
#    examine black
#    examine paper
#    examine typewriter
#    examine wardrobe
#    jump
#    fly
#    out
#    fly
#    northwest
#    examine d3

#You'll notice that the picture on the jigsaw piece has changed, so
#perhaps you aren't finished with this time zone.

#    turn clock to 59
#    press d3
#    examine device
#    east
#    get cloth cap
#    wear cloth cap
#    look through window
#    sketch mallard
#    west
#    north
#    corporal, poacher

#It's 1941, and Black's plan this time is to be a British agent, spying
#on Germany for the British and sending messages in the Enigma cipher.
#Knowing Black, the messages will give misinformation of some sort.  If
#you (a suspected German spy) can decode Black's message, the people at
#Bletchley Park will think that Black is actually a double agent, and
#proceed to disbelieve Black's misinformation.  So all you have to do is
#to decode Black's message.

#Before you go to the walkthrough below, think for a moment of Turing and
#Newman and the other Bletchley Park cryptographers.  When they were
#stuck, they couldn't go to a walkthrough.  They didn't have information
#magically obtained by a ghost.  And if they failed, worse things were at
#stake than merely failing to win an adventure game!

#If you're really stuck, then try the following:

#    read intercept
#    examine crate
#    open crate
#    again
#    get enigma
#    examine enigma
#    get wheel ii
#    get wheel iv
#    get wheel v
#    put wheel ii in enigma
#    put wheel iv in enigma
#    put wheel v in enigma
#    unstecker
#    stecker a to g
#    stecker w to c
#    stecker v to t
#    stecker u to j
#    stecker y to r
#    turn machine off

#Why all the above?  You know that Black must have been using code wheels
#II, IV and V because wheels I and III were on top of the wardrobe.  You
#know five of the steckerboard connections because they were written on
#the torn scrap of paper.  You also know that there are two more
#connections to make (the remaining three wires could be seen dangling
#from Black's machine).  The machine has two modes (on and off), each of
#which decodes messages encoded by the other.  State on is typically used
#for encoding and off for decoding.

#How to decrypt?  You know the settings for wheels II and IV (they were
#on the torn scrap of paper) and there are only ten settings for wheel V.
#Try all ten possibilities.  Because there are only two stecker
#connections missing, you expect that about 8/26 letters will be wrong
#(this is because each letter has two opportunities to be transformed by
#the steckerboard, and there are four letters involved in the unknown
#connections).  Look for output that might consist of English words if
#about a third of the letters were changed.  Try to guess some of the
#wrong letters, and see if you can make stecker connections that correct
#these letters.

#If you couldn't work this out on your own, then here's a walkthrough:

#    stecker d to f
#    stecker x to p

#Then try the following with Z one of 6, 18, 5, 4, 21, 23, 14, 2, 8 or
#17, until you get it right.

#    set ii to X
#    set iv to Y
#    set v to Z
#    type intercept

#Well done if you solved it on your own, shame if you had to resort to
#the walkthrough!

#    z.z.z
#    press white button
#    enter black ball
#    z.z
#    north
#    northwest
#    northwest
#    turn clock to 59
#    press a3


#CHAPTER 12: OLD CARTRIDGE CASES
#--------------------------------

#    examine device

#It's 1989, the year that the Berlin wall fell.  This is the most recent
#historical episode in "Jigsaw"; presumably (in the author's opinion),
#nothing world-shatteringly important has happened since then.

#    west
#    north

#You may have no chance of escaping through no-man's-land, but hares roam
#there:

#    climb wall
#    southwest
#    sketch hare
#    southeast
#    climb wall
#    north
#    get rope
#    south
#    south
#    south
#    in
#    up
#    get berliner
#    examine berliner
#    get purse
#    open purse
#    get cyrillic key
#    get ostmark note
#    down
#    out
#    east
#    north
#    unlock skoda with cyrillic key
#    open skoda
#    enter skoda
#    turn skoda on
#    south
#    examine blockhouse

#If you wait, then you'll see Black fail to get in to East Berlin, but
#you still feel uneasy.  Perhaps this is one of those time zones where
#History needs a helping hand from you.

#    north
#    north
#    [wait for the street cleaner to appear]
#    give ost-mark note to street cleaner
#    look
#    read delivered note

#Black, for some reason, wants the Berlin wall to stay standing until
#1991, but you have other ideas.  It's your job to make sure that the
#people of East Berlin are given the opportunity to express the power of
#the people.

#    west
#    west
#    south
#    out
#    in
#    examine masonry
#    look under masonry
#    down
#    southwest
#    examine cables

#Perhaps if the telephone system of East Berlin were brought down, then
#the police wouldn't be able to react quickly enough to stop a mass
#demonstration?  You can't pull the cables out by hand, but maybe with
#the awesome power of the Skoda's engine?

#    tie rope to cables
#    up
#    tie rope to skoda
#    northeast
#    up
#    out
#    enter skoda
#    north
#    z.z
#    press white button
#    enter black ball
#    z.z
#    south
#    southwest
#    northwest
#    turn clock to 59
#    press d4


#CHAPTER 13: OUT OF THE EAST
#---------------------------

#    examine device
#    get eagle
#    read eagle

#1956, the year of the Suez Crisis.  Black has brokered (or attempted to
#broker) some kind of peace deal between the British and the Egyptians.
#Once again, it falls to you to ensure that war, rather than peace,
#breaks out.

#    open hotel room door
#    hit hotel room door
#    north
#    examine photo
#    northeast
#    get soap
#    southwest
#    south
#    open shutters

#If you wait around for a while, then the mosquito bites you and
#(somewhat improbably) you immediately die of malaria.  You could use the
#mosquito repellent from Kitty Hawk (this is the first dependency between
#the time zones), but if you catch the mosquito you can sketch it.

#    catch mosquito
#    sketch mosquito
#    drop soap
#    [wait until a grappling iron is thrown up to the window]
#    out
#    down
#    black, hello
#    examine cans
#    examine signed paper
#    get metal strongbox
#    open it
#    show metal box to black
#    put gadget on metal box

#Black steals the gadget from you if you are observed opening the box
#with it.

#    open metal box
#    get all from metal box
#    examine passport
#    examine charter

#You need to destroy the agreement, which turns out not to be a difficult
#task:

#    examine deck
#    kiss black
#    z.z.z
#    press white button
#    enter black ball
#    z.z
#    northwest
#    northwest
#    northwest
#    turn clock to 59
#    press d2


#CHAPTER 14: CHRISTABEL, MY DEAR
#-------------------------------

#    examine device
#    spin kaldecki detector
#    examine bobbies
#    examine suffragettes
#    in
#    black, hello

#The women's suffrage movement is going strong in 1912 (but women won't
#get the vote until 1919).  Black is up to no good; it looks as though
#the petrol bomb is intended to be the cause of a great disturbance and
#to somehow advance the suffrage cause.

#    get poster
#    read poster
#    again
#    southeast
#    sketch nightingale
#    get corn bread
#    put corn bread in fountain
#    sketch nightingale

#This use of the corn bread - or the Madeleine cake or the Berliner - is
#the third dependency between the time zones.

#    get newspaper
#    read newspaper
#    southeast
#    examine bobby
#    listen to bobby
#    get handcuffs
#    throw poster at handcuffs
#    get handcuffs
#    northwest
#    northwest
#    handcuff black to railings
#    z.z
#    press white button
#    enter ball
#    z.z
#    north
#    northeast
#    northwest
#    turn clock to 59
#    press d1


#CHAPTER 15: INTO THE DARK
#-------------------------

#    examine device

#Here you are, at the other end of the century.  Perhaps at last you will
#get some answers to all the questions you have by now...

#    north
#    ask gatekeeper about machinery
#    ask him about kaldecki
#    ask him about black
#    ask him about jigsaw
#    ask him about land
#    ask him about me
#    ask him about time
#    east


#CHAPTER 16: THE LIVING LAND
#---------------------------

#    east
#    sketch pterodactyl
#    get rod

#The black rod with a star on the end is a reference to two early
#adventure games which used this as a prop, namely Crowther and Woods'
#"Adventure" and Infocom's "Zork".  Various other references to these
#games will appear as you proceed.

#    northeast
#    wave rod

#Waving the rod could cause a crystal bridge to appear in both
#"Adventure" and "Zork".

#    north
#    east
#    get grenade
#    northwest

#You will need the grenade to destroy Kaldecki's machinery, but
#unfortunately the pterodactyl thinks that the grenade is an egg.  You
#need to persuade it to relinquish it.

#    [wait until a largish rock knocks you over]
#    get all
#    southwest
#    get oval rock

#Now the pterodactyl thinks the oval stone is an egg, too.  If you wait
#long enough, it will deposit the grenade in its nest at the top of the
#tree and take your stone.

#    examine tree
#    push tree
#    [wait until the pterodactyl takes the stone]
#    push tree
#    sketch woodpecker
#    west

#The rabbit is scared by something in your possession.  In "Adventure",
#there was a bird that was scared by the black rod.  Here, the same is
#true of the rabbit.  The rabbit doesn't like the black rod, nor does it
#like the pictures in the location corresponding to square A2.  So you
#can corner it and force it across the bridge.

#    drop rod
#    east
#    east
#    west
#    south
#    sketch apes
#    sketch rabbit

#Now the apes have the grenade, and it's hard to persuade them to
#relinquish it.  If you experiment a bit, you'll see that the apes copy
#everything you do.  You could drop an item (and the apes will drop the
#grenade), but they're faster at picking it up than you.  Instead,
#persuade them to throw it away.

#    throw ticket at rabbit
#    west
#    enter pagoda
#    get cage
#    out
#    east
#    east
#    east
#    sketch spider
#    get grenade

#Now the spider has the grenade (this is a game of pass-the-parcel).
#Perhaps the woodpecker can help?

#    west
#    west
#    north
#    catch woodpecker

#Catching a bird in a cage was a puzzle in "Adventure" (you had to not be
#carrying the rod, otherwise the bird was scared).  Here you have the
#opposite: the bird is tamed by the rod.

#    west
#    get rod
#    east
#    catch woodpecker
#    east
#    south
#    east
#    open cage
#    get grenade
#    drop grenade

#The grenade sticks to your hands.  But the acid in the polluted river
#emerging from the pyramid can get rid of the glue.

#    put grenade in river
#    west
#    west
#    pull pin
#    put grenade in river
#    z.z.z.z


#EPILOGUE
#--------

#You have come full circle.  The start of the game saw the end of the
#twentieth century; now you are back at the beginning.  And the
#significance of the sketch-book finally becomes apparent.

#    northwest
#    toby, hello
#    give sketch book to toby

#You need to sketch at least four animals before you can get a prize in
#the drawing competition.

#    southeast
#    east
#    examine cases
#    west
#    black, hello
#    ask black about kaldecki
#    'give teddy bear to black'

# I added this:
	"score"

# If you've been following the script exactly, you will have scored 100
# out of 100, giving you the rank of Centurion, and you'll have got 16 out
# of 16 in the drawing competition.
	]
	return walkthrough

# Select the input box
#input_box = driver.find_element_by_name('a')

# Send input information
#input_box.send_keys('inventory')

# Find Enter button
#center_buton = driver.find_element_by_name('f')

# Click Enter
# enter_button.submit()
#input_box.submit()

walkthrough = loadWalkthrough()

print(len(walkthrough))
for x in range(0, len(walkthrough)) :
	input_box = driver.find_element_by_name('a')
	input_box.send_keys(walkthrough[x])
	input_box.submit()
	time.sleep(1)