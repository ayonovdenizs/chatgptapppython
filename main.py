print("Starting app...")
print('Don`t close this console window...')
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
import g4f
import sqlite3
from updater import check_version

class chatgptapp(MDApp):
    def build(self, *args):
        # Create MDLabel widget
        self.toolbar = MDTopAppBar(title='Серена ассистент')
        self.toolbar.right_action_items = [
            ['delete', lambda x: self.clear_db(x),
             'download_box', lambda x: self.update(x)]
        ]
        self.message_box = MDList()
        self.conn = sqlite3.connect('messages.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS message (msg TEXT)')
        self.conn.commit()
        self.version = "1.0.0_beta"
        self.need_update = check_version(self.version)
        self.label = MDLabel(text=f'Добро пожаловать в ChatGPT App by ayonovdenizs! Версия: {self.version}')
        self.toolbar.pos_hint = {'top': 1}

        # Create MDTextField widget
        self.text_input = MDTextField(hint_text='Написать Серене')

        # Create MDFlatButton widget
        self.button = MDFlatButton(text='Отправить')
        self.button.bind(on_release=self.on_button_press)
        vbox = MDBoxLayout(orientation='vertical')

        # Add widgets to the layout
        vbox.add_widget(self.toolbar)
        vbox.add_widget(self.message_box)
        vbox.add_widget(self.label)
        vbox.add_widget(self.text_input)
        vbox.add_widget(self.button)

        return vbox

    def on_button_press(self, instance):
        # Get text from the input field
        text = self.text_input.text
        self.label.text = 'Генерация...'
        Clock.schedule_once(self.generate_chat_response, 0.1)
        self.message_box.add_widget(
            TwoLineListItem(
                text=text,
                secondary_text='Вы:'
            )
        )
        self.c.execute(
        """INSERT INTO message(msg) VALUES (:msg)""",
        {
          "msg": text
      },
  )
        self.conn.commit()
    
    def clear_db(self, instance):
        self.label.text = "Диалог очищен."
        self.message_box.clear_widgets()
        self.c.execute("""DELETE FROM `message`
""")
        self.conn.commit()
        self.c.execute('CREATE TABLE IF NOT EXISTS message (msg TEXT)')
        self.conn.commit()
    
    def exportdb(self, instance):
        pass

    def generate_chat_response(self, instance):
        self.c.execute("SELECT * FROM message")
        for self.msg in self.c.fetchall():
            self.msg_list = []
            self.msg_list.append(self.msg)
        req = None
        try:
            req = self.api.predict(
				self.user_message,	# str in 'parameter_28' Textbox component
				"You are an android assistant girl, your name is Serena and you speak Russian. Always answer in Russian.",	# str in 'Optional system prompt' Textbox component
				0.5,	# int | float (numeric value between 0.0 and 1.0)
				4096,	# int | float (numeric value between 0 and 4096)
				0.9,	# int | float (numeric value between 0.0 and 1)
				2,	# int | float (numeric value between 1.0 and 2.0)
				api_name="/chat")
            self.label.text = ''
            self.message_box.add_widget(
                    TwoLineListItem(
                        text=req,
                        secondary_text='Серена'
                    )
                )
        except Exception as e:
            self.label.text = ''
            self.message_box.add_widget(
                    TwoLineListItem(
                        text=str(e),
                        secondary_text='Серена не смогла выполнить запрос'
                    )
                )
        self.c.execute(
                """INSERT INTO message(msg) VALUES (:msg)""",
                {
                "msg": req
            },
        )
        self.conn.commit()

    def update(self, instance):
        pass

if __name__ == '__main__':
    chatgptapp().run()