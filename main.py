from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import random
from kivy.uix.image import Image
from kivy.graphics import Color, Line, Rectangle
import re
from playsound import playsound

Builder.load_file('test.kv')
Window.size = (360, 800)


questions = ["Ты тупой?","Ты острый?", "Ты прямоугольный?",
            "Сколько в тебе углов?","Сколько сторон?", "Какой у тебя характер?",
            "Выбери цвет","Ты уравновешанный?", "Выбери неверный",
            "Треугольник - это...","Зачем ты это проходишь?", "Как ты относищься к этому Бульдозеру?",
            "Распишешь поминутно?","Добро и позитив?", "В жизни или в игре?",
            "Как с математикой?","Как с геометрией?", "Зачем живешь?",
            "Нравится?","Не нравится?"]

questionsImage = ["./photo/1.jpg","./photo/3.jpg", "./photo/4.jpg",
                "./photo/5.jpg","./photo/6.png","./photo/7.jpg",
                "./photo/8.jpg","./photo/9.jpg", "./photo/10.jpg",
                "./photo/11.jpg","./photo/12.jpg", "./photo/13.jpg",
                "./photo/14.png","./photo/15.png", "./photo/16.jpg",
                "./photo/17.png","./photo/18.png", "./photo/19.png",
                "./photo/20.jpg","./photo/21.png"]

variants_otvet = [["Да","Нет","Возможно","Не знаю"],#1
                ["Да","Нет","Возможно","Не знаю"],#2
                ["Да","Нет","Возможно","Не знаю"],#3
                ["1(Ты че палка?)","2(Что это?)","3","4(Это квадрат;/)"],#4
                ["1(Ты че палка?)","2(Что это?)","3","4(Это квадрат;/)"],#5
                ["Как пойдет","Ubunta","Лучше не знать","Классный"],#6
                ["Чёрный","Белый","Жёлтый","Других не существует"],#7
                ["Да","Нет","Зачем ты спрашиваешь?","Я Саня"],#8
                ["Я НЕ треугольник","Я треугольник","Я не квадрат","Круг - это круг"],#9
                ["Треугольник","Квадрат","Круг","Прямоугольник"],#10
                ["Меня заставили","Меня заставили","Меня заставили","Меня заставили"],#11
                ["Не напоминай","Он не работает","Точнее работает","Но не у меня"],#12
                ["Да, каждого в тетрадке","Нет","Возможно","Не уверен"],#13
                ["Добро","Позитив","И то и другое","Нет"],#14
                ["В жизни","В игре","Что за вопрос?","Смотря кто спрашивает?"],#15
                ["2","3","4","5"],#16
                ["2","3","4","5"],#17
                ["Ради удовольствия","Ради мучений","Ради создания apk","Не живу"],#18
                ["Да","Нет","Частично","Так себе"],#19
                ["Да","Нет","Частично","Так себе"],]#20

summ = 0

class PongPaddle(Widget):
    pass
class TestWidget(Widget):
    def on_press(self,string):     
        global summ
        if(len(questions) != 5):
            playsound("audio_file.mp3")
            i = random.randrange(0,len(questions),1)
            img.source = (questionsImage[i])
            arrayOtvet = variants_otvet[i]
            self.ids.input.text = questions[i]
            questionsImage.remove(questionsImage[i])
            questions.remove(questions[i])
            summ = summ + int(string)
            variants_otvet.remove(variants_otvet[i])
            self.ids.button1.text = arrayOtvet[0]
            self.ids.button2.text = arrayOtvet[1]
            self.ids.button3.text = arrayOtvet[2]
            self.ids.button4.text = arrayOtvet[3]


            print(summ)
        else:
            if(summ > 0 and summ < 15):
                self.ids.button1.text = ""
                self.ids.button2.text = ""
                self.ids.button3.text = ""
                self.ids.button4.text = ""
                self.ids.input.text = "Ты тупой"
                img.source = (r"./photo/22.jpg")
            elif(summ >= 15 and summ < 30):
                self.ids.button1.text = ""
                self.ids.button2.text = ""
                self.ids.button3.text = ""
                self.ids.button4.text = ""
                self.ids.input.text = "Ты острый"
                img.source = (r"./photo/21.png")
            elif(summ >= 30 and summ < 45):
                self.ids.button1.text = ""
                self.ids.button2.text = ""
                self.ids.button3.text = ""
                self.ids.button4.text = ""
                self.ids.input.text = "Ты равнобедренный"
                img.source = (r"./photo/23.png")
            elif(summ >= 45 and summ <= 60):
                self.ids.button1.text = ""
                self.ids.button2.text = ""
                self.ids.button3.text = ""
                self.ids.button4.text = ""
                self.ids.input.text = "Ты равносторонний"
                img.source = (r"./photo/24.png")
        

class TestApp(App):
    def build(self):
        global img 
        a = TestWidget()
        img = Image(source = r".\photo\2.jpg", pos=(80, 600), size= (200, 200))
        a.add_widget(img)
        return a

if __name__ == "__main__":
    TestApp().run()