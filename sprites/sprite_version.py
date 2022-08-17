import arcade
class ColdWar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)


def main():
    cold = ColdWar(1920, 1100, "Cold War")
    arcade.run()

main()