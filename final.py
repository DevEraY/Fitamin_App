from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.clock import Clock
import time
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, ThreeLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.clock import Clock
import pandas as pd
from Fitamin import navigation_helper
from functools import partial
from user_profile_facts import user_profile_data
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.checkbox import CheckBox
from daily_recommended_intakes_for_micronutrients import *
from daily_recommended_intakes_for_vitamins import *
from daily_recommended_intakes_for_macronutrients import *
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFloatingActionButton
from kivy.core.window import Window
from circularprogressbardenemesi import CircularProgressBar
import json
import math
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton


class WelcomeScreen(Screen):
    def welcome_screen_enter(self):
        new_name = self.ids.welcome_screen_user_name_entry.text
        user_profile_data[0] = new_name
###################saving it to json file##############
        filename = "user_profile_data.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        # Directly update the first string variable
        data[0] = new_name

        with open(filename, 'w') as file:
            json.dump(data, file)
        ##############################################
        app = MDApp.get_running_app()
        app.root.current = 'calculator'

        return



class ProfileScreen(Screen):

    def update_profile_screen(self):
        filename = "user_profile_data.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        self.ids.isim.text = str(data[0])
        self.ids.age.text = str(data[3])
        self.ids.height.text = str(data[1])
        self.ids.weight.text = str(data[2])
        self.ids.gender.text = str(data[4])
        self.ids.BMI.text = str(data[9])
        #self.ids.Activity = data[6]
        #self.ids.Pregnancy = data[0]

    def on_pre_enter(self, *args):
        # Call the update_profile_screen method when the screen is about to be entered
        self.update_profile_screen()







class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = MDApp.get_running_app()
        self.foods = app.foods
        self.food_basket = app.food_basket
        self.recommended_intakes = app.recommended_intakes






