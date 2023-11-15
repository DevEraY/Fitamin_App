navigation_helper = '''
ScreenManager:
    MainScreen:
        name: 'home'
    ProfileScreen:
        name: 'profile'

    EditProfileScreen:
        name: 'editProfile'    

<MainScreen>:
    MDScreen:

        MDScrollView:  # Add this MDScrollView
            pos_hint: {"center_x": 0.5, "center_y" : 0.37}
            MDList:

                id: container
                
                
        MDFloatingActionButton:
            icon: "calculator"
            pos_hint: {"center_x": 0.5}
            on_release: app.do_this()
        
        
        MDFloatingActionButton:
            icon: "android"
            pos_hint: {"center_x": 0.8}
            on_release: app.do_anotherthing()  
            
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: 'Demo Application'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                            elevation: 5
                        Widget:

            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "8dp"

                    Image:
                        id: avatar
                        size_hint: (1,1)
                        source: "fruit.jpg"

                    MDLabel:
                        text: "Fitamin App"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "şimdilik boş dursun"
                        size_hint_y: None
                        font_style: "Caption"
                        height: self.texture_size[1]

                    ScrollView:
                        DrawerList:
                            id: md_list
                            MDList:
                                OneLineIconListItem:
                                    text: "Profile"
                                    on_release: app.change_screen("profile")
                                    IconLeftWidget:
                                        icon: "account"
                                OneLineIconListItem:
                                    text: "Upload"
                                    IconLeftWidget:
                                        icon: "upload"
                                OneLineIconListItem:
                                    text: "Logout"
                                    IconLeftWidget:
                                        icon: "logout"
    

<ProfileScreen>:
    name: 'profile_screen'
    MDScreen:
        MDLabel:
            id: isim
            text: ''
            halign: 'center'
            font_style: 'H5'
            pos_hint: {'center_x': 0.5, 'center_y': 0.80}


        MDLabel:
            id: age
            text: 'Yaş: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.70}    

        MDLabel:
            id: height
            text: 'Height: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.60}

        MDLabel:
            id: weight
            text: 'Kilo: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}    



        MDLabel:
            id: gender
            text: 'Cinsiyet: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.40}    

        MDLabel:
            id: BMI
            text: 'BMI: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.30}
             
        MDLabel:
            id: Activity
            text: 'Aktiflik: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.20}
            
        MDLabel:
            id: Pregnancy
            text: 'Hamilelik durumu: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.10}      


        MDRaisedButton:
            text: 'Edit Profile'
            size_hint: None, None
            size: '200dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_release: root.manager.current = 'editProfile'
            
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: 'Demo Application'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                            elevation: 5
                        Widget:

            MDNavigationDrawer:
                id: nav_drawer
                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "8dp"

                    Image:
                        id: avatar
                        size_hint: (1,1)
                        source: "fruit.jpg"

                    MDLabel:
                        text: "Attreya"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "attreya01@gmail.com"
                        size_hint_y: None
                        font_style: "Caption"
                        height: self.texture_size[1]

                    ScrollView:
                        DrawerList:
                            id: md_list
                            MDList:
                                OneLineIconListItem:
                                    text: "Profile"
                                    on_release: app.change_screen("profile")
                                    IconLeftWidget:
                                        icon: "python-language"
                                OneLineIconListItem:
                                    text: "Upload"
                                    IconLeftWidget:
                                        icon: "upload"
                                OneLineIconListItem:
                                    text: "Logout"
                                    IconLeftWidget:
                                        icon: "logout"    

<EditProfileScreen>:
    name: 'edit_profile_screen'
    MDScreen:
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
            id: edited_weight
            hint_text: "Enter new weight"
            size_hint: None, None
            size: '300dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.35}



        MDRaisedButton:
            text: 'Save'
            size_hint: None, None
            size: '200dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_release: root.save_edited_profile()


        Spinner:
            id: gender_secme
            text: "Cinsiyet"
            values: ["Erkek", "Kadın"]
            size_hint: None, None
            size: 100, 44
            pos_hint: {'center_x': 0.36, 'center_y': 0.25}

            on_text: app.root.get_screen('editProfile').gender_belirleme(gender_secme.text)

        Spinner:
            id: pregnancy_situation
            text: "Hamilelik Durumu"
            values: ["I am not pregnant or lactating", "I am pregnant", "I am lactating"]
            size_hint: None, None
            size: 150, 44
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            disabled: True
            on_text: root.pregnancy_belirleme(pregnancy_situation.text)
            
        Spinner:
            id: aktiflik_secme
            text: "Aktiflik Seviyesi"
            values: ["Sedanter", "Haftada 1-3 gün hafif egzersiz", "Haftada 3-5 gün hafif-orta seviye egzersiz", "Her gün orta seviye egzersiz ya da haftada 3-4 gün ağır egzersiz", "Haftada 5-7 gün ağır egzersiz" ]
            size_hint: None, None
            size: 500, 44
            pos_hint: {'center_x': 0.55, 'center_y': 0.18}

            on_text: app.root.get_screen('editProfile').activity_level_belirleme(aktiflik_secme.text)        

'''