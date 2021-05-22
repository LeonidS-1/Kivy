import kivy
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime


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
from kivy.uix.stacklayout import StackLayout

from kivy.uix.behaviors import ButtonBehavior

from kivy.graphics import Color, Canvas, Rectangle

con = sqlite3.connect('archive.db')
cur = con.cursor()

cur.execute(
'''CREATE TABLE IF NOT EXISTS archive(
        name TEXT,
        date TEXT,
        text_song );
''')

con.commit()




allowed_letters = '1234567890qwertyuiopasdfghjklzxcvbnm'
big_letter_list = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

class KivyApp(App, Widget):
    
    def build(self):
        self.theme = 'd'
        #self.title = 'Hello world'
        #self.icon = f'btnpic{self.theme}t1.png'
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

##############################################################################################################
    def texture_install(self):
        self.btnpicdt1 = fr'pictures\btnpic{self.theme}t1.png'
        self.btnpicdt2 = fr'pictures\btnpic{self.theme}t2.png'
        self.backgrounddt = fr'pictures\background{self.theme}t.png'

        def redraw(self, args):
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

        self.background = Widget()
        with self.background.canvas:
            self.background.bg_rect = Rectangle(
             source=self.backgrounddt, 
              pos=self.pos, 
               size=self.size)
        self.background.bind(pos=redraw, size=redraw)
        self.add(self.background)
        self.arch_back = False
        self.arch_change = False
        self.text_archive = Button(
         background_normal = self.btnpicdt2,        
          background_down = self.btnpicdt2,
           size_hint = (1, .75),            
            pos_hint = {'x': 0, 'y': 1},)
        self.arch_change_txt = False
##############################################################################################################        
    def callback(self, instance, value):
        def firsttimer(who):
            self.layout.clear_widgets()
            self.typing_screen()
        
        #instance.text \\ value - normal/down
        if value == 'normal' and instance.text == 'Поиск':  
            
            self.remove(self.welcome_btn, )
            try:
                self.add(self.settings_btn)
                self.remove(self.set_part_1, 
                      self.set_part_2)
            except: pass
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
        
        if value == 'normal' and instance.text == 'Архив':  
           
            self.archive() 
            
                
                          
        if value == 'normal' and instance.text == 'Настройки':
            
            self.set_part_1 = Button(
             text='Тема',
              background_normal = self.btnpicdt2,        
               background_down = self.btnpicdt1,
                size_hint = (.375, .15),
                 pos_hint = {'x': .125, 'y': .5},)
            self.set_part_1.bind(state=self.callback)

            self.set_part_2 = Button(
             text='Очистка',
              background_normal = self.btnpicdt2,        
               background_down = self.btnpicdt1,
                size_hint = (.375, .15),
                 pos_hint = {'x': .5, 'y': .5},)
            self.set_part_2.bind(state=self.callback)

            self.remove(self.settings_btn)
            self.add(self.set_part_1, 
                      self.set_part_2)

             
        try:
            if value == 'normal' and instance == self.set_part_2  :
                cur.execute('''DELETE FROM archive''')
                con.commit()
                
                self.welcome_screen()
            if value == 'normal' and instance == self.set_part_1  :
                if self.theme == 'l':
                    self.theme = 'd'
                else:
                    self.theme = 'l'
                self.texture_install()
                self.welcome_screen()
        except: pass
        try:
            if  instance == self.animated_part_3 and value == 'normal':
                if self.part_text < len(self.song_text)-1:
                    self.part_text+=1
                else:
                    self.part_text = 0
                self.text_screen()
                
        except: pass

