from gasp import *
the_maze= Maze 
while not the_maze.finished():
    the_maze.play()
the_maze.done()  
class Maze:                                   # This should already be in your program
    # ...                                     # Other definitions will be here

    def set_layout(self, layout):
        height = len(layout)                   # Length of list
        width = len(layout[0])                 # Length of first string
        self.make_window(width, height)
        self.make_map(width, height)           # Start new map

        max_y = height - 1
        for x in range(width):                 # Go through whole layout
            for y in range(height):
                char = layout[max_y - y][x]    # See discussion 1 page ago
                self.make_object((x, y), char) #

class Immovable:
    pass                                   # We have nothing to put in this class yet

class Nothing(Immovable):
    pass

class Maze:                                # This should already be in your program
    # ...                                  # Other definitions will be here

    def make_map(self, width, height):
        self.width = width                 # Store size of layout
        self.height = height
        self.map = []                      # Start with empty list
        for y in range(height):
            new_row = []                   # Make new row list
            for x in range(width):
                new_row.append(Nothing())  # Add entry to list
            self.map.append(new_row)  