import arcade
import math
movment = 5
class Avatar:
    def __init__(self, x, y, change_x, change_y, radius, color):
        self.position_x = x
        self.position_y = y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.current_name = "Adolf Hitler"

    def draw(self):
        # draw method for Avatar
        # arcade.draw_circle_filled(self.position_x,
        #                          self.position_y,
        #                          self.radius,
        #                          self.color)

        # draws main body
        arcade.draw_ellipse_filled(self.position_x,
                                   (self.position_y - self.radius / 4),
                                   self.radius / 1.5,
                                   self.radius,
                                   color=arcade.color.BROWN)

        # draws head
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y + 50,
                                  # math.sqrt(self.radius),
                                  self.radius / 4,
                                  self.color)

        # draws left eye
        arcade.draw_circle_filled(self.position_x - 10,
                                  self.position_y + 60,
                                  (self.radius / 20),
                                  color=arcade.color.BLUE)

        # draws right eye
        arcade.draw_circle_filled(self.position_x + 10,
                                  self.position_y + 60,
                                  (self.radius / 20),
                                  color=arcade.color.BLUE)

        # draws right arm
        arcade.draw_line((self.position_x + self.radius / 4),
                         self.position_y,
                         (self.position_x + (self.radius / 2) + 25),
                         self.position_y - 25,
                         color=arcade.color.BROWN)

        # draws left arm
        arcade.draw_line((self.position_x - self.radius / 4),
                         self.position_y,
                         (self.position_x - (self.radius / 2) - 10),
                         self.position_y - 25,
                         color=arcade.color.BROWN)

        # draws right leg
        arcade.draw_line((self.position_x + 10),
                         (self.position_y - self.radius / 4),
                         self.position_x + 25,
                         (self.position_y - self.radius - 25),
                         color=arcade.color.BROWN)

        # draws left leg
        arcade.draw_line((self.position_x - 10),
                         (self.position_y - self.radius / 4),
                         (self.position_x - 25),
                         (self.position_y - self.radius - 25),
                         color=arcade.color.BROWN)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class ColdWar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.avatar = Avatar(100, 400, 4, 4, 100, color=arcade.color.BRONZE)
        self.enemy_list = None
        self.year = 1960

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)

        arcade.draw_lrtb_rectangle_filled(0,
                                          1920,
                                          1100,
                                          931,
                                          arcade.color.BLACK)

        arcade.draw_text(f"Year {self.year}",
                         720,
                         931,
                         arcade.color.BRONZE,
                         20)

        arcade.draw_text("Current name: " + self.avatar.current_name,
                         640,
                         1031,
                         arcade.color.BRONZE,
                         20)

    def update(self, delta_time: float):
        self.avatar.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.avatar.change_x = movment
        elif key == arcade.key.LEFT:
            self.avatar.change_x = -movment
        elif key == arcade.key.UP:
            self.avatar.change_y = movment
        elif key == arcade.key.DOWN:
            self.avatar.change_y = -movment
        elif key == arcade.key.SPACE:
            self.avatar.current_name = input("What would you like to change your name to?: ")
            self.avatar.draw()

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.avatar.change_x = 0
        elif key == arcade.key.LEFT:
            self.avatar.change_x = 0
        elif key == arcade.key.UP:
            self.avatar.change_y = 0
        elif key == arcade.key.DOWN:
            self.avatar.change_y = 0


def main():
    cold = ColdWar(1920, 1100, "Cold War")
    arcade.run()

if __name__ == '__main__':
    main()