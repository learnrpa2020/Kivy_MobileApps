import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image,AsyncImage
from kivy.core.window import Window

Window.clearcolor=(1,1,1,1)
Window.size=(360,600)

class MobileScreen(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs,orientation='horizontal',spacing=10,padding=40)
		self.add_widget(Image(source='aws.png'))
		self.add_widget(Button(text='Cancel',size_hint=(None,None),width=100,height=50,pos_hint={'center_x':0.5}))
		self.add_widget(Button(text='OK',size_hint=(None,None),width=100,height=50,pos_hint={'center_x':0.5}))


class MyApp(App):
	def build(self):
		return MobileScreen()


MyApp().run()