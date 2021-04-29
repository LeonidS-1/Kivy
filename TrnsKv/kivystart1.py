import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.base import runTouchApp

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle

from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout

from kivy.uix.behaviors import ButtonBehavior

from kivy.graphics import Color, Canvas, Rectangle

# [.53, .58, .63, 1] - Discord
# [ .41, .55, .73. 1] - VK
# [ .0, 1, .55, 1] - My

#btnclr = [ .35, .04, .76, 1]

allowed_letters = '1234567890qwertyuiopasdfghjklzxcvbnm'



class KivyApp(App, Widget):
    
    def build(self):
          
        self.layout = FloatLayout()
        def redraw(self, args):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

        self.widget = Widget()
        with self.widget.canvas:
            self.widget.bg_rect = Rectangle(source="background.png", pos=self.pos, size=self.size)
        self.widget.bind(pos=redraw, size=redraw)
        self.layout.add_widget(self.widget)
        #
        self.welcome_screen()
        #
        return self.layout
        
    def callback(self, instance, value):
        def timer(who):
            self.layout.clear_widgets()
            self.typing_screen()

        #instance.text \\ value - normal/down
        if value == 'normal' and instance.text == 'Начать':  
            self.layout.remove_widget(self.welcome_btn)
            
            self.animated_part_1 = Button(\
            background_normal = "btnpic2.png",        
            background_down = "btnpic2.png",
            size_hint = (.5, .25),            
            pos_hint = {'x': 0, 'y': .75},)

            self.animated_part_2 = Button(\
            background_normal = "btnpic2.png",        
            background_down = "btnpic2.png",
            size_hint = (.5, .25),            
            pos_hint = {'x': .5, 'y': .75},)

            
            self.layout.add_widget(self.animated_part_1)
            self.layout.add_widget(self.animated_part_2)
            Clock.schedule_once(timer, .55)
            self.animate(self.animated_part_1)
            self.animate(self.animated_part_2)
            

    
    def animate(self, instance):
        if instance == self.animated_part_1:
            animation = Animation(pos_hint = {'x': 0, 'y': .75}, size_hint = (.5, .25), duration=.5)
            animation &= Animation(pos_hint = {'x': 0, 'y': .5}, size_hint = (1, .25), duration=.5)
        if instance == self.animated_part_2:
            animation = Animation(pos_hint = {'x': .5, 'y': .75}, size_hint = (.5, .25), duration=.5)
            animation &= Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .25), duration=.5)

        animation.start(instance)

        
   
    def welcome_screen(self):    
        #root = Widget()
        #root.add_widget(Button())
        #self.layout.add_widget(root)
        self.welcome_btn = Button(\
        text='Начать',
        background_normal = "btnpic2.png",
        background_down = "btnpic1.png",
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .75},)
        self.welcome_btn.bind(state=self.callback)
        self.layout.add_widget(self.welcome_btn)
    
        
    def typing_screen(self): 
        self.text1 = ''
        self.text2 = '' 
        self.type_process = False
        def typing_process(instance, value):
            if instance == self.btn1:                      
                self.type_process = 1
            elif instance == self.btn2:
                self.type_process = 2
        def _on_keyboard_down(keyboard, keycode, text, modifiers):
            
            if self.type_process == 1:
                if keycode[1] == 'backspace':
                    self.text1 = self.text1[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False
                elif keycode[1] == 'spacebar':
                    self.text1+=' ' 
                else:
                    letter_check = 0
                    while letter_check != len(allowed_letters):
                        letter_check+=1
                        if f'{keycode[1]}' == allowed_letters[letter_check-1:letter_check]:
                            self.text1+=f'{keycode[1]}'
                            break
                

                self.layout.remove_widget(self.btn1)
                self.btn1 = Button(\
                text=f'{self.text1}',
                background_normal = "btnpic2.png",
                background_down = "btnpic1.png",
                size_hint = (1, .25),
                pos_hint = {'x': 0, 'y': .5},)
                self.btn1.bind(state=typing_process)
                self.layout.add_widget(self.btn1)
            elif self.type_process == 2:
                if keycode[1] == 'backspace':
                    self.text2 = self.text2[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False  
                elif keycode[1] == 'spacebar':
                    self.text2+=' '           
                else:
                    letter_check = 0
                    while letter_check != len(allowed_letters):
                        letter_check+=1
                        if f'{keycode[1]}' == allowed_letters[letter_check-1:letter_check]:
                            self.text2+=f'{keycode[1]}'
                            break
                

                self.layout.remove_widget(self.btn2)
                self.btn2 = Button(\
                text=f'{self.text2}',
                background_normal = "btnpic2.png",
                background_down = "btnpic1.png",
                size_hint = (1, .25),
                pos_hint = {'x': 0, 'y': .25},)
                self.btn2.bind(state=typing_process)
                self.layout.add_widget(self.btn2)   

            if self._keyboard.widget:
                pass
    


        def close_keyboard():
            self._keyboard.unbind(on_key_down=_on_keyboard_down)
            self._keyboard = None

        self._keyboard = Window.request_keyboard(close_keyboard, self, 'text')
        self._keyboard.bind(on_key_down=_on_keyboard_down)



        self.btn1 = Button(\
        text='Исполнитель',
        background_normal = "btnpic2.png",
        background_down = "btnpic1.png",
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .5},)
        self.btn1.bind(state=typing_process)
        
        self.btn2 = Button(\
        text='Название',
        background_normal = "btnpic2.png",
        background_down = "btnpic1.png",
        # background_disabled_normal ="background.png",
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .25},)
        self.btn2.bind(state=typing_process)

        self.layout.add_widget(self.widget)
        self.layout.add_widget(self.btn1)
        self.layout.add_widget(self.btn2)   
        

     
        
        

KivyApp().run()

