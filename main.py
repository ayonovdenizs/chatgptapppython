from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout

class MyApp(MDApp):
    def build(self, *args):
        # Create MDLabel widget
        self.label = MDLabel(text='Привет, мир!')

        # Create MDTextField widget
        self.text_input = MDTextField(hint_text='Введите текст')

        # Create MDFlatButton widget
        self.button = MDFlatButton(text='Отправить')
        self.button.bind(on_release=self.on_button_press)

        # Create MDBoxLayout for vertical arrangement of widgets
        vbox = MDBoxLayout(orientation='vertical')

        # Add widgets to the layout
        vbox.add_widget(self.label)
        vbox.add_widget(self.text_input)
        vbox.add_widget(self.button)

        return vbox

    def on_button_press(self, instance):
        # Get text from the input field
        text = self.text_input.text
        self.label.text = text

if __name__ == '__main__':
    MyApp().run()
