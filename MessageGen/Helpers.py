"""
Helper classes
for MessageGen
"""

# <--- Import --->
import MessageGen.Math as Math
import textwrap

# <--- Import from --->
from dataclasses import dataclass
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from typing import Optional
from string import ascii_letters


@dataclass
class Size:
    """
    Class for storing
    width and height of
    object
    """
    width: int
    height: int
    
    def to_tuple(self):
        return (self.width, self.height)
    
@dataclass
class Coordinates:
    """
    Class for stroing
    Coordinates of object
    """
    x: int
    y: int
    
    def to_tuple(self):
        return (self.x, self.y)
    
@dataclass
class Color:
    """
    Class for storing
    RGB info
    """
    r: int
    b: int
    g: int
    
    def to_tuple(self):
        return (self.r, self.b, self.g)
    

# Author: Kevin Schluff
# License: Python license
def drop_shadow( image, offset=(5,5), background=0xffffff, shadow=0x444444, 
                border=8, iterations=3):
  """
  Add a gaussian blur drop shadow to an image.  
  
  image       - The image to overlay on top of the shadow.
  offset      - Offset of the shadow from the image as an (x,y) tuple.  Can be
                positive or negative.
  background  - Background colour behind the image.
  shadow      - Shadow colour (darkness).
  border      - Width of the border around the image.  This must be wide
                enough to account for the blurring of the shadow.
  iterations  - Number of times to apply the filter.  More iterations 
                produce a more blurred shadow, but increase processing time.
  """
  
  # Create the backdrop image -- a box in the background colour with a 
  # shadow on it.
  totalWidth = image.size[0] + abs(offset[0]) + 2*border
  totalHeight = image.size[1] + abs(offset[1]) + 2*border
  back = Image.new(image.mode, (totalWidth, totalHeight), background)
  
  # Place the shadow, taking into account the offset from the image
  shadowLeft = border + max(offset[0], 0)
  shadowTop = border + max(offset[1], 0)
  back.paste(shadow, [shadowLeft, shadowTop, shadowLeft + image.size[0], 
    shadowTop + image.size[1]] )
  
  # Apply the filter to blur the edges of the shadow.  Since a small kernel
  # is used, the filter must be applied repeatedly to get a decent blur.
  n = 0
  while n < iterations:
    back = back.filter(ImageFilter.BLUR)
    n += 1
    
  # Paste the input image onto the shadow backdrop  
  imageLeft = border - min(offset[0], 0)
  imageTop = border - min(offset[1], 0)
  back.paste(image, (imageLeft, imageTop))
  return back

def predict_text_size(
        text: str,
        font: ImageFont.FreeTypeFont
    ) -> Size:
        """
        Method to properly
        predict text size
        in PIL
        """
        ascent, descent = font.getmetrics()

        width = font.getmask(text).getbbox()[2]
        height = font.getmask(text).getbbox()[3] + descent
        
        return Size(width, height)

def max_font_size(
    text: str,
    working_area: tuple[int, int, int, int],
    font_path: str,
    start_font_size: Optional[int] = 200,
) -> int:
    """
    Calcualates max font size
    to given working area.
    
    Slightly odified version of
    https://issueexplorer.com/issue/python-pillow/Pillow/5669
    """
    size = None
    font_size = start_font_size
    
    while (size is None or \
           size[0] > working_area[2] - working_area[0] or \
           size[1] > working_area[3] - working_area[1]) and \
           font_size > 0:
               
        font = ImageFont.truetype(font_path, font_size)
        size = font.getsize_multiline(text)
        font_size -= 1
        
    return font_size
    

def add_header(
    image: Image.Image,
    text: str,
    working_area: tuple[int, int, int, int],
    font_color: Optional[Color] = Color(0, 0, 0),
    site_margin: Optional[int] = 15
) -> bool:
    """
    Adds header text onto image
    """
    
    # Margin
    working_area = (
        working_area[0] + site_margin,
        working_area[1],
        working_area[2] - site_margin,
        working_area[3] 
    )

    FONT_PATH = "MessageGen/fonts/PlayfairDisplay-MediumItalic.ttf"
    FONT_SIZE = max_font_size(text, working_area, FONT_PATH)
    FONT = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    TEXT_SIZE = predict_text_size(text, FONT)
            
    coordinates = Math.calculate_center(
        *working_area[2:],
        *TEXT_SIZE.to_tuple()
    )
    
    draw = ImageDraw.Draw(image)
    
    draw.multiline_text(
        text = text,
        xy = coordinates.to_tuple(),
        font = FONT,
        fill = font_color.to_tuple()
    )
    
def add_sub_header(
    image: Image.Image,
    text: str,
    working_area: tuple[int, int, int, int],
    font_color: Optional[Color] = Color(0, 0, 0),
    font_size: Optional[int] = 40,
    site_margin: Optional[int] = 15
) -> bool:
    """
    Adds header text onto image
    """
    
    # Margin
    working_area = (
        working_area[0] + site_margin,
        working_area[1],
        working_area[2] - site_margin,
        working_area[3] 
    )
    
    FONT_PATH = "MessageGen/fonts/lemon-milk-font/LemonMilkBold-gx2B3.otf"
    FONT = ImageFont.truetype(FONT_PATH, font_size)
    
    # Slightly changed version of
    # https://www.alpharithms.com/fit-custom-font-wrapped-text-image-python-pillow-552321/
    average_char_width = sum(FONT.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)      
    max_char_count = int((working_area[2] * .95) / average_char_width)
    
    text = textwrap.fill(text, max_char_count)
    text_size = FONT.getsize_multiline(text)
    
    coordinates = Math.calculate_center(
        *working_area[2:],
        *text_size
    )
        
    draw = ImageDraw.Draw(image) 
    
    draw.text(
        text = text,
        xy = coordinates.to_tuple(),
        font = FONT,
        fill = font_color.to_tuple()
    )
    
    

    
    
    
    
    
    
    
    