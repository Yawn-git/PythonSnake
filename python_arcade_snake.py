import arcade
from random import randrange
from time import sleep

SCREEN_WIDTH = 380
SCREEN_HEIGHT = 400

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'Snake Game', update_rate=0.09)

        self.score = 0

        self.gameOn = None

        self.moved = None
        self.snake_image = arcade.Sprite('snake.png')
        self.snake_coords = []
        self.snake_move_x = 0
        self.snake_move_y = 20

        self.head_image = arcade.Sprite('head.png')             
        self.snake_head = None
        self.new_head_position = None
        self.direction = [0,1]

        self.food_image = arcade.Sprite('food.png')
        self.food_coord = []

    def setup(self):
        self.snake_coords = [
            [90,90],
            [90,70],
            [90,50]
        ]
        self.snake_head = self.snake_coords[0]

        self.food_coord = [randrange(10,370,20), randrange(10,350,20)]
        
        self.gameOn = True

    def on_key_press(self, symbol: int, modifiers: int):
        self.moved = True
        if symbol == arcade.key.D and self.direction[0] != -1:
            self.snake_move_x = 20;self.snake_move_y = 0
            self.direction = [1,0]
        if symbol == arcade.key.A and self.direction[0] != 1:
            self.snake_move_x = -20;self.snake_move_y = 0
            self.direction = [-1,0]
        if symbol == arcade.key.W and self.direction[1] != -1:
            self.snake_move_y = 20;self.snake_move_x = 0
            self.direction = [0,1]
        if symbol == arcade.key.S and self.direction[1] != 1:
            self.snake_move_y = -20;self.snake_move_x = 0
            self.direction = [0,-1]


    def on_draw(self):
        arcade.start_render()

        self.food_image.center_x = self.food_coord[0]
        self.food_image.center_y = self.food_coord[1]
        self.food_image.draw()

        self.head_image.center_x = self.snake_coords[0][0]
        self.head_image.center_y = self.snake_coords[0][1]
        self.head_image.draw()

        for x, y in self.snake_coords[1:]:
            self.snake_image.center_x = x;self.snake_image.center_y = y
            self.snake_image.draw()

        arcade.draw_text(f'Score: {self.score}', 20, SCREEN_HEIGHT-20, arcade.csscolor.WHITE, 12, font_name='arial')

    def update(self, delta_time: float):
        if self.snake_head == self.food_coord:
            self.score += 1
            self.food_coord = [randrange(10, 370, 20), randrange(10, 350, 20)]
            self.snake_coords.append(self.snake_coords[-1][0]+20)

        if self.moved:
            if self.snake_head[0] < 10:
                sleep(1);quit()
            elif self.snake_head[0] > SCREEN_WIDTH - 10:
                sleep(1);quit()
            elif self.snake_head[1] < 10:
                sleep(1);quit()
            elif self.snake_head[1] > SCREEN_HEIGHT - 10:
                sleep(1);quit()
            else:
                self.snake_head = self.snake_coords[0]
                self.new_head_position = [self.snake_head[0]+self.snake_move_x, self.snake_head[1]+self.snake_move_y]
                self.snake_coords = ([self.new_head_position] + self.snake_coords[:-1])

        if self.new_head_position in self.snake_coords[1:]:
            sleep(1);quit()






def main():
    win = MyWindow()
    win.setup()
    arcade.run()

if __name__ == '__main__':
    main()