##############################################################################################################
    def animate(self, *instance1):
        for instance in instance1:
            try:
                if instance == self.animated_part_1:
                    animation = Animation(pos_hint = {'x': 0, 'y': .75}, size_hint = (.5, .25), duration=.5)
                    animation &= Animation(pos_hint = {'x': 0, 'y': .5}, size_hint = (1, .25), duration=.5)            
                if instance == self.animated_part_2:
                    animation = Animation(pos_hint = {'x': .5, 'y': .75}, size_hint = (.5, .25), duration=.5)
                    animation &= Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .25), duration=.5)
            except: pass
            try:
                if instance == self.archive_layout_small:
                    animation = Animation(pos_hint = {'x': 0, 'y': 0}, duration=.5)
                if instance == self.slider_archive:
                    animation = Animation(pos_hint = {'x': 0, 'y': 0}, duration=.5)                
            except: pass
            if self.arch_change == True:
                if instance == self.archive_layout_small:
                    animation = Animation(pos_hint = {'x': 0, 'y': -1-0.1*len(self.spisok)}, duration=.5)
                if instance == self.slider_archive:
                    animation = Animation(pos_hint = {'x': 0, 'y': -1-0.1*len(self.spisok)}, duration=.5)
                if instance == self.text_archive:
                    animation = Animation(pos_hint = {'x': 0, 'y': 0}, duration=.5)
            if self.arch_change != True:     
                if instance == self.text_archive:
                    animation = Animation(pos_hint = {'x':0, 'y': -1}, duration=.5) 
                    
            if  self.arch_change_txt == True:     
                if instance == self.text_archive:
                    animation = Animation(pos_hint = {'x':0, 'y': 1}, duration=.5) 
            if self.arch_back == True:
                if instance == self.welcome_btn:
                    self.welcome_btn.pos_hint= {'x': 0, 'y': 1.75}
                    animation = Animation(pos_hint = {'x': 0, 'y': .75}, duration=.5)
                if  instance == self.settings_btn:
                    self.settings_btn.pos_hint = {'x': .125, 'y': 1.5}
                    animation = Animation(pos_hint = {'x': .125, 'y': .5}, duration=.5)
                if  instance == self.settings_btn1:
                    self.settings_btn1.pos_hint = {'x': .125, 'y': 1.3}
                    animation = Animation(pos_hint = {'x': .125, 'y': .3}, duration=.5)
                if  instance == self.settings_btn2:
                    self.settings_btn2.pos_hint = {'x': .125, 'y': 1.1}
                    animation = Animation(pos_hint = {'x': .125, 'y': .1}, duration=.5)
                if instance == self.archive_layout_small:
                    animation = Animation(pos_hint = {'x': 0, 'y': -1-0.1*len(self.spisok)}, duration=.5)
                if instance == self.slider_archive:
                    animation = Animation(pos_hint = {'x': 0, 'y': -1-0.1*len(self.spisok)}, duration=.5)  
            if self.arch_back != True:
                if instance == self.welcome_btn:
                    animation = Animation(pos_hint = {'x': 0, 'y': -.25}, duration=.5)
                if  instance == self.settings_btn:
                    animation = Animation(pos_hint = {'x': .125, 'y': .5}, duration=.5)
                    animation &= Animation(pos_hint = {'x': .125, 'y': -.4}, duration=.5)
                if  instance == self.settings_btn1:
                    animation = Animation(pos_hint = {'x': .125, 'y': .3}, duration=.5)
                    animation &= Animation(pos_hint = {'x': .125, 'y': -.6}, duration=.5)
                if  instance == self.settings_btn2:
                    animation = Animation(pos_hint = {'x': .125, 'y': .1}, duration=.5)
                    animation &= Animation(pos_hint = {'x': .125, 'y': -.8}, duration=.5)
            if instance == 1:
                animation = Animation(pos_hint = {'x': 0, 'y': .25}, size_hint = (1, .5), duration=.5)
                animation.start(self.animated_part_3)
                break
            try:
                if instance == self.animated_part_3:
                    animation = Animation(pos_hint = {'x': 0, 'y': 0}, size_hint = (1, .75), duration=.5)
                    
                    
            except: pass
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
            
    
##############################################################################################################    
    
    def archive(self):
        #self.text_archive.pos_hint = {'x':0, 'y': 1}   
                #self.welcome_screen()
        def swipe_check(*args):
            def run2(who):
                def run3(who):
                    self.arch_back = False
                    self.welcome_screen()

                self.animate(self.settings_btn, 
                        self.settings_btn1, 
                        self.settings_btn2,
                        self.welcome_btn,)
                Clock.schedule_once(run3, .55)
            if len(self.swipe_count) > 3:        
                self.swipe_count = ''
            
            if args[1] == 1: self.swipe_count = '1'
            if args[1] == 2: self.swipe_count += '2'
            if args[1] == 3: self.swipe_count += '3' 

            if self.swipe_count =='123' :
                self.arch_back = True
                self.animate( 
                        self.archive_layout_small, 
                        self.slider_archive
                        )
                Clock.schedule_once(run2, .55)

        def change_pos(*change_crd):
            
            self.plus_change = self.slider_archive.max - change_crd[1]//1
            for num_block in range(len(self.block_list)-int(self.plus_change)): 
                
                self.block_list[num_block].text = self.spisok[num_block+int(self.plus_change)]
        def text_link(button_name):
            self.text_archive.pos_hint = {'x':0, 'y': 1}
            def run2(who):
                self.arch_change = False
                self.archive_text(button_name)
            self.arch_change = True
            self.animate(self.archive_layout_small,
                          self.slider_archive, 
                           self.text_archive)
            
            try: self.add(self.text_archive)
            except: pass
            Clock.schedule_once(run2, .55)
            
        
        self.spisok = cur.execute('SELECT * FROM archive;').fetchall()   
        self.block_list = []
        self.plus_change = 0
        self.swipe_count = ''

        for num_block in range(len(self.spisok)):
                self.block_list.append(Button(text=f'{self.spisok[num_block][0]}\n{self.spisok[num_block][1]}', 
                background_normal = self.btnpicdt2, 
                 background_down = self.btnpicdt1,  
                  size_hint=(1, .1), 
                   on_press=text_link))
        self.archive_layout_main = BoxLayout(spacing=0, orientation='horizontal')
        self.archive_layout_small = StackLayout(pos_hint = {'x': 0, 'y': 1+0.1*len(self.spisok)}, size_hint=(5, 1), spacing=1)
        
        self.slider_archive = Slider(
         min=0,
          max=10,  
           step=1, 
            value = 11,
             orientation='vertical',               
              background_vertical = self.btnpicdt2, 
               cursor_image = self.btnpicdt1,
                cursor_size = (0, 0), pos_hint = {'x': 0, 'y': 1+0.1*len(self.spisok)},
                 background_width = 10)

        self.slider_swipe_archive = Slider(
         min=0,
          max=3,  
           step=1, 
            
             size_hint=(1, .092),
              cursor_size = (0, 0), 
               background_width = 0)


        
        self.slider_swipe_archive.bind(value=swipe_check)
        
        if len(self.spisok) >= 10:
            
            self.slider_archive.cursor_size = (15, 20)
            self.slider_archive.max = len(self.spisok) - 9
            self.slider_archive.value = len(self.spisok) - 9
            self.slider_archive.bind(value=change_pos)



        def run1(who): 
            #self.archive_layout_small.pos_hint = {}
            self.animate(self.archive_layout_small, self.slider_archive)
        
        #self.add(self.background)
        #
        self.add(self.archive_layout_main,)
        #
        try:
            self.archive_layout_main.add_widget(self.archive_layout_small)  
            self.archive_layout_main.add_widget(self.slider_archive)
        except: pass
        #
        self.archive_layout_small.add_widget(self.slider_swipe_archive)        
        for num_block in range(len(self.block_list)):        
            self.archive_layout_small.add_widget(self.block_list[num_block])
        self.animate(self.settings_btn, 
                        self.settings_btn1, 
                        self.settings_btn2,
                        self.welcome_btn, )
        self.settings_btn.text = ''
        self.settings_btn1.text = ''
        self.settings_btn2.text = ''
        self.welcome_btn.text = ''
        

        Clock.schedule_once(run1, .55)

