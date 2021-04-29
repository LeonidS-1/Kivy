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

# btnclr = [ .35, .04, .76, 1]

allowed_letters = '1234567890qwertyuiopasdfghjklzxcvbnm'
big_letter_list = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'



class KivyApp(App, Widget):
    
    def build(self):
        self.theme = 'd'

        self.layout = FloatLayout()
        
        self.texture_install()
        #
        
        #
        
        #
        self.welcome_screen()
        #
        return self.layout
    def texture_install(self):
        self.btnpicdt1 = f'btnpic{self.theme}t1.png'
        self.btnpicdt2 = f'btnpic{self.theme}t2.png'
        self.backgrounddt = f'background{self.theme}t.png'
        def redraw(self, args):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

        self.widget = Widget()
        with self.widget.canvas:
            self.widget.bg_rect = Rectangle(source=self.backgrounddt, pos=self.pos, size=self.size)
        self.widget.bind(pos=redraw, size=redraw)
        self.layout.add_widget(self.widget)
        
    def callback(self, instance, value):
        def firsttimer( who):
            self.layout.clear_widgets()
            self.typing_screen()
        
        #instance.text \\ value - normal/down
        if value == 'normal' and instance.text == 'Начать':  
            
            self.layout.remove_widget(self.welcome_btn)
            self.layout.remove_widget(self.settings_btn)
            self.layout.remove_widget(self.settings_btn)
            self.layout.remove_widget(self.settings_btn1)
            self.layout.remove_widget(self.settings_btn2)

            self.animated_part_1 = Button(\
            background_normal = self.btnpicdt2,        
            background_down = self.btnpicdt2,
            size_hint = (.5, .25),            
            pos_hint = {'x': 0, 'y': .75},)

            self.animated_part_2 = Button(\
            background_normal = self.btnpicdt2,        
            background_down = self.btnpicdt2,
            size_hint = (.5, .25),            
            pos_hint = {'x': .5, 'y': .75},)

            self.settings_btn = Button(\
            background_normal = self.btnpicdt2,
            background_down = self.btnpicdt1,
            size_hint = (.75, .15),
            pos_hint = {'x': .125, 'y': .5},)
            self.layout.add_widget(self.settings_btn)

            self.settings_btn1 = Button(\
            background_normal = self.btnpicdt2,
            background_down = self.btnpicdt1,
            size_hint = (.75, .15),
            pos_hint = {'x': .125, 'y': .3},)
            self.layout.add_widget(self.settings_btn1)

            self.settings_btn2 = Button(\
            background_normal = self.btnpicdt2,
            background_down = self.btnpicdt1,
            size_hint = (.75, .15),
            pos_hint = {'x': .125, 'y': .1},)
            self.layout.add_widget(self.settings_btn2)


            self.layout.add_widget(self.animated_part_1)
            self.layout.add_widget(self.animated_part_2)
            Clock.schedule_once(firsttimer, .55)
            
            self.animate(self.animated_part_1)
            self.animate(self.animated_part_2)
            self.animate(self.settings_btn)
            self.animate(self.settings_btn1)
            self.animate(self.settings_btn2)
        if value == 'normal' and instance.text == 'Настройки':
            if self.theme == 'l':
                self.theme = 'd'
            else:
                self.theme = 'l'
            self.texture_install()
            self.welcome_screen()
            

    
    def animate(self, instance):
        
        if instance == self.animated_part_1:
            animation = Animation(pos_hint = {'x': 0, 'y': .75}, size_hint = (.5, .25), duration=.5)
            animation &= Animation(pos_hint = {'x': 0, 'y': .5}, size_hint = (1, .25), duration=.5)
        if instance == self.animated_part_2:
            animation = Animation(pos_hint = {'x': .5, 'y': .75}, size_hint = (.5, .25), duration=.5)
            animation &= Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .25), duration=.5)
        if  instance == self.settings_btn:
            animation = Animation(pos_hint = {'x': .125, 'y': .5}, duration=.5)
            animation &= Animation(pos_hint = {'x': .125, 'y': .15*(-1)}, duration=.5)
        if  instance == self.settings_btn1:
            animation = Animation(pos_hint = {'x': .125, 'y': .3}, duration=.5)
            animation &= Animation(pos_hint = {'x': .125, 'y': .35*(-1)}, duration=.5)
        if  instance == self.settings_btn2:
            animation = Animation(pos_hint = {'x': .125, 'y': .1}, duration=.5)
            animation &= Animation(pos_hint = {'x': .125, 'y': .55*(-1)}, duration=.5)
        

        try: 
            if instance == self.settings_btn_back:
                animation = Animation(pos_hint = {'x': .125, 'y': .15*(-1)}, duration=.5) 
                animation &= Animation(pos_hint = {'x': .125, 'y': .5}, duration=.5)
            if instance == self.settings_btn1_back: 
                animation = Animation(pos_hint = {'x': .125, 'y': .35*(-1)}, duration=.5)
                animation &= Animation(pos_hint = {'x': .125, 'y': .3}, duration=.5)   
            if  instance == self.settings_btn2_back:
                animation = Animation(pos_hint = {'x': .125, 'y': .55*(-1)}, duration=.5)
                animation &= Animation(pos_hint = {'x': .125, 'y': .1}, duration=.5)
                
        
            if instance == self.button_input_text_1:
                animation = Animation(pos_hint = {'x': 0, 'y': .5}, size_hint = (1, .25), duration=.5)
                animation &= Animation(pos_hint = {'x': .5, 'y': .75}, size_hint = (.5, .25), duration=.5)
            if instance == self.button_input_text_2:
                animation = Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .25), duration=.5)
                animation &= Animation(pos_hint = {'x': 0, 'y': .75}, size_hint = (.5, .25), duration=.5)
        except:
            pass
        animation.start(instance)

        
   
    def welcome_screen(self): 
        self.layout.clear_widgets() 
        self.layout.add_widget(self.widget)

        
        self.welcome_btn = Button(\
        text='Начать',
        #color = [.01, .46, .56, 1],
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .75},)
        self.welcome_btn.bind(state=self.callback)
        self.layout.add_widget(self.welcome_btn)

        self.settings_btn = Button(\
        text='Настройки',
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        size_hint = (.75, .15),
        pos_hint = {'x': .125, 'y': .5},)
        self.settings_btn.bind(state=self.callback)
        self.layout.add_widget(self.settings_btn)
    
        self.settings_btn1 = Button(\
        #text='Настройки',
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        size_hint = (.75, .15),
        pos_hint = {'x': .125, 'y': .3},)
        self.settings_btn1.bind(state=self.callback)
        self.layout.add_widget(self.settings_btn1)

        self.settings_btn2 = Button(\
        #text='Настройки',
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        size_hint = (.75, .15),
        pos_hint = {'x': .125, 'y': .1},)
        self.settings_btn2.bind(state=self.callback)
        self.layout.add_widget(self.settings_btn2)
        
    def typing_screen(self):       
        self.text1 = ''
        self.text2 = '' 
        self.type_process = False
        self.big_letter = False
        def typing_process_control(instance, value):
            if instance == self.button_input_text_1:                      
                self.type_process = 1
            elif instance == self.button_input_text_2:
                self.type_process = 2
        def _on_keyboard_down(keyboard, keycode, text, modifiers):
            
            if self.type_process == 1:
                if keycode[1] == 'backspace':
                    self.text1 = self.text1[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False
                elif keycode[1] == 'spacebar':
                    self.text1+=' ' 
                elif keycode[1] == 'shift':
                    self.big_letter = True
                else:
                    letter_check = 0
                    while letter_check != len(allowed_letters):
                        letter_check+=1
                        if f'{keycode[1]}' == allowed_letters[letter_check-1:letter_check]:
                            if self.big_letter == False:
                                self.text1+=f'{keycode[1]}'
                            else:                                
                                self.text1+=f'{big_letter_list[letter_check-1:letter_check]}'
                                self.big_letter = False
                            break
                
                if self.type_process != False:
                    self.layout.remove_widget(self.button_input_text_1)
                    self.button_input_text_1 = Button(\
                    text=f'{self.text1}',
                    background_normal = self.btnpicdt2,
                    background_down = self.btnpicdt1,
                    size_hint = (1, .25),
                    pos_hint = {'x': 0, 'y': .5},)
                    self.button_input_text_1.bind(state=typing_process_control)
                    self.layout.add_widget(self.button_input_text_1)
            elif self.type_process == 2:
                if keycode[1] == 'backspace':
                    self.text2 = self.text2[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False  
                elif keycode[1] == 'spacebar':
                    self.text2+=' ' 
                elif keycode[1] == 'shift':
                    self.big_letter = True        
                else:
                    letter_check = 0
                    while letter_check != len(allowed_letters):
                        letter_check+=1
                        if f'{keycode[1]}' == allowed_letters[letter_check-1:letter_check]:
                            if self.big_letter == False:
                                    self.text2+=f'{keycode[1]}'
                            else:                                
                                self.text2+=f'{big_letter_list[letter_check-1:letter_check]}'
                                self.big_letter = False
                            break
                
                
                if self.type_process != False:
                    self.layout.remove_widget(self.button_input_text_2)
                    self.button_input_text_2 = Button(\
                    text=f'{self.text2}',
                    background_normal = self.btnpicdt2,
                    background_down = self.btnpicdt1,
                    size_hint = (1, .25),
                    pos_hint = {'x': 0, 'y': .25},)
                    self.button_input_text_2.bind(state=typing_process_control)
                    self.layout.add_widget(self.button_input_text_2)   

            if self._keyboard.widget:
                pass
    


        def close_keyboard():
            self._keyboard.unbind(on_key_down=_on_keyboard_down)
            self._keyboard = None

        self._keyboard = Window.request_keyboard(close_keyboard, self, 'text')
        self._keyboard.bind(on_key_down=_on_keyboard_down)



        self.button_input_text_1 = Button(\
        text='Исполнитель',
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .5},)
        self.button_input_text_1.bind(state=typing_process_control)
        
        self.button_input_text_2 = Button(\
        text='Название',
        background_normal = self.btnpicdt2,
        background_down = self.btnpicdt1,
        # background_disabled_normal ="background.png",
        size_hint = (1, .25),
        pos_hint = {'x': 0, 'y': .25},)
        self.button_input_text_2.bind(state=typing_process_control)

        def secondtimer(who):
            self.welcome_screen() 

        self.swipe_count = ''
        
        def swipe_check(*args):
            if args[1] == 1:
                self.swipe_count = '1'
            if args[1] == 2:
                self.swipe_count += '2'
            if args[1] == 3:
                self.swipe_count += '3'
            if self.swipe_count =='123':
                self.type_process = False
                self._keyboard.unbind(on_key_down=_on_keyboard_down)


                self.settings_btn_back = self.settings_btn
                self.layout.remove_widget(self.settings_btn)
                self.layout.add_widget(self.settings_btn_back)
                self.animate(self.settings_btn_back)

                self.settings_btn1_back = self.settings_btn1
                self.layout.remove_widget(self.settings_btn1)
                self.layout.add_widget(self.settings_btn1_back)
                self.animate(self.settings_btn1_back)
            
                self.settings_btn2_back = self.settings_btn2
                self.layout.remove_widget(self.settings_btn2)
                self.layout.add_widget(self.settings_btn2_back)
                self.animate(self.settings_btn2_back)



                self.layout.remove_widget(self.button_input_text_1)
                self.button_input_text_1 = self.animated_part_1
                self.layout.add_widget(self.button_input_text_1)
                self.animate(self.button_input_text_1)

                self.layout.remove_widget(self.button_input_text_2)
                self.button_input_text_2 = self.animated_part_2
                self.layout.add_widget(self.button_input_text_2)
                self.animate(self.button_input_text_2)

                Clock.schedule_once(secondtimer, .55)
                
          
        self.slider_swipe = Slider(min=0,
        max=3,  
        step=1, 
        pos_hint={'y': .375}, 
        cursor_size = (0, 0), 
        background_width = 0)
        self.slider_swipe.bind(value=swipe_check)
        
        


        
        self.layout.add_widget(self.widget)
        self.layout.add_widget(self.slider_swipe)
        self.layout.add_widget(self.button_input_text_1)
        self.layout.add_widget(self.button_input_text_2)   
        

     
        
        

KivyApp().run()

