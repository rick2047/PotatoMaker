import arcade
from belt import Belt

# Screen Setup
from grid import Grid

SPRITE_SCALING = 0.5
GRID_WIDTH = 25
GRID_HEIGHT = 15
TILE_SIZE = 64
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

SCREEN_TITLE = "Potato Maker"


class GameWindow(arcade.Window):
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE):
        super().__init__(width, height, title)

        self.source = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
        self.destination = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
        arcade.set_background_color(arcade.color.PASTEL_YELLOW)
        self.belt_list = arcade.SpriteList()
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = Grid()

    def setup(self):
        self.source.bottom = 0
        self.source.center_x = 40
        self.destination.bottom = 500
        self.destination.center_x = 700

        # List of points the belt will travel too.
        position_list = [[self.source.center_x, self.source.center_y],
                         [self.destination.center_x - 500, self.destination.center_y - 300],
                         [self.destination.center_x, self.destination.center_y]]
        # Create the belt
        belt = Belt(":resources:images/tiles/grassMid.png",
                    SPRITE_SCALING,
                    position_list)
        # Set initial location of the belt at the first point
        belt.center_x = position_list[0][0]
        belt.center_x = position_list[0][1]

        # Add the enemy to the enemy list
        self.belt_list.append(belt)

    def on_draw(self):
        self.clear()
        # self.source.draw()
        # self.destination.draw()
        # self.belt_list.draw()
        self.grid.draw()

    def on_update(self, delta_time):
        self.belt_list.update()

    def on_mouse_press(self, x, y, button, modifiers):
        self.grid.on_click(x, y)


def main():
    game = GameWindow()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
