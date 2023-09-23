import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Создаем виджет Label
        self.label = Label(text='Привет, мир!')

        # Создаем виджет TextInput
        self.text_input = TextInput(text='Введите текст')

        # Создаем кнопку "Отправить"
        self.button = Button(text='Отправить')
        self.button.bind(on_press=self.on_button_press)

        # Создаем вертикальный контейнер для размещения виджетов
        vbox = BoxLayout(orientation='vertical')

        # Добавляем виджеты в контейнер
        vbox.add_widget(self.label)
        vbox.add_widget(self.text_input)
        vbox.add_widget(self.button)

        return vbox

    def on_button_press(self, instance):
        # Получаем текст из поля ввода
        text = self.text_input.text

        # Вызываем метод create() из g4f.ChatCompletion с переданным текстом
        result = g4f.ChatCompletion.create(text)

        # Обновляем текст в Label
        self.label.text = result

if __name__ == '__main__':
    MyApp().run()
