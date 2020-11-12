"""
Python Script used to draw the shape you would like your print on your arduino printer.
    INSTRUCTIONS:
    -Press start
    -draw your shape using the arrow pads
    -once you are satisfied with the shape, press space. This will close the program, and cache your drawing for the arduino script
NOTICE: The arcade and numpy library must be installed for this project to work.
"""


import arcade
import numpy

PIXEL_SIZE = 2
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80

class Cursor():
    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_WIDTH/2
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, PIXEL_SIZE, PIXEL_SIZE, arcade.color.GREEN)


class Game(arcade.Window):
    """
    This class handles all the "game" callback. I have used the Arcade library simply because it is a library that I am familiar with that
    can work as a sort of GUI.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        
        self.file = open("drawing.c", "w")
        self.held_keys = set()
        arcade.set_background_color(arcade.color.WHITE)
        self.cursor = [Cursor()]
        self.record = []
  
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        #for pixels in self.pixel:
        for line in self.cursor:
            line.draw()
            
        self.check_keys()
        
                
    def check_keys(self):
        """
        This function checks for keys that are being held down.
        This moves the cursor up and down
        """
        if arcade.key.LEFT in self.held_keys:
            object = self.cursor[-1]
            object.x -= 1
            self.cursor.append(object)
            self.record.append("1")
        if arcade.key.RIGHT in self.held_keys:
            object = self.cursor[-1]
            object.x += 1
            self.cursor.append(object)
            self.record.append("2")
        if arcade.key.UP in self.held_keys:
            object = self.cursor[-1]
            object.y += 1
            self.cursor.append(object)
            self.record.append("3")
        if arcade.key.DOWN in self.held_keys:
            object = self.cursor[-1]
            object.y -= 1
            self.cursor.append(object)
            self.record.append("4")

        # Close the program

        if arcade.key.SPACE in self.held_keys:
            self.file.write('char drawing[] = "')
            for i in self.record:
                self.file.write(i)
            self.file.write('";')
            self.file.close()
            exit()
            

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        self.held_keys.add(key)

        if key == arcade.key.SPACE:
            pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
        
  
  
  

    
    