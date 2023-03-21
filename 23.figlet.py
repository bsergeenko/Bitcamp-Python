import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet = Figlet(font = random.choice(Figlet().getFonts()))
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    my_font = sys.argv[2]
    if my_font in fonts:
        figlet.setFont(font = my_font)
    else:
        sys.exit()
else:
    sys.exit()

text = input("Input: ")

print(figlet.renderText(text))
