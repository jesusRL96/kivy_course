from kivy.app import App
from kivy.metrics import dp

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.stacklayout import StackLayout 
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.properties import StringProperty


class WidgetExamples(GridLayout):
    count = 1
    my_text = StringProperty(f"Count: {count}")
    def on_button_click(self):
        print('button clicked')
        self.count += 1
        self.my_text = f"Count: {self.count}"


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(100):
            # size = dp(100 + i*10)
            size = dp(100)
            b =  Button(text=f"Button {i+1}", size_hint=(None,None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"

    #     b1 = Button(text="Button1")
    #     b2 = Button(text="Button2")
    #     b3 = Button(text="Button3")

    #     self.add_widget(b1)    
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()