from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen

# Create a string containing the KV language code
kv_code = '''
ScreenManager:
    ProfileScreen:
        name : "Profile"
    EditProfileScreen:
        name : "editProfile"
    WelcomeScreen:
        name : 'welcome'
    MainScreen:
        name : 'home'
    
<WelcomeScreen>:
    
    MDTextField:
        id: text_field
        hint_text: 'Enter your text'
        helper_text: 'This is a text input'
        helper_text_mode: 'on_focus'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300

    MDRectangleFlatButton:
        text: 'Get Input'
        pos_hint: {"center_x": 0.9, "center_y": 0.5}
        on_release: root.show_data()
        
    MDRectangleFlatButton:
        text: 'home'
        pos_hint: {"center_x": 0.7, "center_y": 0.4}
        
        on_release: root.manager.current = "home"    

<MainScreen>:
    MDScrollView:
        MDList:
            id:container
    MDIconButton:
        icon:"android"
        pos_hint: {"center_x" :0.9, "center_y" : 0.99}
        on_release : root.print_wadafuq()    
    
    
    
        
<ProfileScreen>:
    name: 'profile_screen'

    MDLabel:
        id: isim
        text: 'wqe'
        halign: 'center'
        font_style: 'H5'
        pos_hint: {'center_x': 0.5, 'center_y': 0.80}
        
        
    MDLabel:
        id: age
        text: 'Yaş: '
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.70}    

    MDLabel:
        id: height_label
        text: 'Height: '
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.60}
        
    MDLabel:
        id: kilo
        text: 'Kilo: '
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.50}    
        
    
    
    MDLabel:
        id: gender
        text: 'Cinsiyet: '
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.40}    

    MDRaisedButton:
        text: 'Edit Profile'
        size_hint: None, None
        size: '200dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: root.manager.current = 'edit_profile_screen'

<EditProfileScreen>:
    name: 'edit_profile_screen'

    MDLabel:
        text: 'Edit Profile'
        halign: 'center'
        font_style: 'H5'
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}

    MDTextField:
        id: edited_isim
        hint_text: "Enter new name"
        size_hint: None, None
        size: '300dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        
        
    MDTextField:
        id: edited_age
        hint_text: "Enter new age"
        size_hint: None, None
        size: '300dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}    

    MDTextField:
        id: edited_height
        hint_text: "Enter new height"
        size_hint: None, None
        size: '300dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
    
    MDTextField:
        id: edited_
        hint_text: "Enter new height"
        size_hint: None, None
        size: '300dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
    
    MDTextField:
        id: edited_height
        hint_text: "Enter new height"
        size_hint: None, None
        size: '300dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}        

    MDRaisedButton:
        text: 'Save'
        size_hint: None, None
        size: '200dp', '40dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: app.save_edited_profile()
'''
class WelcomeScreen(Screen):
    def show_data(self):
        global KullaniciAdi
        KullaniciAdi = str(self.ids.text_field.text)
        print("KullaniciAdi:", KullaniciAdi)


class MainScreen(Screen):
    def print_wadafuq(self):
        print(total_proteins)




def calculation(c,p):
    global total_calories
    total_calories += c
    global total_proteins
    total_proteins += p



    return 0

class ProfileScreen(MDScreen):
    pass

class EditProfileScreen(MDScreen):
    pass

class ProfileApp(MDApp):
    def build(self):
        screen=Screen()
        self.root = Builder.load_string(kv_code)
        #Ana_Ekran = self.root.get_screen("home")
       # screen.add_widget(Ana_Ekran)
        screen.add_widget(self.root)
        return screen

    def save_edited_profile(self):
        new_name = self.root.get_screen('edit_profile_screen').ids.edited_isim.text
        new_age =  self.root.get_screen('edit_profile_screen').ids.edited_age.text
        new_height = self.root.get_screen('edit_profile_screen').ids.edited_height.text
        profile_screen = self.root.get_screen('profile_screen')
        profile_screen.ids.isim.text = new_name
        profile_screen.ids.age.text = f'Age: {new_age}'
        profile_screen.ids.height_label.text = f'Height: {new_height}'
        self.root.current = 'profile_screen'

if __name__ == '__main__':
    ProfileApp().run()
