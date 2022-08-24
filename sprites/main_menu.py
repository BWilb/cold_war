import arcade
import time

class Menu(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        options = ["1. Play Game",
                   "2. Options",
                   "3. Quit"]
        arcade.start_render()

        arcade.draw_lrtb_rectangle_outline(480,
                                           1440,
                                           900,
                                           300,
                                           color=arcade.color.BRONZE)

        for i in range(len(options)):
            y_placement = 900
            arcade.draw_text(options[i],
                             960,
                             y_placement - 100,
                             color=arcade.color.AVOCADO)

            arcade.draw_text(options[i],
                             960,
                             y_placement - 200,
                             color=arcade.color.AVOCADO)

            arcade.draw_text(options[i],
                             960,
                             y_placement - 300,
                             color=arcade.color.AVOCADO)

        user_choice = input("what do you choose?: ")

def main():
    menu = Menu(1920, 1200, "Cold War")
    arcade.run()
main()