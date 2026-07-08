import minescript
import sys

# ------------
# The amount will be amount+1.
# This means if bot y3, y1, y2, y3 are online you'll have to enter 3 as amount
# ------------

def exit():
    minescript.execute("/tellraw @s {\"text\":\"Please supply a name and amount\",\"color\":\"green\"}")
    minescript.execute("/tellraw @s [\"Usage: \",{\"text\":\"kill \",\"color\":\"aqua\"},{\"text\":\"<name> <amount>\",\"color\":\"dark_green\"}]")
    minescript.execute("/tellraw @s [\"Example: \",{\"text\":\"kill \",\"color\":\"aqua\"},{\"text\":\"x 4\",\"color\":\"dark_green\"}]")
    sys.exit(1)

name = str(sys.argv[1]) if len(sys.argv) > 2 else exit()
number = int(sys.argv[2]) if len(sys.argv) > 2 else exit()

for i in range(number+1):
    minescript.execute(f"/player {name}{i} kill")
