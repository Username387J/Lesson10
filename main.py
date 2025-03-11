import random
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

    if game_over :
        display_message("GAME OVER","Try again.")
    elif game_complete :
        display_message("YOU WON","Congratulations")
    else:
        for item in items:
            item.draw()

def display_message(heading,subheading):
    screen.draw.text(heading, fontsize = 60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(300,300), color="black")

def update():
    global items 
    if len(items) == 0:
        items = make_items(current_level)
#Make items
#1.get the options from ITEMS list - random
#2.Create actors and add it to items list
#3.Layout items - display them with equal spacing
#4.Animations - move the objects down

#Abstraction : callling a function that has not been created
def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    
    for i in range (0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
        
    return items_to_create



def create_items(items_to_create):
    return []


def layout_items(items_to_layout):
    pass 

def animate_items(items_to_animate):
    pass


    

pgzrun.go()




