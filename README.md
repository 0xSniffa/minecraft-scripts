# Scarpet + Minescript scripts

# 
>[!warning]
> The scarpet scripts currently due not work. I'll investigate as soon as possible

> [!NOTE]
> - To run the `.py` scripts you'll need the [Minescript mod](https://minescript.net/).
> - To run the `.sc` scripts you'll only need the [Carpet mod](https://modrinth.com/mod/carpet).


---
## Babysit Sweepers V3
- [Minescript](./minescript/babySitSweeperV3.py)
- [Scarpet](#) - Coming Soon
>[!NOTE]
> - This script requires the [Carpet mod](https://modrinth.com/mod/carpet) and it's [/player](https://github.com/gnembon/fabric-carpet/wiki/Commands#player) command.
> - WorldEater start coordinates have to be set in the file config.

>[!warning]
> - **[V2](./minescript/outdated/babysitSweeperV2.py) has bugs and is not working correctly, use [V3](./minescript/babySitSweeperV3.py)!**
> - This script only has a basic error handling!

This script will spawn bots along the length of the WorldEater.
Especially useful for big Worldeaters/Perimeters.

How to use:
If your WorldEater is heading **North-South** enter the **most South** coordinate.
If it's heading **East-West** then enter the **most East** coordinate.

1. unstuck the sweeper
2. look into the direction where the sweeper is going to head
3. start the bot spawning script by typing `\babysitSweeperV3 <name>`
4. start the Sweeper
5. once the sweeper is docked, kill all the bots by using the [kill](/README.md#kill-bots) script.

![Image](/src/gridSweeper.png)

Open issue [here](https://github.com/weirdge/scarpet.minescript/issues).

---

## Trench bot spawner
- [Minescript](./minescript/trenchSpawn.py)
- [Scarpet](./scarpet/trench.sc)
>[!NOTE]
> - This script requires the [Carpet mod](https://modrinth.com/mod/carpet) and it's [/player](https://github.com/gnembon/fabric-carpet/wiki/Commands#player) command

Used for spawning bots to dig bottom trench of Trenchers

**Usage:** 
Python: `\trenchSpawn <name> <amount>`
Scarpet: `/trench <name> <amount>`

**Example:** 
Python: `\trenchSpawn n 12`
Scarpet: `/trench n 12`

![Trench image](/src/trenchSpawn.png)

[Trench image 1](/src/trench1.png)

[Trench image 2](/src/trench2.png)

---

## Discover V1
- [Minescript](./minescript/discoverWorldV1.py)
- [Scarpet](#) Coming Soon
> [!NOTE]  
> - You have to have Op rights to use this script since it relies on `/tp`
> - The config variable still have to be set in the file. V2 will fix this.

This program uses teleports to discover the world. It can be useful for WorldMap or Distant Horizons/Voxy.

![How the program works](/src/gridV1.png)



---
## Misc
Utility scripts

### Kill bots
- [Minescript](./minescript/killBots.py)
- [Scarpet](#) Coming Soon

This will kill all bots that match the given arguments

Usage: `\killBots <name> <amount>`

Example: `\killBots x 4`

### Get player rotation
- [Minescript](./minescript/getPlayerRotation.py)
- [Scarpet](./scarpet/getPlayerRotation.sc)

This script simply outputs the players rotation

**Usage:** 
Python: `\getPlayerRotation`
Scarpet: `/getPlayerRotation`

---
# Todo
- [ ] Add Error handling ([Babysit](./babysitSweeperV2.py))
- [ ] Do [discoverWorld](./discoverWorldV1.py) V2

![discoverV2](./src/gridV2.png)
