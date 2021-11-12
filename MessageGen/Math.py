"""
Math module for
Message Generator
"""

# <--- Import --->

# <--- Import from --->
from MessageGen.Helpers import Coordinates

def calculate_center(
    x1: int,
    y1: int, 
    x2: int, 
    y2: int) -> Coordinates:
    """
    Calculating center
    of one image when placed
    to another
    """
    x = int(.5 * x1) - int(.5 * x2)
    y = int(.5 * y1) - int(.5 * y2)
    
    return Coordinates(x, y)