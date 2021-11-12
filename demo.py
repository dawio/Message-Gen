"""i
Module with examples
"""

# <--- Import --->
import sys

# <--- Import from --->
from MessageGen.Gen import Message
from MessageGen.Helpers import Color, Size
from time import time as timestamp

class App:
    def __init__(self):
        header = sys.argv[1]
        sub_header = sys.argv[2]
        msg = Message(
            header = header,
            sub_header = sub_header,
            image_size = Size(1920, 1920),
            message_size = Size(1080, 1080),
            background_color = Color(255, 255, 51),
            message_color =  Color(64, 64, 64),
            font_color = Color(255, 255, 255)
        )
        
        msg.save("output.png")
        

if __name__ == "__main__":
    _ = App()
