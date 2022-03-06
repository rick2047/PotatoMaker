import arcade

# Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = "Potato Maker"

class GameWindow(arcade.Window):
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.PASTEL_YELLOW)
    
    def setup(self):
        pass

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