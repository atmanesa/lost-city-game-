from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (360, 640)

class WelcomeScreen(Screen): pass
class StageOneScreen(Screen):
    def check_answer(self):
        user_answer = self.ids.answer_input.text.strip().lower()
        if user_answer == "سين":
            self.manager.current = "stage_one_success"
        else:
            self.ids.feedback.text = "❌ خطأ... حاول مجددًا."
class StageOneSuccess(Screen): pass
class StageTwoScreen(Screen):
    def check_answer(self):
        user_answer = self.ids.answer_input2.text.strip().lower()
        if user_answer == "حفرة":
            self.manager.current = "stage_two_success"
        else:
            self.ids.feedback2.text = "❌ الإجابة غير صحيحة."
class StageTwoSuccess(Screen): pass

class GameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(StageOneScreen(name='stage_one'))
        sm.add_widget(StageOneSuccess(name='stage_one_success'))
        sm.add_widget(StageTwoScreen(name='stage_two'))
        sm.add_widget(StageTwoSuccess(name='stage_two_success'))
        return sm

if __name__ == '__main__':
    GameApp().run()