class EditProfileScreen(Screen):
    new_recommended_intakes_full_list = {}

    def gender_belirleme (self, selected_option):
        profile_screen = self.manager.get_screen('profile')
        profile_screen_2 = self.manager.get_screen('editProfile')
        if selected_option == 'Kadın':
            self.ids.pregnancy_situation.disabled = False
        else:
            self.ids.pregnancy_situation.disabled = True
            profile_screen.ids.Pregnancy.text = "Hamilelik durumu: "
            user_profile_data[10] = ""
            profile_screen_2.ids.pregnancy_situation.text="Hamilelik Durumu"
        profile_screen.ids.gender.text = "Cinsiyet: " + selected_option
        user_profile_data[4] = selected_option



    def pregnancy_belirleme(self,situation):
        profile_screen = self.manager.get_screen('profile')
        profile_screen.ids.Pregnancy.text = "Hamilelik durumu: " + situation
        user_profile_data[10]=situation

    def activity_level_belirleme(self,selected_option):
        profile_screen = self.manager.get_screen('profile')
        profile_screen.ids.Activity.text = "Aktiflik: " + selected_option
        user_profile_data[6] = selected_option


    def save_edited_profile(self):
        app = MDApp.get_running_app()  # recommended_intake editlemek için

        new_name = self.ids.edited_isim.text
        new_age = int(self.ids.edited_age.text)
        new_height = self.ids.edited_height.text
        new_weight = self.ids.edited_weight.text


        profile_screen = self.manager.get_screen('profile')
        #
        # profile_screen.ids.isim.text = new_name
        # profile_screen.ids.age.text = f'Age: {new_age}'
        # profile_screen.ids.height.text = f'Height: {new_height}'
        # profile_screen.ids.weight.text = f'Weight: {new_weight}'
        new_gender = user_profile_data[4]
        pregnancy_situation = user_profile_data[10]
        
        #recommended_intakes editleme
        if new_gender == "Erkek" :
            if 1<=new_age<=3 :
                self.new_recommended_intakes_full_list.update(element_values_children_1_3_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_children_1_3_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_children_1_3_y)

            elif 4<=new_age<=8 :
                self.new_recommended_intakes_full_list.update(element_values_children_4_8_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_children_4_8_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_children_4_8_y)

            elif 9 <= new_age <= 13 :
                self.new_recommended_intakes_full_list.update(element_values_males_9_13_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_9_13_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_9_13_y)

            elif 14 <= new_age <= 18 :
                self.new_recommended_intakes_full_list.update(element_values_males_14_18_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_14_18_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_14_18_y)

            elif 19 <= new_age <= 30 :
                self.new_recommended_intakes_full_list.update(element_values_males_19_30_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_19_30_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_19_30_y)

            elif 31 <= new_age <= 50 :
                self.new_recommended_intakes_full_list.update(element_values_males_31_50_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_31_50_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_31_50_y)

            elif 51 <= new_age <= 70 :
                self.new_recommended_intakes_full_list.update(element_values_males_51_70_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_51_70_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_51_70_y)

            elif 71 <= new_age :
                self.new_recommended_intakes_full_list.update(element_values_males_gt_70_plus_y)
                self.new_recommended_intakes_full_list.update(nutrient_values_males_over_70_y_g)
                self.new_recommended_intakes_full_list.update(vitamin_values_males_gt_70_plus_y)


        elif new_gender =="Kadın" :



            if pregnancy_situation == "I am pregnant" :

                if 14 <= new_age <= 18 :
                    self.new_recommended_intakes_full_list.update(element_values_pregnancy_14_18_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_pregnancy_14_18_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_pregnancy_14_18_y)

                if 19<= new_age <= 30 :
                    self.new_recommended_intakes_full_list.update(element_values_pregnancy_19_30_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_pregnancy_19_30_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_pregnancy_19_30_y)

                if 31<= new_age <= 50 :
                    self.new_recommended_intakes_full_list.update(element_values_pregnancy_31_50_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_pregnancy_31_50_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_pregnancy_31_50_y)

            elif pregnancy_situation == "I am lactating" :
                if 14 <= new_age <= 18 :
                    self.new_recommended_intakes_full_list.update(element_values_lactation_14_18_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_lactation_14_18_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_lactation_14_18_y)

                if 19 <= new_age <= 30 :
                    self.new_recommended_intakes_full_list.update(element_values_lactation_19_30_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_lactation_19_30_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_lactation_19_30_y)

                if 31 <= new_age <= 50 :
                    self.new_recommended_intakes_full_list.update(element_values_lactation_31_50_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_lactation_31_50_y)
                    self.new_recommended_intakes_full_list.update(vitamin_values_lactation_31_50_y)


            elif pregnancy_situation == "I am not pregnant or lactating" :

                if 1 <= new_age <= 3 :
                    self.new_recommended_intakes_full_list.update(element_values_children_1_3_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_children_1_3_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_children_1_3_y)

                elif 4 <= new_age <= 8 :
                    self.new_recommended_intakes_full_list.update(element_values_children_4_8_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_children_4_8_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_children_4_8_y)

                elif 9 <= new_age <= 13 :
                    self.new_recommended_intakes_full_list.update(element_values_females_9_13_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_9_13_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_9_13_y)

                elif 14 <= new_age <= 18 :
                    self.new_recommended_intakes_full_list.update(element_values_females_14_18_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_14_18_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_14_18_y)

                elif 19 <= new_age <= 30 :
                    self.new_recommended_intakes_full_list.update(element_values_females_19_30_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_19_30_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_19_30_y)

                elif 31 <= new_age <= 50 :
                    self.new_recommended_intakes_full_list.update(element_values_females_31_50_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_31_50_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_31_50_y)

                elif 51 <= new_age <= 70 :
                    self.new_recommended_intakes_full_list.update(element_values_females_51_70_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_51_70_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_51_70_y)

                elif 71 <= new_age :
                    self.new_recommended_intakes_full_list.update(element_values_females_gt_70_plus_y)
                    self.new_recommended_intakes_full_list.update(nutrient_values_females_over_70_y_g)
                    self.new_recommended_intakes_full_list.update(vitamin_values_females_gt_70_plus_y)


        ##BMI da ekleyelim gelmişken
        BMI = int(new_weight) / ((int(new_height) / 100) ** 2)
        profile_screen.ids.BMI.text = f'BMI: {BMI}'


        #proteini updatele#
        self.new_recommended_intakes_full_list["Protein"] = 0.8 * int(new_weight)
        app.recommended_intakes = self.new_recommended_intakes_full_list

        # Basal Metabolism rate calculation according to Mifflin Equation {10.1093/ajcn/51.2.241}

        new_BasalMetabolismRate = 0

        if new_gender == "Erkek":
            new_BasalMetabolismRate = (9.99*int(new_weight))+(6.25*int(new_height))+5

        elif new_gender == "Kadın":
            new_BasalMetabolismRate = (9.99*int(new_weight))+(6.25*int(new_height))-161

        # yeni verileri belleğe alma
        user_profile_data[0] = new_name
        user_profile_data[1] = new_height
        user_profile_data[2] = new_weight
        user_profile_data[3] = new_age

        user_profile_data[5] = new_BasalMetabolismRate
        user_profile_data[9] = BMI

        filename = "user_profile_data.json"
        with open(filename, 'r') as file:
            data = json.load(file)

        # Directly update the first string variable
            data[0] = new_name
            data[1] = new_height
            data[2] = new_weight
            data[3] = new_age

            data[5] = new_BasalMetabolismRate
            data[9] = BMI

        with open(filename, 'w') as file:
            json.dump(data, file)
        ##############################################


        app.save_user_profile_data(user_profile_data)
        print(user_profile_data)
        self.manager.current = 'profile'

