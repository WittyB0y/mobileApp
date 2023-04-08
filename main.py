from modules import *


LINK = 'http://127.0.0.1:8000/'

KV = KV

TOKEN = ''


def url_sign_in():
    """it uses closures instead of global variables"""
    urls = {
        'signin': f'{LINK}api/v1/files/',
        'get_token': f'{LINK}api/v1/auth/token/login/',
        'dataUser': f'{LINK}api/v1/auth/users/',
    }

    def wrapper(url_name):
        return urls.get(url_name)

    return wrapper


url_sign_in = url_sign_in()


class NotifScreen(Screen):
    data_label = StringProperty("Выполняется авторизация")

    @staticmethod
    def success(msg):
        NotifScreen.data_label = msg


class MyFilesScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class SuccessAuthScreen(Screen):
    greetings = StringProperty("Добро пожаловать!")

    def get_json(self):
        result = UrlRequest(url=url_sign_in('signin'), req_headers={'Authorization': f'Token {TOKEN}'},
                            on_success=lambda x, z: print(z))

    def clean_token(self):
        global TOKEN
        TOKEN = ''


class ProfileScreen(Screen):

    def signin(self):
        login = self.ids.Login.text
        password = self.ids.Password.text
        result = ProfileScreen.do_auth(login, password)
        self.ids['Login'].text = ''
        self.ids['Password'].text = ''
        self.validator(result, login)

    def validator(self, data, username):
        key = data.json()
        if data.status_code == 400:
            notif_screen = self.manager.get_screen('notif')
            notif_screen.data_label = 'Произошла ошибка при авторизации!'
            Clock.schedule_once(self.switch_screen, 1)
        elif data.status_code == 200:
            notif_screen = self.manager.get_screen('notif')
            notif_screen.data_label = 'Вы успешно авторизированы!'
            global TOKEN
            TOKEN = key['auth_token']
            window_auth = self.manager.get_screen('main_auth')
            window_auth.greetings = f'Привет, {username}!!!'
            Clock.schedule_once(self.switch_screen_success, 2)

    def switch_screen(self, dt):
        self.manager.current = 'profile'

    def switch_screen_success(self, dt):
        self.manager.current = 'main_auth'

    @staticmethod
    def do_auth(login, password):
        data = {
            'username': login,
            'password': password
        }
        return requests.post(url=url_sign_in('get_token'), data=data)

    @staticmethod
    def got_json(request, result):
        result = json.dumps(result)
        print(result)


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(NotifScreen(name='notif'))
sm.add_widget(SuccessAuthScreen(name='main_auth'))
sm.add_widget(MyFilesScreen(name='my_files'))


class MobileApp(MDApp):

    def build(self):
        screen = Builder.load_string(KV)
        return screen


if __name__ == '__main__':
    MobileApp().run()