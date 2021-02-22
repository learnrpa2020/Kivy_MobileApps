import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyFirstApp(App):
	def build(self):
		return Label(text="Hello Monica")



MyFirstApp().run()