class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class RemainingIntake(BoxLayout):
    def __init__(self, remaining_nutrients, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Choose Input Type:')
        self.remaining_nutrients = remaining_nutrients

        for nutrient_info in self.remaining_nutrients:
            nutrient_label = Label(text=f"{nutrient_info[0]}: {nutrient_info[1]} {nutrient_info[2]}")
            self.add_widget(nutrient_label)


class ConsumedAmount(BoxLayout):
    def __init__(self, consumed_amount, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Choose Input Type:')
        self.consumed_amount = consumed_amount

        for nutrient_info in self.consumed_amount:
            nutrient_label = Label(text=f"{nutrient_info[0]}: {nutrient_info[1]} {nutrient_info[2]}")
            self.add_widget(nutrient_label)

class DualInput(BoxLayout):
    def __init__(self, food, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Choose Input Type:')

        if food.portion_name!="":
            hint_text = f'{food.portion_name} or grams'
        else:
            hint_text = 'grams'

        self.input_type = TextInput(hint_text=hint_text)
        self.add_widget(self.label)
        self.add_widget(self.input_type)


class AmountInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label_quantity = Label(text='Enter Quantity:')
        self.quantity_input = TextInput(hint_text='Quantity')
        self.label_grams = Label(text='Enter Grams:')
        self.grams_input = TextInput(hint_text='Grams')
        self.add_widget(self.label_quantity)
        self.add_widget(self.quantity_input)
        self.add_widget(self.label_grams)
        self.add_widget(self.grams_input)


class QuantityInput(BoxLayout):
    def __init__(self, food, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label_quantity = Label(text=f'Enter {food.portion_name} consumed')
        self.quantity_input = TextInput(hint_text=food.portion_name)
        self.add_widget(self.label_quantity)
        self.add_widget(self.quantity_input)



class GramsInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Enter Grams:')
        self.grams_input = TextInput(hint_text='Grams')
        self.add_widget(self.label)
        self.add_widget(self.grams_input)


# Define a class to represent a food item
class Food:
    def __init__(self, description):
        self.description = description
        self.nutrients = {}  # A dictionary to store nutrient values
        self.portion_amount=0
        self.portion_name = ""
        self.gram_weight=0
    def add_nutrient(self, name, amount,unit):
        self.nutrients[name] = (amount,unit)

    def add_fdc_id(self, id):
        self.fdc_id = int(id)

    def add_portion(self, portion_amount, portion_name, gram_weight):
        self.portion_amount = portion_amount
        self.portion_name=portion_name
        self.gram_weight = gram_weight



class FitaminApp(MDApp):
    checkboxes = {}  # Dictionary to store CheckBox instances
    foods = {}
    food_basket = {}
    #age=user_profile_data[3]
    recommended_intakes = {}  # Import recommendations from the Python file
    total_nutrients_consumed={}



############################################BUCKET LIST (FOODS CONSUMED) MODIFICATION############################################
    def create_entry_layout(self, food_name, grams, popup):
        label_text = f"{food_name}: {grams} grams"
        label = MDLabel(text=label_text)

        delete_button = MDIconButton(icon="delete", on_release=lambda instance, name=food_name: self.remove_food(name, popup))

        entry_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)  # Adjust height as needed
        entry_layout.add_widget(label)
        entry_layout.add_widget(delete_button)
        return entry_layout

    def remove_food(self, food_name, popup):
        if food_name in self.food_basket:
            del self.food_basket[food_name]
            self.refresh_popup_content(popup)

    def refresh_popup_content(self, popup):
        box_layout = popup.content
        box_layout.clear_widgets()

        for food_name, grams in self.food_basket.items():
            entry_layout = self.create_entry_layout(food_name, grams, popup)
            box_layout.add_widget(entry_layout)

        popup.size = (400, 50 * len(self.food_basket) + 100)

    def show_bucket_popup(self):
        popup = Popup(title='Bucket', size_hint=(None, None), size=(400, 400))
        box_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)

        for food_name, grams in self.food_basket.items():
            entry_layout = self.create_entry_layout(food_name, grams, popup)
            box_layout.add_widget(entry_layout)

        scrollview = ScrollView(size_hint=(1, 1))
        scrollview.add_widget(box_layout)

        popup.content = scrollview
        popup.open()

####################################PROFILE DATA SAVING#############################################################
    def save_user_profile_data(self,user_profile_data, filename='user_profile_data.json'):
        with open(filename, 'w') as file:
            json.dump(user_profile_data, file)

    def load_user_profile_data(self,filename='user_profile_data.json'):
        try:
            with open(filename, 'r') as file:
                loaded_data = json.load(file)

                # Fill in the loaded data to the existing user_profile_data
                for i, value in enumerate(loaded_data):
                    user_profile_data[i] = value

                print("User profile data loaded successfully.")
        except FileNotFoundError:
            print("No user profile data found. Starting with default data.")
#####################################################################################################################
#Making user add own food
    # def add_new_food(self):
    #     with open("new_food_data.json", "r") as file:
    #         food_data = json.load(file)
    #
    #     def save_data(instance):
    #         entry_widgets = instance
    #         # Extract food name
    #         food_name = entry_widgets["Food Name"].text
    #
    #         try:
    #             df = pd.read_csv("food_information_per_description_sorted.csv")
    #         except FileNotFoundError:
    #             # Create a new DataFrame if the file doesn't exist
    #             df = pd.DataFrame(columns=["description", "name", "amount"])
    #
    #             # Extract values from entry_widgets
    #         food_name = entry_widgets["Food Name"].text
    #
    #         for key, entry in entry_widgets.items():
    #             # Skip "Food Name" as it's already used
    #             if key == "Food Name":
    #                 continue
    #             elif key == "Weight of the food":
    #                 continue
    #             else:
    #             # Format the row and append to the DataFrame
    #                 nutrient_name = key
    #                 value = entry.text
    #                 row = {"description": food_name, "name": nutrient_name, "amount": value}
    #                 df = df.append(row, ignore_index=True)
    #
    #         # Save the DataFrame to the CSV file
    #         df.to_csv("food_information_per_description_sorted.csv", index=False, mode='a', header=not df.index.any())
    #
    #
    #         popup.dismiss()
    #
    #     entry_widgets = {}
    #
    #     layout = BoxLayout(orientation='vertical', spacing=40, size_hint_y=None)
    #     layout.bind(minimum_height=layout.setter('height'))
    #
    #     # Calculate the width based on the popup width
    #     layout_width = Window.width * 0.78   # Adjust the multiplier as needed
    #
    #     for key, value in food_data.items():
    #         label = Label(text=f"{key}:", size_hint_x=None, width=layout_width, height=50, size_hint_y=None,
    #                       text_size=(layout_width, None), halign='left', valign='top')
    #         entry = TextInput(text=str(value), size_hint_x=None, width=layout_width, height=50, size_hint_y=None,
    #                           multiline=False)
    #         entry_widgets[key] = entry
    #         layout.add_widget(label)
    #         layout.add_widget(entry)
    #
    #
    #
    #
    #
    #
    #     scrollview = ScrollView(size_hint=(1, None), size=(layout_width, Window.height * 0.65))
    #
    #     scrollview.add_widget(layout)
    #
    #     popup_content = BoxLayout(orientation='vertical')
    #     popup_content.add_widget(scrollview)
    #
    #     save_button = Button(text="Save", size_hint_x=None, width=Window.width * 0.78, height=50)
    #     save_button.bind(on_press=lambda instance: save_data(entry_widgets))
    #     popup_content.add_widget(save_button)
    #
    #     popup = Popup(title='Add New Food', content=popup_content, size_hint=(None, None),
    #                   size=(Window.width * 0.8, Window.height * 0.8))
    #
    #     popup.open()

    def calculate_remaining_intake_pop_up(self):
        width, height = Window.size[0] * 0.8, Window.size[1] * 0.4

        dolu_array = []

        remaining_intakes = self.calculate_remaining_intakes()
        remanining_intakes_popup = Popup(
            title='Remaining Intakes',
            size_hint=(None, None),
            size=(width, height),
            auto_dismiss=True
        )
        if remaining_intakes:

            print("Remaining Nutrient Intakes:")
            for nutrient_name, nutrient_amount in remaining_intakes.items():
                print(f"{nutrient_name}: {nutrient_amount}")
                label_name = Label(text=nutrient_name)
                label_amount = Label(text=str(nutrient_amount))
                # label_unit = Label(text=unit)

                # Create a BoxLayout to hold the labels horizontally
                nutrient_layout = BoxLayout(orientation='horizontal', spacing=10)
                nutrient_layout.add_widget(label_name)
                nutrient_layout.add_widget(label_amount)
                # nutrient_layout.add_widget(label_unit)

                # Add the BoxLayout to dolu_array
                dolu_array.append(nutrient_layout)



        else:
            print("No data found for remaining nutrient intakes.")

        content_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))
        for widget in dolu_array:
            content_layout.add_widget(widget)



        # content_layout.add_widget(writing_consumed_intakes)

        scroll_view = ScrollView(size_hint=(1, 1), size=(width, height))
        scroll_view.add_widget(content_layout)

        remanining_intakes_popup.content = scroll_view
        remanining_intakes_popup.open()







    def calculate_total_nutrients_consumed_pop_up(self):
        self.calculate_total_nutrients()
        width, height = Window.size[0] * 0.8, Window.size[1] * 0.4
        total_nutrients = self.total_nutrients_consumed
        dolu_array = []
        consumed_amount_popup = Popup(
            title='Total Intakes',
            size_hint=(None, None),
            size=(width, height),
            auto_dismiss=True
        )
        if total_nutrients:
            print("Total Nutrient Facts Consumed:")
            for nutrient_name, (nutrient_amount, unit) in total_nutrients.items():
                print(f"{nutrient_name}: {nutrient_amount} {unit}")
                label_name = Label(text=nutrient_name)
                label_amount = Label(text=str(nutrient_amount))
                label_unit = Label(text=unit)

                # Create a BoxLayout to hold the labels horizontally
                nutrient_layout = BoxLayout(orientation='horizontal', spacing=10)
                nutrient_layout.add_widget(label_name)
                nutrient_layout.add_widget(label_amount)
                nutrient_layout.add_widget(label_unit)

                # Add the BoxLayout to dolu_array
                dolu_array.append(nutrient_layout)

        else:
            print("No food items consumed yet.")


        content_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))
        for widget in dolu_array:
            content_layout.add_widget(widget)


        #content_layout.add_widget(writing_consumed_intakes)


        scroll_view = ScrollView(size_hint=(1,1),size=(width,height))
        scroll_view.add_widget(content_layout)


        consumed_amount_popup.content = scroll_view


        consumed_amount_popup.open()


    def calculate_remaining_intake(self, nutrient_name):
        consumed_intake = self.total_nutrients_consumed.get(nutrient_name, (0,))[0]
        recommended_intake = self.recommended_intakes.get(nutrient_name, 0)
        if recommended_intake is not None:

            remaining_intake = recommended_intake - consumed_intake
            return remaining_intake if remaining_intake > 0 else 0
        else:
            return 0

    def calculate_remaining_intakes(self):
        remaining_intakes = {}
        for nutrient_name in self.recommended_intakes:
            remaining_intake = self.calculate_remaining_intake(nutrient_name)
            if remaining_intake is not None:
                remaining_intakes[nutrient_name] = remaining_intake
        return remaining_intakes



    def confirm_quantity_to_food_basket(self, food_description, user_s_consumed_portions):
        food_instance = self.foods.get(food_description)
        data_portions=food_instance.portion_amount
        data_grams = food_instance.gram_weight
        if food_description in self.food_basket:
            self.food_basket[food_description] += user_s_consumed_portions*(data_grams/data_portions)
        else:
            self.food_basket[food_description] = user_s_consumed_portions*(data_grams/data_portions)

    def confirm_grams_to_food_basket(self, food_description, grams):
        if food_description in self.food_basket:
            self.food_basket[food_description] += grams
        else:
            self.food_basket[food_description] = grams

    def show_dual_input_popup(self, food_description):
        width, height = Window.size[0] * 0.8, Window.size[1] * 0.4
        dual_input_popup = Popup(
            title='Enter Amount',
            size_hint=(None, None),
            size=(width, height),
            auto_dismiss=True
        )

        # Get the Food object for the selected food description
        food_instance = self.foods.get(food_description)

        dual_input_widget = DualInput(food_instance)

        # Create a button to confirm the input type
        confirm_button = Button(text='Confirm Input Type')
        confirm_button.bind(on_release=lambda instance: confirm_input_type(instance))

        def confirm_input_type(instance):
            input_type = dual_input_widget.input_type.text.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
            if hasattr(food_instance, 'portion_name') and input_type == food_instance.portion_name and not input_type == "":
                self.show_quantity_popup(food_description, food_instance)
            elif input_type == 'grams':
                self.show_grams_popup(food_description)
            else:
                if food_instance.portion_name != "" :
                    print(f'Invalid input type. Please enter "{food_instance.portion_name}" or "grams".')
                else:
                    print(f'Invalid input type. Please enter "grams".')

            dual_input_popup.dismiss()

        # Add widgets to the popup content
        dual_input_popup.content = BoxLayout(orientation='vertical')
        dual_input_popup.content.add_widget(dual_input_widget)
        dual_input_popup.content.add_widget(confirm_button)

        dual_input_popup.open()

    def show_quantity_popup(self, food_description, food):
        quantity_popup = Popup(
            title=f'Enter Amount for {food_description}',
            size_hint=(None, None),
            size=(400, 200),
            auto_dismiss=False
        )

        quantity_input = QuantityInput(food)

        # Create a button to confirm the quantity input
        confirm_button = Button(text='Confirm')

        def confirm_quantity(instance):
            quantity = float(quantity_input.quantity_input.text)

            # You can now use the quantity as needed.
            self.confirm_quantity_to_food_basket(food_description, quantity)

            print(f'You ate {quantity} {food.portion_name} of {food.description}')
            self.calculate_total_nutrients()
            quantity_popup.dismiss()

        confirm_button.bind(on_release=confirm_quantity)

        # Add widgets to the popup content
        quantity_popup.content = BoxLayout(orientation='vertical')
        quantity_popup.content.add_widget(quantity_input)
        quantity_popup.content.add_widget(confirm_button)

        quantity_popup.open()

    def show_grams_popup(self, food_description):
        grams_popup = Popup(
            title=f'Enter Grams for {food_description}',
            size_hint=(None, None),
            size=(400, 200),
            auto_dismiss=False
        )

        grams_input = TextInput(hint_text='Enter Grams')

        # Create a button to confirm the grams input
        confirm_button = Button(text='Confirm Grams')

        def on_popup_dismiss(instance):
            self.calculate_average_percentage_consumed()

        def confirm_grams(instance):
            grams = float(grams_input.text)
            self.confirm_grams_to_food_basket(food_description, grams)  # Add to food_basket
            print(f'You consumed {grams} grams of {food_description}')

            self.calculate_total_nutrients()
            grams_popup.dismiss()


        confirm_button.bind(on_release=confirm_grams)
        grams_popup.bind(on_dismiss=on_popup_dismiss)

        # Add widgets to the grams popup content
        grams_popup.content = BoxLayout(orientation='vertical')
        grams_popup.content.add_widget(grams_input)
        grams_popup.content.add_widget(confirm_button)

        grams_popup.open()

    def calculate_total_nutrients(self):
        total_nutrients = {}  # Dictionary to store total nutrient values
        for food_description, amount in self.food_basket.items():
            food_instance = self.foods.get(food_description)

            if food_instance:
                for nutrient_name, (nutrient_amount, unit) in food_instance.nutrients.items():
                    # Create a key with both the nutrient name and unit
                    nutrient_key = f"{nutrient_name}"

                    if nutrient_key in total_nutrients:
                        existing_amount, existing_unit = total_nutrients[nutrient_key]
                        total_nutrients[nutrient_key] = (existing_amount + (nutrient_amount * amount) / 100, existing_unit)
                    else:
                        total_nutrients[nutrient_key] = ((nutrient_amount * amount)/100, unit)
        self.total_nutrients_consumed = total_nutrients
        return total_nutrients



    def change_screen(self, screen_name):
        self.root.current = screen_name

    def calculate_average_percentage_consumed(self):
        circular_progress_bar = self.root.get_screen(
            "calculator").ids.progressbar  # Assuming "progressbar" is the ID of your CircularProgressBar
        total_percentage = 0
        nutrient_count = 0
        total_nutrient_number = 36
        self.calculate_total_nutrients()

        for nutrient_name in self.recommended_intakes:
            if nutrient_name in self.total_nutrients_consumed:
                dri_value = int(self.recommended_intakes[nutrient_name])
                consumed_value_tuple = self.total_nutrients_consumed.get(nutrient_name, 0)
                consumed_value = int(consumed_value_tuple[0])

                if consumed_value >= dri_value:
                    percentage_consumed = 1.0
                else:
                    percentage_consumed = consumed_value / dri_value if dri_value > 0 else 0

                total_percentage += percentage_consumed
                #nutrient_count += 1

        # average_percentage = total_percentage / nutrient_count if nutrient_count > 0 else 0
        progress_value = min(round((total_percentage*100)/total_nutrient_number), 100)  # Round to integer and ensure it doesn't exceed 100



        def update_progress(dt):

            if circular_progress_bar.value < progress_value:
                circular_progress_bar.value +=1


            elif circular_progress_bar.value == progress_value:
                Clock.unschedule(update_progress)



        Clock.schedule_interval(update_progress, 0.1)  # Adjust the interval as needed

    #def animate(self, circular_progress_bar):
        #def update_progress(dt):
            #if circular_progress_bar.value < circular_progress_bar.max:
                #circular_progress_bar.value +=1
                #bu_kac=self.calculate_average_percentage_consumed()
                #print(bu_kac)
            #else:
              #  circular_progress_bar.value = circular_progress_bar.min

        #Clock.schedule_interval(update_progress, 0.05)




    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.load_user_profile_data()
        kullanici_adi = user_profile_data[0]
        self.root = Builder.load_string(navigation_helper)
        print(kullanici_adi)
        if not kullanici_adi:
            # User doesn't have a Kullanici Adi, navigate to WelcomeScreen

            self.root.current = 'welcome'
        else:
            # User has a Kullanici Adi, navigate to CalculatorScreen

            self.root.current = 'calculator'
          # Load the Kivy language string

        Liste = self.root.get_screen("calculator").ids.container
        circular_progress_bar = self.root.get_screen("calculator").ids.progressbar  # Assuming "progressbar" is the ID of your CircularProgressBar
        circular_progress_bar.value = 0





        # # Read the Excel sheets into pandas DataFrames
        # deneme_df = pd.read_csv(
        #     'deneme.csv')
        # food_nutrients_df = pd.read_csv(
        #     'food_nutrientt.csv')
        # nutrient_df = pd.read_csv(
        #     'nutrientt.csv')
        # # food portions calculation
        # food_portion_df = pd.read_csv(
        #     'food_portionn.csv')
        # measure_unit_df = pd.read_csv(
        #     'measure_unitt.csv')
        #
        # # Merge food_nutrients_df with nutrient_df to get nutrient names and units
        # merged_nutrient_df = pd.merge(food_nutrients_df, nutrient_df, left_on='nutrient_id', right_on='id')
        #
        # # Merge deneme_df with merged_nutrient_df on fdc_id
        # result_df = pd.merge(deneme_df, merged_nutrient_df, left_on='fdc_id', right_on='fdc_id')
        #
        # # Group by food and nutrient name to sum the amounts
        # grouped_df = result_df.groupby(['description', 'name', 'unit_name', 'fdc_id'])['amount'].sum().reset_index()
        #
        # food_portion_edited_df = food_portion_df.merge(measure_unit_df, on="measure_unit_id", how="left")
        # selected_columns = ["fdc_id", "measure_unit_id", "portion_name", "portion_amount", "gram_weight"]
        # food_portion_final_df = food_portion_edited_df[selected_columns]
        #
        # final_df = pd.merge(grouped_df, food_portion_final_df, left_on='fdc_id', right_on='fdc_id')

        final_df = pd.read_csv("food_information_per_description_sorted.csv")
        final_df["portion_amount"].fillna("", inplace=True)
        final_df["portion_name"].fillna("", inplace=True)
        final_df["gram_weight"].fillna("", inplace=True)

        for _, row in final_df.iterrows():
            description = row['description']
            name = row['name']
            amount = row['amount']
            unit = row['unit_name']
            fdc_id = row['fdc_id']
            portion_amount = row["portion_amount"]
            portion_name = row["portion_name"]
            gram_weight = row["gram_weight"]

            if description not in self.foods:
                self.foods[description] = Food(description)

            self.foods[description].add_nutrient(name, amount,unit)
            self.foods[description].add_fdc_id(fdc_id)
            self.foods[description].add_portion(portion_amount, portion_name, gram_weight)

        #for _, row in grouped_df.iterrows():
           # description = row['description']
          #  name = row['name']
          #  amount = row['amount']

          #  if description not in self.foods:
          #      self.foods[description] = Food(description)  # Pass fdc_id to Food constructor

          #  self.foods[description].add_nutrient(name, amount,unit)

        for food_description, food_instance in self.foods.items():
            item = TwoLineAvatarIconListItem(text=food_description, secondary_text="Additional Info")
            item.bind(
                on_release=lambda x, food_description=food_description: self.show_dual_input_popup(food_description))

            Liste.add_widget(item)


        return self.root

    def filter_items(self, text):
        """Filter and update the list based on the search criteria."""
        # Assuming you have a reference to the MDList
        container = self.root.get_screen("calculator").ids.container

        # Clear existing items in the MDList
        container.clear_widgets()

        # Add items based on the search criteria
        for food_description, food_instance in self.foods.items():
            if text.lower() in food_description.lower():
                item = TwoLineAvatarIconListItem(text=food_description, secondary_text="Additional Info")
                item.bind(
                    on_release=lambda x, food_description=food_description: self.show_dual_input_popup(
                        food_description))
                container.add_widget(item)


FitaminApp().run()
