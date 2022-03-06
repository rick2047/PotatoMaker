import arcade

# Screen Setup
GRID_WIDTH = 25
GRID_HEIGHT = 15

TILE_SIZE = 64

SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

SCREEN_TITLE = "Potato Maker"

class GameWindow(arcade.Window):
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.PASTEL_YELLOW)

        # Declare and Initialize variables
        self.scene = None
    
    def setup(self):
        self.scene = arcade.Scene()

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time):
        pass


def main():
    game = GameWindow()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()