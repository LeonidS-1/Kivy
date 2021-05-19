import kivy
kivy.require('1.0.8')

import requests
from bs4 import BeautifulSoup

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.lang.builder import Builder

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

#2

class KivyApp(App, Widget):
    
    def build(self):
        self.theme = 'd'

        self.layout = FloatLayout()
        
        self.texture_install()
        #
        self.welcome_screen()
        #
        return self.layout

    def add(self, *instance):
        for inst in instance:
            self.layout.add_widget(inst)

    def remove(self, *instance):
        for inst in instance:
            self.layout.remove_widget(inst)

    def texture_install(self):
        self.btnpicdt1 = f'btnpic{self.theme}t1.png'
        self.btnpicdt2 = f'btnpic{self.theme}t2.png'
        self.backgrounddt = f'background{self.theme}t.png'

        def redraw(self, args):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

        self.widget = Widget()
        with self.widget.canvas:
            self.widget.bg_rect = Rectangle(
             source=self.backgrounddt, 
              pos=self.pos, 
               size=self.size)
        self.widget.bind(pos=redraw, size=redraw)
        self.add(self.widget)
        
    def callback(self, instance, value):
        def firsttimer(who):
            self.layout.clear_widgets()
            self.typing_screen()
        
        #instance.text \\ value - normal/down
        if value == 'normal' and instance.text == 'Начать':  
            
            self.remove(self.welcome_btn)

            self.animated_part_1 = Button(
             background_normal = self.btnpicdt2,        
              background_down = self.btnpicdt2,
               size_hint = (.5, .25),            
                pos_hint = {'x': 0, 'y': .75},)

            self.animated_part_2 = Button(
             background_normal = self.btnpicdt2,        
              background_down = self.btnpicdt2,
               size_hint = (.5, .25),            
                pos_hint = {'x': .5, 'y': .75},)

            self.settings_btn.text = ''
            self.settings_btn.background_down = self.btnpicdt2
            self.settings_btn.unbind(state=self.callback)

            self.settings_btn1.text = ''
            self.settings_btn1.background_down = self.btnpicdt2
            self.settings_btn1.unbind(state=self.callback)

            self.settings_btn2.text = ''
            self.settings_btn2.background_down = self.btnpicdt2
            self.settings_btn2.unbind(state=self.callback)


            self.add(self.animated_part_1, 
                      self.animated_part_2)

            Clock.schedule_once(firsttimer, .55)
            
            self.animate(self.animated_part_1, 
                          self.animated_part_2, 
                           self.settings_btn, 
                            self.settings_btn1, 
                             self.settings_btn2)
            
        if value == 'normal' and instance.text == 'Настройки':
            if self.theme == 'l':
                self.theme = 'd'
            else:
                self.theme = 'l'
            self.texture_install()
            self.welcome_screen()
        try:
            if  instance == self.animated_part_3 and value == 'normal':
                if self.part_text < len(self.song_text)-1:
                    self.part_text+=1
                else:
                    self.part_text = 0
                self.text_screen()
        except:
            pass
    def animate(self, *instance1):
        for instance in instance1:
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
            if instance == 1:
                animation = Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .5), duration=.5)
                animation.start(self.animated_part_3)
                break
            try:
                if instance == self.animated_part_3:
                    animation = Animation(pos_hint = {'x': 0, 'y': 0}, size_hint = (1, .75), duration=.5)
            except:
                pass
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
        
        self.welcome_btn = Button(
        #color = [.01, .46, .56, 1],
         text='Начать',       
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (1, .25),
             pos_hint = {'x': 0, 'y': .75},)
        self.welcome_btn.bind(state=self.callback)

        self.settings_btn = Button(
         text='Настройки',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (.75, .15),
             pos_hint = {'x': .125, 'y': .5},)
        self.settings_btn.bind(state=self.callback)
    
        self.settings_btn1 = Button(
         text='none1',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (.75, .15),
             pos_hint = {'x': .125, 'y': .3},)
        self.settings_btn1.bind(state=self.callback)

        self.settings_btn2 = Button(
         text='none2',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (.75, .15),
             pos_hint = {'x': .125, 'y': .1},)
        self.settings_btn2.bind(state=self.callback)

        self.add(self.widget, 
                  self.settings_btn2, 
                   self.settings_btn1, 
                    self.settings_btn,
                     self.welcome_btn)

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
            self._keyboard = Window.request_keyboard(close_keyboard, self, 'text')
            
            if self._keyboard.widget:
                pass
            self._keyboard.bind(on_key_down=_on_keyboard_down)
        def _on_keyboard_down(keyboard, keycode, text, modifiers):
            
            if self.type_process == 1:
                if keycode[1] == 'backspace':
                    self.text1 = self.text1[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False
                    self.finding_song()
                    keyboard.release()
                elif keycode[1] == 'spacebar':
                    self.text1+=' ' 
                elif keycode[1] == 'shift':
                    self.big_letter = True
                else:
                    try:
                        letter_check = 0
                        while letter_check <= len(allowed_letters):                        
                            if f'{keycode[1]}' == allowed_letters[letter_check]:
                                if self.big_letter == False:
                                    self.text1+=f'{keycode[1]}'
                                else:                                
                                    self.text1+=f'{big_letter_list[letter_check]}'
                                    self.big_letter = False
                                break  
                            letter_check+=1 
                    except:
                        pass       
                self.button_input_text_1.text=f'{self.text1}'
                    
            elif self.type_process == 2:
                if keycode[1] == 'backspace':
                    self.text2 = self.text2[:-1]
                elif keycode[1] == 'enter':
                    self.type_process = False  
                    self.finding_song()
                    keyboard.release()
                elif keycode[1] == 'spacebar':
                    self.text2+=' ' 
                elif keycode[1] == 'shift':
                    self.big_letter = True        
                else:
                    try:
                        letter_check = 0
                        while letter_check <= len(allowed_letters):                        
                            if f'{keycode[1]}' == allowed_letters[letter_check]:
                                if self.big_letter == False:
                                        self.text2+=f'{keycode[1]}'
                                else:                                
                                    self.text2+=f'{big_letter_list[letter_check]}'
                                    self.big_letter = False
                                break  
                            letter_check+=1 
                    except:
                        pass             
                self.button_input_text_2.text=f'{self.text2}'
                    

            
    


        def close_keyboard():
            self._keyboard.unbind(on_key_down=_on_keyboard_down)
            
            #self._keyboard = None

        



        self.button_input_text_1 = Button(
         text='Исполнитель',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (1, .25),
             pos_hint = {'x': 0, 'y': .5},)
        self.button_input_text_1.bind(state=typing_process_control)
        
        self.button_input_text_2 = Button(
        # background_disabled_normal ="background.png",
         text='Название',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,        
            size_hint = (1, .25),
             pos_hint = {'x': 0, 'y': .25},)
        self.button_input_text_2.bind(state=typing_process_control)

        def secondtimer(who):
            self.welcome_screen() 

        self.swipe_count = ''
        
        def swipe_check(*args):
            if len(self.swipe_count) > 3:        
                self.swipe_count = ''

            if args[1] == 1: self.swipe_count += '1'
            if args[1] == 2: self.swipe_count += '2'
            if args[1] == 3: self.swipe_count += '3' 
            # if self.swipe_count =='321': 
            #     print(self.swipe_count)    
            if self.swipe_count =='123' and self.type_process == False:
                try:
                    self._keyboard.unbind(on_key_down=_on_keyboard_down)
                except:
                    pass
                self.settings_btn_back = self.settings_btn
                self.settings_btn1_back = self.settings_btn1
                self.settings_btn2_back = self.settings_btn2


                self.remove(self.settings_btn_back, 
                             self.settings_btn1_back, 
                              self.settings_btn2_back, 
                               self.button_input_text_1, 
                                self.button_input_text_2)
                
                
                self.button_input_text_1 = self.animated_part_1
                self.button_input_text_2 = self.animated_part_2


                self.animate(self.settings_btn_back, 
                              self.settings_btn1_back, 
                               self.settings_btn2_back, 
                                self.button_input_text_1,  
                                 self.button_input_text_2)

                self.add(self.settings_btn_back, 
                          self.settings_btn1_back, 
                            self.settings_btn2_back, 
                             self.button_input_text_1, 
                              self.button_input_text_2)

                Clock.schedule_once(secondtimer, .55)
            
               
          
        self.slider_swipe = Slider(
         min=0,
          max=3,  
           step=1, 
            pos_hint={'y': .375}, 
             cursor_size = (0, 0), 
              background_width = 0)
        self.slider_swipe.bind(value=swipe_check)
        

        self.add(self.widget, 
                  self.slider_swipe,
                   self.button_input_text_1, 
                    self.button_input_text_2)

    def finding_song(self):
        def firsttimer(who):
            self.text_screen()

        if self.text1  and self.text2:
            singer = ''
            for space_check in range(len(self.text1.split())):
                if space_check!=0:
                    singer+='_'
                singer+=self.text1.split()[space_check]
            name = ''
            for space_check in range(len(self.text2.split())):
                if space_check!=0:
                    name+='_'
                name+=self.text2.split()[space_check]
            singer = singer.lower()
            name = name.lower()
            response = requests.get(f'https://www.amalgama-lab.com/songs/{singer[0]}/{singer}/{name}.html')

            html_text = BeautifulSoup(response.text, 'lxml')


            self.original = html_text.find_all('div', class_='original')
            self.translate = html_text.find_all('div', class_='translate')
            self.song_text = ''
            for string in range(len(self.original)):
                self.song_text+= str(self.original[string].text).lstrip()
                self.song_text+= '\n'
                self.song_text+= str(self.translate[string].text).lstrip()
                self.song_text+= '\n'
            self.song_text = self.song_text.split('\n\n')
            self.song_text = list(filter(lambda x: x != '' and x != '\n' , self.song_text))
            self.part_text = 0
            self.animated_part_3 = Button(
             background_normal = self.btnpicdt2,        
              background_down = self.btnpicdt2,
               size_hint = (1, .5),            
                pos_hint = {'x': 0, 'y': .25},)
            Clock.schedule_once(firsttimer, 1)
            self.add(self.animated_part_3)
            self.animate(self.animated_part_3) 


    def text_screen(self):
        def firsttimer(who):
            self.text_screen()
            self.add(self.slider_swipe, 
                     self.button_input_text_1, 
                      self.button_input_text_2)
            

        self.remove(self.slider_swipe, 
                     self.button_input_text_1, 
                      self.button_input_text_2)
        self.swipe_count = ''
        def second_swipe_check(*args):
            
            if len(self.swipe_count) > 3:        
                self.swipe_count = ''
             
            if args[1] == 1: self.swipe_count = '1'
            if args[1] == 2: self.swipe_count += '2'
            if args[1] == 3: self.swipe_count += '3' 
            # if self.swipe_count =='321': 
            #     print(self.swipe_count)    
            if self.swipe_count =='123' :  
                self.animated_part_3.text = ''
                #print(self.swipe_count, 1)              
                self.animate(1)
                Clock.schedule_once(firsttimer, .5)

        
        self.slider_swipe_2 = Slider(
         min=0,
          max=3,  
           step=1, 
            pos_hint={'y': .375}, 
             cursor_size = (0, 0), 
              background_width = 0)
        self.add(self.slider_swipe_2)
        self.slider_swipe_2.bind(value=second_swipe_check)
        
        self.animated_part_3.text = self.song_text[self.part_text]
        
        self.animated_part_3.bind(state=self.callback)
        



                      



     
        
        

KivyApp().run()

