from random import randint
import pgzrun
WIDTH=800
HEIGHT=600
TITLE="RECYCLING GAME"

START_SPEED = 10
ITEMS = ["bag","battery","bottle","chips"]

FINAL_LEVEL = 6
current_level = 1

game_over = False
game_complete = False

items = []
animations = []
def draw():
    screen.clear()
    screen.blit("bg",(0,0))




pgzrun.go()




