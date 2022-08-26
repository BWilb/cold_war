import arcade
import sprite_choice
def game_logic():
    # based off of the choices on the image projected
    user_choice = input("Which option do you choose?: ")
    if user_choice.lower() == "play" or user_choice.lower() == "play game":
        # Another file will be created listing all the different nations to play

        print("not available")
    elif user_choice.lower() == "options":
        print("printing options")
    elif user_choice.lower() == "quit":
        print("good bye")

class Menu(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.options = ["1. Play Game",
                        "2. Options",
                        "3. Quit"]

    def on_draw(self):
        self.y_placement = 1000
        arcade.start_render()
        self.background_color = arcade.color.BLACK

        arcade.draw_text("Options",
                         750,
                         975,
                         color=arcade.color.BRONZE)

        arcade.draw_lrtb_rectangle_outline(460,
                                           1160,
                                           1050,
                                           600,
                                           color=arcade.color.BRONZE)

        for i in range(len(self.options)):
            arcade.draw_text(self.options[i],
                             720,
                             self.y_placement - 100,
                             arcade.color.BRONZE, 16)
            self.y_placement -= 100

        arcade.draw_text("Go back to console to choose: Push Space bar",
                         600,
                         500,
                         arcade.color.GREEN_YELLOW, 16)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            arcade.finish_render()
            arcade.close_window()
            game_logic()

def main():
    menu = Menu(1920, 1200, "Cold War")
    arcade.run()

main()
