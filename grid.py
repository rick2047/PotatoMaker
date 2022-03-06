import arcade

NUM_COLUMNS = 25
NUM_ROWS = 15
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 54
HEIGHT = 54
SPRITE_SCALING = 0.5

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5


class Grid:
    def __init__(self):
        self.source = arcade.Sprite(":resources:images/items/flagGreen1.png", SPRITE_SCALING)
        self.destination = arcade.Sprite(":resources:images/items/flagRed1.png", SPRITE_SCALING)
        self.belt_list = arcade.SpriteList()
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(NUM_ROWS):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(NUM_COLUMNS):
                self.grid[row].append(0)  # Append a cell

    def draw(self):
        for row in range(NUM_ROWS):
            for column in range(NUM_COLUMNS):
                # Do the math to figure out where the box is
                center_x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                center_y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                # Figure out what color to draw the box
                if self.grid[row][column] == 0:
                    arcade.draw_rectangle_filled(center_x, center_y, WIDTH, HEIGHT, arcade.color.WHITE)
                elif self.grid[row][column] == 1:
                    self.source.center_x = center_x
                    self.source.center_y = center_y
                    self.source.draw()
                elif self.grid[row][column] == 2:
                    self.destination.center_x = center_x
                    self.destination.center_y = center_y
                    self.destination.draw()
                elif self.grid[row][column] == 3:
                    arcade.draw_rectangle_filled(center_x, center_y, WIDTH, HEIGHT, arcade.color.BLACK)

    def on_click(self, x, y):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < NUM_ROWS and column < NUM_COLUMNS:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 3:
                self.grid[row][column] = 0
            else:
                self.grid[row][column] += 1