##############################################################################################################
    def welcome_screen(self): 
        self.layout.clear_widgets() 
        
        self.welcome_btn = Button(
        #color = [.01, .46, .56, 1],
         text='Поиск',       
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
         text='Архив',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (.75, .15),
             pos_hint = {'x': .125, 'y': .3},)
        self.settings_btn1.bind(state=self.callback)

        self.settings_btn2 = Button(
         text='',
          background_normal = self.btnpicdt2,
           background_down = self.btnpicdt1,
            size_hint = (.75, .15),
             pos_hint = {'x': .125, 'y': .1},)
        self.settings_btn2.bind(state=self.callback)

        self.add(self.background, 
                  self.settings_btn2, 
                   self.settings_btn1, 
                    self.settings_btn,
                     self.welcome_btn)
        
        try:
            self.remove(self.animated_part_3)
        except:
            pass
               
##############################################################################################################
    def typing_screen(self):  
        try:
            self.remove(self.animated_part_3)
        except:
            pass     
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
        

        self.add(self.background, 
                  self.slider_swipe,
                   self.button_input_text_1, 
                    self.button_input_text_2)

##############################################################################################################
    def finding_song(self):
        def firsttimer(who):
            self.text_screen()
        
        if self.text1  and self.text2:
            self.singer = ''
            for space_check in range(len(self.text1.split())):
                if space_check!=0:
                    self.singer+='_'
                self.singer+=self.text1.split()[space_check]
            self.name1 = ''
            for space_check in range(len(self.text2.split())):
                if space_check!=0:
                    self.name1+='_'                
                self.name1+=self.text2.split()[space_check]
            self.singer = self.singer.lower()
            self.name1 = self.name1.lower()
            response = requests.get(f'https://www.amalgama-lab.com/songs/{self.singer[0]}/{self.singer}/{self.name1}.html')

            html_text = BeautifulSoup(response.text, 'lxml')


            self.original = html_text.find_all('div', class_='original')
            if self.original ==[]:
                self.layout.clear_widgets() 
                self.typing_screen()
            else:
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

                self.singer = self.singer.title().replace('_', ' ')
                self.name1 = self.name1.title().replace('_', ' ')
                execute_help = ''
                for i in range(len(self.song_text)):
                    execute_help+=self.song_text[i]
                    execute_help+='_1_'
                spisok_ch = cur.execute('SELECT * FROM archive;').fetchall() 
                for ch_arch in spisok_ch:
                    if ch_arch[0] == f'{self.name1} - {self.singer}':
                        break
                else:
                    time_now = datetime.now()
                    text_execute = (f'{self.name1} - {self.singer}', f'{time_now.hour}:{time_now.minute} - {time_now.date()}', execute_help)
                    cur.execute('INSERT INTO archive VALUES(?, ?, ?)', text_execute)
                    con.commit()
                self.song_text.append('')
                self.animated_part_3 = Button(
                 background_normal = self.btnpicdt2,        
                  background_down = self.btnpicdt2,
                   size_hint = (1, .5),            
                    pos_hint = {'x': 0, 'y': .25},)
                self.animated_part_3.text_size=(self.layout.width//2.5, None)
                Clock.schedule_once(firsttimer, 1)
                self.add(self.animated_part_3)
                self.animate(self.animated_part_3) 

##############################################################################################################    
    def text_screen(self):
        
        def firsttimer(who):
            
            self.text_screen()
            self.add(self.slider_swipe, 
                    self.button_input_text_1, 
                    self.button_input_text_2)
            self.remove(self.animated_part_3)
             
        
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
                self.animate(1)
                Clock.schedule_once(firsttimer, .5)

        
        self.slider_swipe_song_text = Slider(
         min=0,
          max=3,  
           step=1, 
            pos_hint={'y': .75}, 
             cursor_size = (0, 0), 
              background_width = 0)
        self.add(self.slider_swipe_song_text)
        self.slider_swipe_song_text.bind(value=second_swipe_check)
        self.animated_part_3.pos_hint = {'x': 0, 'y': 0}
        self.animated_part_3.size_hint = (1, .75)


        self.animated_part_3.text = f'{self.name1} - {self.singer}   [{self.part_text} / {len(self.song_text)-1}]\n\n\n' + \
                                    self.song_text[self.part_text] 



        self.animated_part_3.bind(state=self.callback)

##############################################################################################################  
    def archive_text(self, button_name):
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
                self.archive()
                self.animate(self.text_archive)
                
        
        self.slider_swipe_song_text_1 = Slider(
         min=0,
          max=3,  
           step=1, 
            pos_hint={'y': .75}, 
             cursor_size = (0, 0), 
              background_width = 0)
        self.add(self.slider_swipe_song_text_1)
        self.slider_swipe_song_text_1.bind(value=second_swipe_check)

        exex_hlp = button_name.text.split('\n')
        execution_help = f'SELECT * FROM archive WHERE name="{exex_hlp[0]}"'
        
        cur.execute(execution_help)
        helping = cur.fetchall()
        con.commit()
        def plus(who):
            if self.part_text < len(normal_text)-1 :
                self.part_text += 1
            else:
                self.part_text = 0
            self.text_archive.text = f'{helping[0][0]}   [{self.part_text} / {len(normal_text)-1}]\n\n\n' +\
                                         normal_text[self.part_text] 
        
        self.part_text = 0
                   
        self.text_archive.bind(on_press=plus)
        normal_text = helping[0][2].split('_1_')
        
        self.text_archive.text = f'{helping[0][0]}   [{self.part_text} / {len(normal_text)-1}]\n\n\n' +\
                                    normal_text[self.part_text]
        

     
        
        

KivyApp().run()

