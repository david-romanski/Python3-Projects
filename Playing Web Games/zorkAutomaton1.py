# David Romanski
# Started 04/22/2020
# zorkAutomaton1
# Comments: Zork Deaf, Dumb, and Blind Automated Walkthrough

import time
import selenium
from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome();

# Open the website
driver.get('http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq')

def loadWalkthrough():
	walkthrough = [	
#Zork 1 Walkthrough
#Introduction.
#Part 1  Surface and Jewelled Egg
#Part 2  Chimney and Painting
#Part 3  Troll, Cyclops and Thief; Coins, Chalice, Canary and Bauble
#Part 4  Evil Spirits, Platinum Bar, Ivory Torch, Coffin, Sceptre, and Crystal Skull
#Part 5  Pot of Gold, Scarab
#Part 6  Crystal Trident, Trunk of Jewels, Emerald
#Part 7  Jade Figurine, Bracelet, Diamond, Map
#Introduction
#I do not believe that there is a definitive highest points / least moves walkthrough because of the random appearance of the Thief. Though this walkthrough does not visit every area it is played in a reasonably natural way as an adventurer might who had done some preliminary exploration, and who wanted to deal with sources of danger expeditiously.
#[Feedback]  [Home Page]  [Top of Page]
#Part 1  Surface and Jewelled Egg
#At the start of the game you are at the West Side of the White House. 
"Go North", #to the North Side, then 
"North", #again to the Forest Path. Go Up the Tree and get the Jewelled Egg. Go down, then North again to the Clearing. Get the Leaves to reveal the Grating, then drop the Leaves.
#"Go East to the eastern Dimly Lit Forest, then South to the Small Clearing. Let us presume that you have been East to explore the Canyon View and have noted the Rainbow, the Frigid River and the Aragain Falls.
#"Go West to the Behind House area, Open the Window, and Enter the Kitchen.
#"Open the Brown Sack and get the Garlic. Go West into the Living Room. Drop the Garlic. Get the Lamp. Go back East into the Kitchen, and Up to the Attic. Turn on the Lamp before the Grue gets you. Get the Knife and the Rope. Go back Down again, Turn the Lamp off, and go East into the Living Room. Drop the Knife and the Rope. Put the Egg in the Trophy Case.
#"[Feedback]  [Home Page]  [Top of Page]
#"Part 2   Chimney and Painting
#"Pull the Rug, open the Trapdoor, and go Down into the Cellar. Turn on the Lamp.
#"Go South into the East of Chasm, and East into the Art Gallery. Take the Painting, and go North into the Studio. You should be carrying only the Lamp and the Painting. Go Up the Chimney to the Kitchen. Turn the Lamp off. Go West into the Living Room, and Put the Painting into the Trophy Case.
#"[Feedback]  [Home Page]  [Top of Page]
#"Part 3  Troll, Cyclops and Thief; Coins, Chalice, Canary and Bauble
#"Get the Jewelled Egg and the Sword. Open the trapdoor again, and go Down. Turn on the Lamp. Save the Game. Go North into the Troll Room and Kill the Troll with the Sword. It may take several repetitions of 'Kill the Troll with the Sword' to do it, and you may get killed yourself.
#"Go West into the Maze of Twisty Passages, All Alike, and then South, East, and Up. This brings you to the Skeleton Room. Get the Bag of Coins, and the Skeleton Key. Do not take the the Rusty Knife, or touch the Skeleton.
#"Continue SW, East, South, and SE through the Maze to meet the Cyclops in the Cyclops Room. Say either name of the man who blinded his father to scare away him away. Save the Game. Go Up to the Treasure Room, quickly give the Jewelled Egg to the Thief, and then go Down. Go East through the Strange Passage and East again into the Living Room. Turn off the Lamp, and put the Bag of Coins into the Trophy Case.
#"Drop the Sword and get the Knife. Turn on the Lamp. Go West through the Strange Passage to the Cyclops Room. Save the Game. Go Upstairs and Kill the Thief with the Knife. It may take several repetitions of 'Kill the Thief with the Knife' to do it, and you may get killed yourself.
#"Get the Jewelled Egg which is open to show a Golden Canary within it, the Silver Chalice, and all the other objects in the room. Take them East to the Living Room. It may take more than one trip. Turn off and Drop the Lamp.
#"Get the Canary. Put the Jewelled Egg, the Silver Chalice and the other Treasures into the Trophy Case.
#"Go East and East again(through the Window) to Behind the House, then North through the North Side to the Forest Path. Climb the Tree, and Wind the Golden Canary. The Singing Bird will drop the Brass Bauble on your head. Go Down the Tree and get the Bauble. Go South through the North Side and East through Behind House. Enter the House, then go West into the Living Room. Put the Golden Canary and the Brass Bauble into the Trophy Case.

#"[Feedback]  [Home Page]  [Top of Page]
#"Part 4  Evil Spirits; Platinum Bar, Ivory Torch, Coffin, Sceptre, and Crystal Skull
#"Drop the Knife and get the Sword, if only for its ability to warn of danger. Get the Rope.
#"Open the Trapdoor, go Down into the Cellar, and turn on the Brass Lantern.
#"Go North to the Troll Room, East to the E/W Passage and East again to the Round Room. Now that the Thief has been disposed of you can cache things without concern, so drop the Rope for the time being. Go East into the Loud Room, say 'Echo', and get the Platinum Bar. Go West back to the Round Room and drop the Bar.
#"Go North to the N/S Passage and NE to the Deep Canyon. Go East to the Top of Dam, then North to the Dam Lobby and get the Matches. Go East (or North) to the Maintenance Room, and get the Screwdriver and the Wrench. Press the Yellow Button. Go West and South back to the Top of Dam, and turn the Bolt with the Wrench. Go Down to the Dam Base and note that there is a deflated Inflatable Boat there. Go back Up, then South, SW, and South to the Round Room. Drop the Screwdriver and the Wrench, and get the Rope.
#"Go SE into the Engravings Cave then East to the Dome Room. Tie the Rope to the railing.
#"Go Down to the Torch Room and get the Ivory Torch. Turn off the Brass Lantern to conserve its battery. Go Down the stairs to the North End of Temple. Go East to the Egyptian Room. Open the Coffin and note that it contains a Sceptre. Wave the Sceptre and note that it emits a flash of multicoloured light. Put it back into the Coffin.
#"Your load is too heavy to carry the Coffin, so drop everything except the Lamp and turn it on. Get the Coffin, go West and then South to the Altar Room, and drop the Coffin. It is too big to get through the hole (the program will tell you that you haven't a prayer) and too heavy to get up the stairs, so leave it there for now.
#"Go back to the Egyptian Room to get all your possessions, turn the Lamp off, then go West to the North End of Temple to get the Bell. Go back South to the Altar Room and get the Book and the Candles.
#"Go Down into the Tiny Cave. The fact that you must go Down clearly indicates that the Underground Empire was designed by a disciple of M.C. Escher. Go Down again to the Entrance to Hades where the Evil Spirits will either ignore or jeer at you. Save the Game. Ring the Bell, which will become red hot and fall from your hands together with the Candles which will go out.
#"Get the Candles, Light the Match, Light the Candles, and Read the Book. A voice will banish the Evil Spirits. Go South into the Land of the Dead, and get the Crystal Skull, which hardly seems worth the effort.
#"Retrace your steps back to the Tiny Cave. Go North to the Mirror Room and North and North again to the Round Room. Drop the Book, the Candles, and the Matches. Get the Platinum Bar. Go West to the E/W Passage and West again to the Troll Room. Go South to the Cellar and Up into the Living Room. Put the Crystal Skull, the Platinum Bar, and the Torch in the Trophy Case.

#"[Feedback]  [Home Page]  [Top of Page]
#"Part 5  Pot of Gold and Scarab
#"The Coffin and Sceptre were left behind. So Drop the Sword, Go Down, Turn on the Lamp, and retrace your steps through the Cellar, Troll Room, and E/W Passage to the Round Room. Go SE and E to the Dome Room and Down the Rope to the Torch Room. Go Down and South into the Altar Room, Get the Coffin, and Pray. You will be transported (complete with Coffin, Sceptre, and Lamp) to the Forest, East Sunlight. Turn the Lamp off.
#"There is not much point in lugging the Coffin around, so go East to the Forest Path, South to the North Side of the House, and East to the Behind House area. The Coffin has magically become smaller and lighter so that you can get it through the Window and into the Trophy Case. Before you put the Coffin into the Trophy Case Get the Sceptre. Drop the Lamp and the the Torch.
#"Go East to the Behind House area, East again to the Small Clearing, and East again to the Canyon View. Go Down to the Ledge, and Down again to the Canyon Bottom. Go North to the End of Rainbow, and Wave the Sceptre. The Rainbow will solidify so that you can walk on it and a Pot of Gold will appear. Get it, and Go East and East again to the Aragain Falls.
#"Go North to the Shore and North again to the Sandy Beach. Get the Shovel, and go NE to the Sandy Cave. Save the game. Dig in Sand (it took me four tries) until the Scarab appears. Get it, and then go SW (without having to climb out of the hole) to the Sandy Beach, and South to the Shore. Go South again to the Aragain Falls. Go West and West again to the End of Rainbow, SW to the Canyon Bottom, and Up twice to the Canyon View. Go NW to the Small Clearing, West to Behind House, West and West again to the Living Room. Put the Pot of Gold, the Scarab and the Sceptre in the Trophy Case.

#"[Feedback]  [Home Page]  [Top of Page]
#"Part 6  Crystal Trident, Trunk of Jewels, Emerald
#"You obviously haven't finished the game, though it seems that you have been everywhere. There must be at least one hidden area.
#"For the next part trust me, you need to travel light and can't take sharps. Go Down into the Cellar, North through the Troll Room, and East through the E/W Passage to the Round Room. Go South through the Narrow Passage into the Mirror Room. You've no doubt heard of two way mirrors, so Rub the Mirror to see if this is one. You will find yourself in the Other Mirror Room.
#"Go East to the Other Tiny Cave. Go Down into the Atlantis Room and Get the Crystal Trident. Go South again, and you will find yourself on the North Side of the Reservoir. Get the Airpump. Keep going South, and because you have opened the Sluice Gates you will see and be able to Get a Trunk of Jewels.
#"Go South again to the South Side of the Reservoir, then East to the Top of Dam, and go Down to the Dam Base where you will find an Inflatable Boat.
#"Inflate the Boat, Get In, and Launch the Boat on to the Frigid River. Save the Game. Look repeatedly until you see the Buoy. Get it, and immediately Go East to the Sandy Beach. Open the Buoy, get the Emerald, and drop the Buoy.
#"Go South past the Shore to the Aragain Falls, and East twice to the End of Rainbow. Go SW to the Canyon Bottom, and Up twice to the Canyon View. Go NW to the Small Clearing, and West three times to the Living Room. Put the Crystal Trident, the Trunk of Jewels, and the Emerald into the Trophy Case.

#"[Feedback]  [Home Page]  [Top of Page]
#"Part 7  Jade Figurine, Bracelet, Diamond, Map
#"You still haven't finished, so get the lamp, garlic, and sword, and get ready for perhaps the most laborious part of the game.
#"Go Down into the Cellar, North to the Troll Room, and East through the E/W Passage to the Round Room. Get the Screwdriver you left here earlier, and go South through the N/S Passage to the Mirror Room. Rub the Mirror again to get into the Other Mirror Room, but this time go North into the Cold Passage. Go West into the Slide Room, and note the other end of the slide leading to the Cellar. Go North to the Mine Entrance, and West to the Squeeky Room where your Sword will warn you of impending danger. Go North into the Bat Room. Since you are carrying the Garlic the Vampire will cower away on the ceiling where you can't get to him. Drop the Garlic. There is a Jade Figurine here, but leave it for now.
#"Go East into the Shaft Room. Put the Torch and the Screwdriver in the Basket, but do not lower it yet. Go North into the Smelly Room and Turn on the Lamp. Go Down into the Gas Room. Leave the Bracelet for now.
#"Go East into the Coal Mine, which is a cleverly disguised maze. Go East, NE, SE, SW, and Down to get to the Ladder Top, and Go Down to the Ladder Bottom. Go West into the Timber Room and note that the passage to the West is so narrow that you cannot take anything through except the Screwdriver. Go East again, and then South to the Dead End and Get the Coal. Retrace your steps North and Up (twice) to the Coal Mine. Go North, East, South, and North to the Gas Room. Go Up through the Smelly Room and Down to the Shaft Room, and Put the Coal into the Basket. Lower the Basket.
#"Retrace your steps yet again to the Timber Room, drop the Lamp and the Sword and Go West into the Drafty Room where you will find the Basket and its contents. Get the Torch, Screwdriver, and Coal. Go South into the Machine Room.
#"Open the Lid of the Machine, Put the Coal into the Machine, Close the Lid, and Turn the Switch with the Screwdriver. After the pyrotechnics have finished Open the Lid and get the Diamond. Drop the Screwdriver. Go North to the Drafty Room, and put the Diamond and Torch into the Basket.
#"Go back for the last time to the Shaft Room, collecting the Lamp, Sword, and Bracelet on the way. Raise the Basket and get the Diamond and the Torch. Turn the Lamp off. Go West into the Bat Room and Get the Jade Figurine. Go South to the Squeeky Room, East to the Mine Entrance, and South the the Slide Room. Go Down via the Slide to the Cellar.
#"Go Up to the Living Room. Put the Bracelet, Diamond, Jade Figurine and Torch into the Case. A Voice will tell you to look among the Treasures, where you will find a Map.
#"Just for the sake of completeness Go East and East again to the Behind House area, South and West to the West Side. Go SW to the Stone Barrow. When I entered the Barrow the game terminated. On to Zork 2.

#"[Feedback]  [Home Page]  [Top of Page]
#"[Opera Software's Project Magic!]
#"Validated 3.2
#"Use Any Browser
#"This page hosted by GeoCities
#"Geocities
#"Get your own Free Home Page",

	"score"

	]
	return walkthrough

walkthrough = loadWalkthrough()

print(len(walkthrough))

print(len(walkthrough))

time.sleep(3)
for x in range(0, len(walkthrough)) :
	input_box = driver.find_element_by_class_name('div.main')
#	input_box.send_keys(walkthrough[x])
#	input_box.submit()
	time.sleep(1)

#//*[@id="parchment"]/div[2]/span[12]/input
#/html/body/div/div[2]/span[12]/input

#//*[@id="parchment"]/div[2]/span[4]/input
#/html/body/div/div[2]/span[4]/input
# input.TextInput

