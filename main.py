import arcade
from isort import file
from sklearn.preprocessing import scale
import copy

# Screen Setup
GRID_WIDTH = 25
GRID_HEIGHT = 15

TILE_SIZE = 64

SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

SCREEN_TITLE = "Potato Maker"

class Machine(arcade.Sprite):
    def __init__(self, filename, grid_x, grid_y,scale=0.5):
        super().__init__(filename=filename,scale=scale)

        self.center_x = grid_x * TILE_SIZE + (TILE_SIZE/2)
        self.center_y = grid_y * TILE_SIZE + (TILE_SIZE/2)

        self.grid_x = grid_x
        self.grid_y = grid_y

class Ingredient(arcade.Sprite):
    def __init__(self, filename, center_x, center_y, scale=0.5):
        super().__init__(filename=filename, scale=scale)
        self.center_x = center_x
        self.center_y = center_y

class Producer(Machine):
    def __init__(self, filename, grid_x, grid_y,output_ingrident,facing=(0,1),scale=0.5):
        super().__init__(filename, grid_x, grid_y, scale)
        self.facing_x = facing[0] * TILE_SIZE
        self.facing_y = facing[1] * TILE_SIZE

        self.output_ingrident =output_ingrident

    def produce(self,scene):
        ingredient_sprite_list = scene.get_sprite_list("ingredients")
        a = arcade.get_sprites_at_point((self.center_x + self.facing_x, self.center_y + self.facing_y), ingredient_sprite_list)
        if a == []:
            o = copy.deepcopy(self.output_ingrident)
            o.center_x = self.center_x + self.facing_x
            o.center_y = self.center_y + self.facing_y
            scene.add_sprite("ingredients", o)
            print("added")

class Consumer(Machine):
    pass

class Transformer(Machine):
    pass

class GameWindow(arcade.Window):
    def __init__(self, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.PASTEL_YELLOW)

        # Declare and Initialize variables
        self.scene = None
        self.time = 0
    
    def setup(self):
        o = Ingredient(":resources:images/items/coinBronze.png",-1,-1,scale=0.5)
        p = Producer(":resources:images/tiles/lavaTop_high.png",12,6, o)
        self.scene = arcade.Scene()
        self.scene.add_sprite("producers",p)
        self.scene.add_sprite_list("ingredients")

    def on_draw(self):
        self.clear()

        self.scene.draw()

    def on_update(self, delta_time):
        self.time += 1
        if self.time %60 == 0:
            a = self.scene.get_sprite_list("producers")
            for p in a:
                p.produce(self.scene)


def main():
    game = GameWindow()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()