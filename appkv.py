from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MainWindow(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="hi"))


class MyApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    app = MyApp()
    app.run()
