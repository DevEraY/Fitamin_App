#:import CircularProgressBar CircularProgressBar
navigation_helper = '''
ScreenManager:
    WelcomeScreen:
        name: 'welcome'
    CalculatorScreen:
        name: 'calculator'
    ProfileScreen:
        name: 'profile'

    EditProfileScreen:
        name: 'editProfile'
        
    AboutScreen:
        name: 'about'        


<WelcomeScreen>:
    MDTextField:
        id: welcome_screen_user_name_entry
        hint_text: 'Enter your name please'
        helper_text: 'You can change it from edit profile screen'
        helper_text_mode: 'on_focus'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: None
        width: 300

    MDRectangleFlatButton:
        text: 'Get Input'
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: root.welcome_screen_enter()
        
       




<CalculatorScreen>:
    name : 'calculator'
    MDScreen:
        CircularProgressBar:
            id: progressbar # This is the ID you assign to your CircularProgressBar
            pos_hint: {'center_x': 0.04, 'center_y': 0.7}
            thickness: 5
            cap_style: 'round'
            progress_colour: (1, 0, 0, 1)
            background_colour: (0.26, 0.26, 0.26, 1)
            max: 100
            min: 0
            widget_size: 50
            
            
            
        
            
            
        MDScrollView:  # Add this MDScrollView
            pos_hint: {"center_x": 0.5, "center_y" : 0.37}
            BoxLayout:  # Container for MDList and CircularProgressBar
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height  # Adjust the height dynamically based on content
                    
                
                MDList:
    
                    id: container
                    
                CircularProgressBar:
                    pos_hint: {'center_x': 0.1, 'center_y': 0.8}
                    thickness: 15
                    cap_style: 'round'
                    progress_colour: (1, 0, 0, 1)
                    background_colour: (0.26, 0.26, 0.26, 1)
                    max: 100
                    min: 0
                    widget_size: 200    
        MDFloatingActionButton:
            icon: "food-apple"
            pos_hint: {"center_x": 0.1, "center_y": 0.15}
            on_release: app.calculate_remaining_intake_pop_up()
            
            
            
        MDFloatingActionButton:
            icon: "basket"
            pos_hint: {"center_x": 0.5,"center_y": 0.15}
            on_release: app.show_bucket_popup()      
            
        
          
        
        MDFloatingActionButton:
            icon: "nutrition"
            pos_hint: {"center_x": 0.9,"center_y": 0.15}
            on_release: app.calculate_total_nutrients_consumed_pop_up()  
            
            
        # MDFloatingActionButton:
        #     icon: "plus-outline"
        #     pos_hint: {"center_x": 0.3}
        #     on_release: app.add_new_food() 
            
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: 'Fitamin App'
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
                        size_hint: (0.5,0.5)
                        source: "FitaminAppIcon.jpg"

                    MDLabel:
                        text: "Fitamin App"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Have a healthy diet, live a healthy life"
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
                                    text: "Calculate"
                                    on_release: app.change_screen("calculator")
                                    IconLeftWidget:
                                        icon: "calculator"
                                OneLineIconListItem:
                                    text: "About the Fitamin App "
                                    on_release: app.change_screen("about") 
                                    IconLeftWidget:
                                        icon: "information-outline"
    

<ProfileScreen>:
    name: 'profile_screen'
    MDScreen:
        MDLabel:
            id: isim
            text: ''
            halign: 'center'
            font_style: 'H3'
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}


        MDLabel:
            id: age
            text: 'Yaş: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.75}    

        MDLabel:
            id: height
            text: 'Height: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.70}

        MDLabel:
            id: weight
            text: 'Kilo: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.60}    



        MDLabel:
            id: gender
            text: 'Cinsiyet: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}    

        MDLabel:
            id: BMI
            text: 'BMI: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.40}
             
        MDLabel:
            id: Activity
            text: 'Aktiflik: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.30}
            
        MDLabel:
            id: Pregnancy
            text: 'Hamilelik durumu: '
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.20}      


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
                            title: 'Fitamin App'
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
                        size_hint: (0.5,0.5)
                        source: "FitaminAppIcon.jpg"

                    MDLabel:
                        text: "Fitamin App"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Have a healthy diet, live a healthy life"
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
                                    text: "Hesapla"
                                    on_release: app.change_screen("calculator")
                                    IconLeftWidget:
                                        icon: "calculator"
                                OneLineIconListItem:
                                    text: "About the Fitamin App"
                                    on_release: app.change_screen("about")
                                    IconLeftWidget:
                                        icon: "information-outline"    

<EditProfileScreen>:
    name: 'edit_profile_screen'
    MDScreen:
        MDLabel:
            text: 'Edit Profile'
            halign: 'center'
            font_style: 'H5'
            pos_hint: {'center_x': 0.5, 'center_y': 0.90}

        MDTextField:
            id: edited_isim
            hint_text: "Enter new name"
            size_hint: None, None
            size: '300dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.80}


        MDTextField:
            id: edited_age
            hint_text: "Enter new age"
            size_hint: None, None
            size: '300dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.70}    

        MDTextField:
            id: edited_height
            hint_text: "Enter new height"
            size_hint: None, None
            size: '300dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.60}

        MDTextField:
            id: edited_weight
            hint_text: "Enter new weight"
            size_hint: None, None
            size: '300dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}



        MDRaisedButton:
            text: 'Save'
            size_hint: None, None
            size: '200dp', '40dp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            on_release: root.save_edited_profile()


        Spinner:
            id: gender_secme
            text: "Cinsiyet"
            values: ["Male", "Female"]
            size_hint: None, None
            size: 100, 44
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}

            on_text: app.root.get_screen('editProfile').gender_belirleme(gender_secme.text)

        Spinner:
            id: pregnancy_situation
            text: "Hamilelik Durumu"
            values: ["I am not pregnant or lactating", "I am pregnant", "I am lactating"]
            size_hint: None, None
            size: 150, 44
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            disabled: True
            on_text: root.pregnancy_belirleme(pregnancy_situation.text)
            
        Spinner:
            id: aktiflik_secme
            text: "Aktiflik Seviyesi"
            values: ["Sedanter", "1-3 times weekly light exercise", "3-5 times weekly exercise", "Exercise everyday or 3-5 times weekly instense exercise", "5-7 times weekly intense exercise" ]
            size_hint: None, None
            size: 500, 44
            pos_hint: {'center_x': 0.50, 'center_y': 0.20}

            on_text: app.root.get_screen('editProfile').activity_level_belirleme(aktiflik_secme.text)        


<AboutScreen>
    name: 'about'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDTopAppBar:
                            title: 'Fitamin App'
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
                        size_hint: (0.5,0.5)
                        source: "FitaminAppIcon.jpg"

                    MDLabel:
                        text: "Fitamin App"
                        font_style: "Subtitle1"
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: "Have a healthy diet, live a healthy life"
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
                                    text: "Hesapla"
                                    on_release: app.change_screen("calculator")
                                    IconLeftWidget:
                                        icon: "calculator"
                                OneLineIconListItem:
                                    text: "About the Fitamin App"
                                    on_release: app.change_screen("about")
                                    IconLeftWidget:
                                        icon: "information-outline"        
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            
            Label:
                text: "Hii, I am a 5th year medical student and this is a project that I built in my free time.\\n In the future I am planning to add new features with updates. \\nAlso, this is a free App and I will keep it free because many of us do not recognize how bad we eat. \\nMany of us probably exceed the daily recommended intake amounts and so diseases follow.\\n I hope I could help you a little bit :) ."
                font_size: '16sp'
                halign: 'center'
    
            Label:
                text: "If you have any suggestions, feel free to mail me\\nfitaminapp@gmail.com"
                font_size: '16sp'
                halign: 'center'

'''