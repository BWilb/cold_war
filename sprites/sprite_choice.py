import arcade

def game_logic():
    user_choice = input("Which nation will you choose? ")

class SpriteChoices(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.height = height
        self.length = width
        self.faction_options = ["1. Nato",
                                "2. Shanghai Pact",
                                "3. Warsaw Pact"]

        self.nato_nations = ["1. United States",
                             "2. United Kingdom",
                             "3. France",
                             "4. Belgium",
                             "5. Netherlands",
                             "6. Italy",
                             "7. Turkey",
                             "8. West Germany"]

        self.warsaw_nations = ["1. Soviet Union",
                               "2. East Germany",
                               "3. Romania",
                               "4. Hungary",
                               "5. Poland",
                               "6. Czechoslovakia"]

        self.shanghai_nations = ["1. China",
                                 "2. North Korea",
                                 "3. Mongolia",
                                 "4. Vietnam",
                                 "5. Cambodia"]

    def on_draw(self):
        arcade.start_render()
        self.background_color = arcade.color.BLACK

        for i in range((self.height - 200), 0, -1):
            # drawing separators
            arcade.draw_text("|",
                             560,
                             i,
                             arcade.color.LIME_GREEN,
                             25)

        for i in range((self.height - 200), 0, -1):
            arcade.draw_text("|",
                             1100,
                             i,
                             arcade.color.LIME_GREEN,
                             25)
        for i in range((self.length), 0, -50):
            arcade.draw_text("_",
                             i,
                             1050,
                             arcade.color.LIME_GREEN,
                             25)
        arcade.draw_text("CHOOSE YOUR SIDE!!!",
                         625,
                         1100,
                         arcade.color.SKY_BLUE,
                         25)
        arcade.draw_text("Push Spacebar to exit",
                         700,
                         1075,
                         arcade.color.SKY_BLUE,
                         15)

        for i in range(0, len(self.faction_options) + 1):
            if i == 0:
                arcade.draw_text(self.faction_options[i], 205, 1000, arcade.color.LIME_GREEN, 25)
            elif i == 1:
                arcade.draw_text(self.faction_options[i], 700, 1000, arcade.color.LIME_GREEN, 25)
            elif i == 2:
                arcade.draw_text(self.faction_options[i], 1200, 1000, arcade.color.LIME_GREEN, 25)

        height = 950
        for i in range(len(self.nato_nations)):
            arcade.draw_text(self.nato_nations[i], self.length - 1715, height, arcade.color.LIME_GREEN, 15)
            height -= 50

        size = 950
        for i in range(len(self.shanghai_nations)):
            arcade.draw_text(self.shanghai_nations[i], 700, size, arcade.color.LIME_GREEN, 15)
            size -= 50

        fun = 950
        for i in range(len(self.warsaw_nations)):
            arcade.draw_text(self.warsaw_nations[i], 1200, fun, arcade.color.LIME_GREEN, 15)
            fun -= 50
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            arcade.finish_render()
            arcade.close_window()
            game_logic()


def main():
    choices = SpriteChoices(1920, 1200, "Choose")
    arcade.run()

if __name__ == '__main__':
    main()