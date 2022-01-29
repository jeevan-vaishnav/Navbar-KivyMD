from kivymd.app import MDApp
from kivy.lang import Builder


class NavBarIcon(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    NavBarIcon().run()
