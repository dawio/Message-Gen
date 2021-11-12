"""
Message generator
made by WXS in 2021
code is under MIT
license
"""

# <--- Import --->
import MessageGen.Math as Math
import MessageGen.Helpers as Helpers

# <--- Import from --->
from PIL import Image, ImageDraw
from typing import Optional
from MessageGen.Helpers import Coordinates, Size, Color

class Message:
    image_pil: Image.Image
    def __init__(
        self,
        header: str,
        sub_header: str,
        image_size: Optional[Size] = Size(500, 500),
        message_size: Optional[Size] = Size(400, 400),
        background_color: Optional[Color] = Color(137, 207, 240),
        message_color: Optional[Color] = Color(255, 255, 255),
        font_color: Optional[Color] = Color(0, 0, 0)
    ) -> None:
        """
        Message generator
        
        header           - The header text on top of image\n
        sub_header       - The smaller text under header\n
        image_size       - Size of the whole image\n
        message_size     - Size of message box\n
        background_color - Color of background\n
        message_color    - Color of message box\n
        font_color       - Color of header && subheader font.\n
        """
        self.image_pil = Image.new(
            mode = "RGB",
            size = image_size.to_tuple(),
            color = background_color.to_tuple()
        )
        
        # Layout calculation
        
        coordinates = Math.calculate_center(
            x1 = image_size.width,
            y1 = image_size.height,
            x2 = message_size.width,
            y2 = message_size.height
        )
        
        message_box = (
            coordinates.x,
            coordinates.y,
            coordinates.x + message_size.width,
            coordinates.y + message_size.height
        )
        
        rectangle = Image.new(
            mode = "RGB",
            size = message_size.to_tuple(),
            color = message_color.to_tuple()
        )
        
        draw = ImageDraw.Draw(rectangle)
        draw.rectangle(
            xy = message_box,
            fill = message_color.to_tuple()
        )
        
        OFFSET = (5, 5)
        SHADOW_BORDER = 8
        rectangle = Helpers.drop_shadow(
            image = rectangle, 
            background = background_color.to_tuple(),
            border = SHADOW_BORDER,
            offset = OFFSET,
        )

        header_area = (
            SHADOW_BORDER, 
            SHADOW_BORDER, 
            rectangle.width - (abs(OFFSET[0]) + SHADOW_BORDER),
            rectangle.height * 0.1
        )
        
        sub_header_area = (
            header_area[0],
            header_area[1] + header_area[3],
            header_area[2],
            rectangle.height * 0.9
        )
        
        Helpers.add_header(
            image = rectangle,
            text = header,
            working_area = header_area,
            font_color = font_color
        )
        
        Helpers.add_sub_header(
            image = rectangle,
            text = sub_header,
            working_area = sub_header_area,
            font_color = font_color
        )
        
        self.image_pil.paste(
            im = rectangle,
            box = message_box[:2]
        )
    
        
    def get_image_pil(self): 
        return self.image_pil
    
    def show(self):
        self.image_pil.show()
        
    def save(self, path: str):
        self.image_pil.save(path)
        
   

