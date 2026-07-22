import minescript
import sys, math, time
from dataclasses import dataclass

def exit():
    minescript.execute("/tellraw @s {\"text\":\"Please supply a mine direction and name\",\"color\":\"green\"}")
    minescript.execute("/tellraw @s [\"Usage: \",{\"text\":\"trench \",\"color\":\"aqua\"},{\"text\":\"<name> <amount>\",\"color\":\"dark_green\"}]")
    minescript.execute("/tellraw @s [\"Example: \",{\"text\":\"trench \",\"color\":\"aqua\"},{\"text\":\"n 12\",\"color\":\"dark_green\"}]")
    sys.exit(1)

def roundHalf(num):
    return round(num - 0.5) + 0.5

# -------- CONFIG --------
timeInBetweenSpawn = 0.3
# ------------------------

#  utility vars
name = str(sys.argv[1]) if len(sys.argv) > 2 else exit()
count = int(sys.argv[2]) if len(sys.argv) > 2 else exit()
position = minescript.player_position()
finalPos = [roundHalf(position[0]), math.floor(position[1]), roundHalf(position[2])]
absoluteRotation = minescript.player_orientation()
relativeRotation = (absoluteRotation[0] + 180) % 360 - 180


@dataclass
class amount():
    direction: str
    angle1: int
    angle2: int
    positive: int
    position: int # 0 = Z | 1 = X
    yaw: int

directions = [
    amount("spawn West mine North",   90,  135, -1, 1, 180),
    amount("spawn East mine North", -135,  -90,  1, 1, 180),
    amount("spawn North mine East", -180, -135, -1, 0, -90),
    amount("spawn South mine East",  -45,    0,  1, 0, -90),
    amount("spawn West mine South",   45,   90, -1, 1,   0),
    amount("spawn East mine South",  -90,  -45,  1, 1,   0),
    amount("spawn South mine West",    0,   45,  1, 0,  90),
    amount("spawn North mine West",  135,  180, -1, 0,  90)
]

for i in range(len(directions)):
    if relativeRotation > directions[i].angle1 and relativeRotation < directions[i].angle2:
        print(f"{directions[i].direction}")
        print(f"rotation: {round(relativeRotation)}")
        looking = directions[i]
        for j in range(count):
            time.sleep(timeInBetweenSpawn)
            minescript.execute(f"/player {name}{j} spawn at {finalPos[0]+(j+1)*looking.positive*looking.position} {finalPos[1]} {finalPos[2]+(j+1)*looking.positive*int(not looking.position)} facing {looking.yaw} 45")
        break
