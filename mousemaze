from ursina import *
from PIL import Image
import sys

BLACK = (0,0,0)
GREEN = (34, 177, 76)

try:
    save = open("savefile", "r").read()
    print(save)
except FileNotFoundError:
    save = "1"


level = "levels/" + save + ".png"

app = Ursina()


image = Image.open(level)
width, height = image.size
window.windowed_size = (width, height)
window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True
camera.orthographic = True

bg = Entity(model='quad', texture=level, scale_x=width/height)
bg.scale *= 40
bg.aspect_ratio = bg.scale_x / bg.scale_y

det = True
won = False

def update():
    try:
        x = round((mouse.position[0] + 0.5) * width)
        y = round((abs(mouse.position[1] - 0.5)) * height)
        print(x,y,image.getpixel((x, y)))
        if image.getpixel((x, y)) == BLACK and det:
            det = False
            exit()
            sys.exit(0)
            
        if image.getpixel((x, y)) == GREEN and det:
            det = False
            print("congrats")
            open("savefile", "w").write(str(int(save) + 1))
            exit()
            sys.exit(0)
        
    except:
        pass

app.run()
    
