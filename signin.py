import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
kivy.require("1.10.1")



class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(SigninWindow, self).__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == '' or passw == '':
            info.text = '[color=#FE00EE]username and/ or password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = ('[color=#1AFE00]Logged in! You are ready to Party:d[/color]')
            else:
                info.text = '[color=#FE00EE]invalid username and/ or password[/color]'


class SigninApp(App):
    def build(self):
        return SigninWindow()



if __name__=="__main__":
    sa = SigninApp()
    sa.run()

