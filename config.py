KV = """
ScreenManager:
    MenuScreen:
    NotifScreen:
    ProfileScreen:
    UploadScreen:
    SuccessAuthScreen:
    MyFilesScreen:
    
    
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Авторизироваться'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'О проекте'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'

<NotifScreen>:
    name: 'notif'
    BoxLayout:
        orientation: "vertical"
        size_hint: 0.28, 0.17
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        Image:
            source: './load.gif'
        MDLabel:
            text: root.data_label
            halign: 'center'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: "vertical"
        size_hint: 0.58, 0.2
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        TextInput:
            id: Login
            multiline: False
            hint_text: "Логин"
        TextInput:
            id: Password
            multiline: False
            hint_text: "Пароль"
            password: True
        Button:
            on_press: root.signin(); root.manager.current = 'notif'
            text: "Войти"
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    

<UploadScreen>:
    name: 'upload'
    Image:
        source: './load.gif'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

<SuccessAuthScreen>:
    name: 'main_auth'
    MDLabel:
        text: root.greetings
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Мои файлы'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'my_files'
    MDRectangleFlatButton:
        text: 'Выйти'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'profile'; root.clean_token()

<MyFilesScreen>:
    name: 'my_files'
    size_hint: (1, 1)
    MDLabel:
        text: 'Еще больше текста'
        pos_hint: {'center_x':0.8,'center_y':0.3}
    MDLabel:
        pos_hint: {'center_x':0.8,'center_y':0.2}
        text: 'Ну а теперь и вовсе много много текста'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'main_auth' 
"""