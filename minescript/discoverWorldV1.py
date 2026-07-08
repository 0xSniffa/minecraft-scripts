import math
import minescript
import time

## Change as you like
renderDistance = 16 # render distance in chunks
discoverDistance = 5000 # range of blocks to discover (in blocks)(square radius)
waitTime = 10 # time inbetween each teleport
teleportHeight = 250 # height that the player is teleported to
startCountdown = 8 # in seconds
#### don't change

blockRenderDistance = renderDistance * 16
amount = math.ceil(discoverDistance / blockRenderDistance)
totalAmount=(2*amount)**2
ETA = (2*amount)**2 * waitTime
counter = 0

def start(seconds):
    print(f"Remember type \'\\z\' to exit")
    print(f"ETA: {convert(ETA)}")
    print(f"Total Teleports: {totalAmount}")
    for i in range(seconds):
        print(f"Starting in : {seconds-i}s")
        time.sleep(1)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    return "%d:%02d:%02d" % (hour, minutes, seconds)

start(startCountdown)

for i in range(2*amount):
    for j in range(2*amount):
        minescript.execute(f"tp {-discoverDistance + i * blockRenderDistance} {teleportHeight} {-discoverDistance + j * blockRenderDistance}")
        print(convert(ETA - counter*waitTime))
        counter+=1
        time.sleep(waitTime)
