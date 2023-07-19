import json
import time
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout




class ScrollViewMain(ScrollView):
    pass




def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)




# Активация кнопок
seconds = time.time()
result = time.gmtime(seconds)

def read(filename):
    with open(filename, 'r') as file:
        return json.load(file)
a = read('project.json')
my_value = int(a['v1'])
my_max = int(a['v2'])
lvl_text = a['v3']
time1 = a['t']
count_enabled1 = a["b1"]
count_enabled2 = a["b2"]
count_enabled3 = a["b3"]


if time1 != int(result.tm_mday):
    print('Work')
    value = {
        "v1": my_value,
        "v2": my_max,
        "v3": lvl_text,
        "b1": False,
        "b2": False,
        "b3": False,
        "t": result.tm_mday
    }
    write(value, 'project.json')





class NameTask(BoxLayout):

    def read(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    a = read('project.json')
    my_value = NumericProperty(int(a['v1']))
    my_max = NumericProperty(int(a['v2']))
    lvl_text = StringProperty((a['v3']))
    count_enabled1 = BooleanProperty(a["b1"])
    count_enabled2 = BooleanProperty(a["b2"])
    count_enabled3 = BooleanProperty(a["b3"])
    time1 = a['t']
    def on_button_click1(self):
        self.count_enabled1 = True
        count_enabled2_2 = self.count_enabled2
        count_enabled3_3 = self.count_enabled3
        time = self.time1
        self.my_value += 500
        print(self.my_value, self.my_max, self.lvl_text)
        if self.my_value >= self.my_max:
            self.my_value = 0
            self.lvl_text = str(int(self.lvl_text) + 1)
            if int(self.lvl_text) == 5:
                self.my_max += 500
            elif int(self.lvl_text) == 10:
                self.my_max += 1000
            elif int(self.lvl_text) == 15:
                self.my_max += 500
            elif int(self.lvl_text) == 20:
                self.my_max += 1000
            elif int(self.lvl_text) == 25:
                self.my_max += 500
            elif int(self.lvl_text) == 30:
                self.my_max += 1000
            elif int(self.lvl_text) == 35:
                self.my_max += 500
            elif int(self.lvl_text) == 40:
                self.my_max += 1000
            elif int(self.lvl_text) == 45:
                self.my_max += 500
            elif int(self.lvl_text) == 50:
                self.my_max += 1000
        value = {
            "v1": self.my_value,
            "v2": self.my_max,
            "v3": self.lvl_text,
            "b1": self.count_enabled1,
            "b2": count_enabled2_2,
            "b3": count_enabled3_3,
            "t": time
        }
        write(value, 'project.json')

    a = read('project.json')
    my_value = NumericProperty(int(a['v1']))
    my_max = NumericProperty(int(a['v2']))
    lvl_text = StringProperty((a['v3']))
    count_enabled1 = BooleanProperty(a["b1"])
    count_enabled2 = BooleanProperty(a["b2"])
    count_enabled3 = BooleanProperty(a["b3"])
    time1 = a['t']
    def on_button_click2(self):
        self.count_enabled2 = True
        count_enabled1_1 = self.count_enabled1
        count_enabled3_3 = self.count_enabled3
        time = self.time1
        self.my_value += 500
        print(self.my_value, self.my_max, self.lvl_text)
        if self.my_value >= self.my_max:
            self.my_value = 0
            self.lvl_text = str(int(self.lvl_text) + 1)
            if int(self.lvl_text) == 5:
                self.my_max += 500
            elif int(self.lvl_text) == 10:
                self.my_max += 1000
            elif int(self.lvl_text) == 15:
                self.my_max += 500
            elif int(self.lvl_text) == 20:
                self.my_max += 1000
            elif int(self.lvl_text) == 25:
                self.my_max += 500
            elif int(self.lvl_text) == 30:
                self.my_max += 1000
            elif int(self.lvl_text) == 35:
                self.my_max += 500
            elif int(self.lvl_text) == 40:
                self.my_max += 1000
            elif int(self.lvl_text) == 45:
                self.my_max += 500
            elif int(self.lvl_text) == 50:
                self.my_max += 1000
        value = {
            "v1": self.my_value,
            "v2": self.my_max,
            "v3": self.lvl_text,
            "b1": count_enabled1_1,
            "b2": self.count_enabled2,
            "b3": count_enabled3_3,
            "t": time
        }
        write(value, 'project.json')

    a = read('project.json')
    my_value = NumericProperty(int(a['v1']))
    my_max = NumericProperty(int(a['v2']))
    lvl_text = StringProperty((a['v3']))
    count_enabled1 = BooleanProperty(a["b1"])
    count_enabled2 = BooleanProperty(a["b2"])
    count_enabled3 = BooleanProperty(a["b3"])
    time1 = a['t']

    def on_button_click3(self):
        self.count_enabled3 = True
        count_enabled1_1 = self.count_enabled1
        count_enabled2_2 = self.count_enabled2
        time = self.time1
        self.my_value += 500
        print(self.my_value, self.my_max, self.lvl_text)
        if self.my_value >= self.my_max:
            self.my_value = 0
            self.lvl_text = str(int(self.lvl_text) + 1)
            if int(self.lvl_text) == 5:
                self.my_max += 500
            elif int(self.lvl_text) == 10:
                self.my_max += 1000
            elif int(self.lvl_text) == 15:
                self.my_max += 500
            elif int(self.lvl_text) == 20:
                self.my_max += 1000
            elif int(self.lvl_text) == 25:
                self.my_max += 500
            elif int(self.lvl_text) == 30:
                self.my_max += 1000
            elif int(self.lvl_text) == 35:
                self.my_max += 500
            elif int(self.lvl_text) == 40:
                self.my_max += 1000
            elif int(self.lvl_text) == 45:
                self.my_max += 500
            elif int(self.lvl_text) == 50:
                self.my_max += 1000
        value = {
            "v1": self.my_value,
            "v2": self.my_max,
            "v3": self.lvl_text,
            "b1": count_enabled1_1,
            "b2": count_enabled2_2,
            "b3": self.count_enabled3,
            "t": time
        }
        write(value, 'project.json')





















#schedule.every().day.at('20:15').do(unlocking)

#a = NameTask()
#schedule.every().day.at('19:48').do()
#schedule.every().day.at('19:48').do(uncloking)































class StatusLayout(BoxLayout):
    my_intelligence = StringProperty('1')
    my_agility = StringProperty('1')
    my_perception = StringProperty('1')
    my_stamina = StringProperty('1')
    my_strength = StringProperty('1')





class BigGridLayout(GridLayout):
    pass

class BigBoxLayout(BoxLayout):
    pass

class NameBox(BoxLayout):
    my_max = NumericProperty(1000)
    my_value = NumericProperty(500)

class Task(BoxLayout):
    def on_button_click(self):
        self.my_value += 500






class TaskBoxLayout(BoxLayout):
    pass

class StatisticsBox(BoxLayout):
    pass



class TheLabApp(App):
    pass

TheLabApp().run()