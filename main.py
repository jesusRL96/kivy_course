from kivy.app import App
from kivy.metrics import dp

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.stacklayout import StackLayout 
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400,200,80), width=2)
            Line(rectangle=(600,400,150,100), width=3)
            Rectangle(pos=(600,100), size=(100, 200))

class CanvasExample3(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample1(Widget):
    pass


class WidgetExamples(GridLayout):
    count = 1
    count_enable = BooleanProperty(False)
    my_text = StringProperty(f"Count: {count}")
    text_input_str = StringProperty("foo")
    # slider_value_text = StringProperty(f"Value: {50}")
    def on_button_click(self):
        print('button clicked')
        if self.count_enable:
            self.count += 1
            self.my_text = f"Count: {self.count}"

    def on_toggle_button_state(self, toggle_button):
        print('toggle state: ', toggle_button.state)
        if toggle_button.state == "normal":
            # OFF
            toggle_button.text = "OFF"
            self.count_enable = False
        else:
            # ON
            toggle_button.text = "ON"
            self.count_enable = True
    
    def on_switch_active(self, widget):
        print('active state: ', widget.active)

    def on_slider_value(self, widget):
        print('Value: ', widget.value)
        # self.slider_value_text = f"Value: {widget.value:.2f}"

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

        


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