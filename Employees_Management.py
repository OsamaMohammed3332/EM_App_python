from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
# import mysql.connector as sql

Window.size = (400, 600)
Window.clearcolor = (100 / 255.0, 0, 2, 1)


class Eapp(App):
    def build(self):
        self.title = "Employee App"
        layout = GridLayout(cols=1)
        image = Image(source='logo.png')
        label1 = Label(text='Employee', size_hint=(0.1, 0.3))
        label2 = Label(text='Add New Employee', size_hint=(0.1, 0.3))
        username = TextInput(hint_text='username', size_hint=(0.1, 0.3))
        work = TextInput(hint_text='work', size_hint=(0.1, 0.3))
        phone = TextInput(hint_text='phone', size_hint=(0.1, 0.3))
        country = TextInput(hint_text='country', size_hint=(0.1, 0.3))
        gender = TextInput(hint_text='gender', size_hint=(0.1, 0.3))
        submit = Button(text='Add Employee', size_hint=(0.1, 0.5))
        layout.add_widget(image)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(username)
        layout.add_widget(work)
        layout.add_widget(phone)
        layout.add_widget(country)
        layout.add_widget(gender)
        layout.add_widget(submit)
        return layout

# If you want to add database

    # def collect(self):
    #     un = self.username.text
    #     wo = self.work.text
    #     ph = self.phone.text
    #     co = self.country.text
    #     gd = self.gender.text
    #
    #     con = sql.connect(host='', user='', password='', database='')
    #     cur = con.cursor()
    #     query = 'Insert into teble_name (username,work,phone,country,gender) values (%s,%s,%s,%s,%s)'
    #     val = (un, wo, ph, co, gd)
    #     cur.execute(query, val)
    #     con.commit()
    #     con.close()

# Add this to button to submit info > on_press=self.collect


if __name__ == '__main__':
    Eapp().run()
