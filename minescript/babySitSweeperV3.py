import minescript
import math
import time
import sys
from dataclasses import dataclass

def exit():
    minescript.execute("/tellraw @s {\"text\":\"Please supply a name\",\"color\":\"green\"}")
    minescript.execute("/tellraw @s [\"Usage: \",{\"text\":\"babysitV3 \",\"color\":\"aqua\"},{\"text\":\"<name>\",\"color\":\"dark_green\"}]")
    minescript.execute("/tellraw @s [\"Example: \",{\"text\":\"babysitV3 \",\"color\":\"aqua\"},{\"text\":\"sweeper\",\"color\":\"dark_green\"}]")
    sys.exit(1)

# -------- INFO ----------
# The variable weStart should contain the start coordinate.
# So if your WorldEater is heading from north-south/south-north then set weStart to the coordinate most south
# If the WorldEater is heading east-west/west-east then set it to the most east
# -------- CONFIG --------
renderDistance = 16
weStart = 2000
weLength = 4000
dimension = "overworld"
# ---------- ADVANCED CONFIG -------------
botHeight = 120
timeInBetweenSpawn = 0.3 # in seconds
sweeperBPS = 2 # how many blocks per second the sweeper moves
botGamemode = "spectator"
botName = str(sys.argv[1]) if len(sys.argv) > 1 else exit()


#  utility vars, don't change
renderDistanceBlocks = renderDistance*16
position = minescript.player_position()
absoluteRotation = minescript.player_orientation()
relativeRotation = (absoluteRotation[0] + 180) % 360 - 180

@dataclass
class amount():
    direction: str # world direction (east, south, west, north)
    amount: int # rought 2x the amount of bots needed
    positive: int # determines the direction e.g (south or north) or (east or west)
    position: int # 0 = Z | 1 = X | determines which coordinate gets increased e.g. x or z
    angle1: int # angle1 to find direction
    angle2: int # angle2 to find direction
    distance: int # distance from player to Worldeater

directions = [
amount("east",  abs(math.ceil((weStart-position[0])/(renderDistanceBlocks))),           1,  1, -45,  -135, weStart-position[0]),
amount("south", abs(math.ceil((weStart-position[2])/(renderDistanceBlocks))),           1,  0,  45,   -45, weStart-position[2]),
amount("west",  abs(math.ceil((weStart-weLength-position[0])/(renderDistanceBlocks))), -1,  1, 135,    45, weStart-weLength-position[0]),
amount("north", abs(math.ceil((weStart-weLength-position[2])/(renderDistanceBlocks))), -1,  0, 180,  -180, weStart-weLength-position[2]), # -135 135. This could be removed and replaced with an if/else
]


for i in range(len(directions)):
    if relativeRotation < directions[i].angle1 and relativeRotation > directions[i].angle2:
        print(f"Looking: {directions[i].direction} | Rotation: {round(relativeRotation)}°")
        looking = directions[i]
        c = 0
        print(f"Sweeper ETA: {abs(round((looking.distance/sweeperBPS)/60))}:{abs(round((looking.distance/sweeperBPS)%60))}min | {abs(round(looking.distance))} Blocks")
        for j in range(looking.amount):
            if j%2==1 or j == looking.amount-1:
                time.sleep(timeInBetweenSpawn)
                minescript.execute(f"/player {botName}{c} spawn at {position[0]+looking.positive*renderDistanceBlocks*j*looking.position} {botHeight} {position[2]+looking.positive*renderDistanceBlocks*j*int(not looking.position)} facing 0 0 in minecraft:{dimension} in {botGamemode}")
                c+=1
        break