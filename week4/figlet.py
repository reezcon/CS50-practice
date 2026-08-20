from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
fonts = figlet.getFonts()

def render_with_font(f):
    text = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(text))

if len(sys.argv) == 1:
    render_with_font(choice(fonts))
else:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        render_with_font(sys.argv[2])
    else:
        sys.exit("Error")
