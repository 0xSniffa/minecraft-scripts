import minescript
import math
import sys
import time
def exit():
    minescript.execute("/tellraw @s {\"text\":\"Please supply a name\",\"color\":\"green\"}")
    minescript.execute("/tellraw @s [\"Usage: \",{\"text\":\"babysitV2 \",\"color\":\"aqua\"},{\"text\":\"<name>\",\"color\":\"dark_green\"}]")
    minescript.execute("/tellraw @s [\"Example: \",{\"text\":\"babysitV2 \",\"color\":\"aqua\"},{\"text\":\"sweeper\",\"color\":\"dark_green\"}]")
    sys.exit(1)


# -------- INFO ----------
# The variable weStart should contain the start coordinate.
# So if your WorldEater is heading from north-south/south-north then set weStart to the coordinate most south
# If the WorldEater is heading east-west/west-east then set it to the most east
# -------- CONFIG --------
renderDistance = 16
weStart = 2000
weLength = 4000
botHeight = 120
botName = str(sys.argv[1]) if len(sys.argv) > 1 else exit()
# ---------- ADVANCED CONFIG -------------
timeInBetweenSpawn = 0.3

#  utility vars
renderDistanceBlocks = renderDistance*16
position = minescript.player_position()
absoluteRotation = minescript.player_orientation()
relativeRotation = (absoluteRotation[0] + 180) % 360 - 180

# direction decision && spawning logic
print(relativeRotation)

if relativeRotation < 45 and relativeRotation > -45: # looking south
    print(f"looking south")
    for i in range(abs(math.ceil((weStart-position[2])/(renderDistanceBlocks)/2))):
        minescript.execute(f"/player {botName}{i} spawn at {position[0]} {botHeight} {position[2]+(i*renderDistanceBlocks*2)+renderDistanceBlocks}")
        time.sleep(timeInBetweenSpawn)

elif relativeRotation < -45 and relativeRotation > -135: # looking east
    print(f"looking east")
    for i in range(abs(math.ceil((weStart-position[0])/(renderDistanceBlocks)/2))):
        minescript.execute(f"/player {botName}{i} spawn at {position[0]+(i*renderDistanceBlocks*2)+renderDistanceBlocks} {botHeight} {position[2]}")
        time.sleep(timeInBetweenSpawn)

elif relativeRotation > 45 and relativeRotation < 135: # looking west
    print(f"looking west")
    for i in range(abs(math.ceil((weStart-weLength-position[0])/(renderDistanceBlocks)/2))):
        minescript.execute(f"/player {botName}{i} spawn at {position[0]-(i*renderDistanceBlocks*2)-renderDistanceBlocks} {botHeight} {position[2]}")
        time.sleep(timeInBetweenSpawn)

elif relativeRotation < -135 or relativeRotation > 135: # looking north
    print(f"looking north")
    for i in range(abs(math.ceil((weStart-weLength-position[2])/(renderDistanceBlocks)/2))):
        minescript.execute(f"/player {botName}{i} spawn at {position[0]} {botHeight} {position[2]-(i*renderDistanceBlocks*2)-renderDistanceBlocks}")
        time.sleep(timeInBetweenSpawn)

else: # something else
    print(f"looking at transition.\nPlease rotate a little.\n\nIf there's anything else please open an issue.\nGithub: https://github.com/weirdge/minescript/issues")