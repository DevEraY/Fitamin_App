from kivymd.app import MDApp
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
import pandas as pd
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

class ProfileScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = MDApp.get_running_app()
        self.foods = app.foods
        self.food_basket = app.food_basket
        self.recommended_intakes = app.recommended_intakes






class EditProfileScreen(Screen):

    def gender_belirleme (self, selected_option):
        profile_screen = self.manager.get_screen('profile')
        if selected_option == 'Kadın':
            self.ids.pregnancy_situation.disabled = False
        else:
            self.ids.pregnancy_situation.disabled = True
            profile_screen.ids.Pregnancy.text = "Hamilelik durumu: "
            user_profile_data[10] = ""
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
        new_name = self.ids.edited_isim.text
        new_age = self.ids.edited_age.text
        new_height = self.ids.edited_height.text
        new_weight = self.ids.edited_weight.text


        profile_screen = self.manager.get_screen('profile')

        profile_screen.ids.isim.text = new_name
        profile_screen.ids.age.text = f'Age: {new_age}'
        profile_screen.ids.height.text = f'Height: {new_height}'
        profile_screen.ids.weight.text = f'Weight: {new_weight}'
        new_gender = user_profile_data[4]
        

        ##BMI da ekleyelim gelmişken
        BMI = int(new_weight) / ((int(new_height) / 100) ** 2)
        profile_screen.ids.BMI.text = f'BMI: {BMI}'


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



        print(user_profile_data)
        self.manager.current = 'profile'

class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass



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
    def add_nutrient(self, name, amount):
        self.nutrients[name] = amount

    def add_fdc_id(self, id):
        self.fdc_id = int(id)

    def add_portion(self,portion_amount,portion_name,gram_weight):
        self.portion_amount = portion_amount
        self.portion_name=portion_name
        self.gram_weight = gram_weight



class DemoApp(MDApp):
    checkboxes = {}  # Dictionary to store CheckBox instances
    foods = {}
    food_basket = {}
    recommended_intakes = element_values_males_19_30_y  # Import recommendations from the Python file

    def do_this(self):
        self.total_nutrients_consumed = self.calculate_total_nutrients()

        remaining_intakes = self.calculate_remaining_intakes()

        if remaining_intakes:
            print("Remaining Nutrient Intakes:")
            for nutrient_name, remaining_intake in remaining_intakes.items():
                print(f"{nutrient_name}: {remaining_intake} units")
        else:
            print("No data found for remaining nutrient intakes.")

    def do_anotherthing(self):
        total_nutrients = self.calculate_total_nutrients()
        if total_nutrients:
            print("Total Nutrient Facts Consumed:")
            for nutrient_name, nutrient_amount in total_nutrients.items():
                print(f"{nutrient_name}: {nutrient_amount} units")
        else:
            print("No food items consumed yet.")



    def calculate_remaining_intake(self, nutrient_name):
        if nutrient_name in self.recommended_intakes:
            remaining_intake = self.recommended_intakes[nutrient_name] - self.total_nutrients_consumed.get(
                nutrient_name, 0)
            return remaining_intake if remaining_intake > 0 else 0
        else:
            return None

    def calculate_remaining_intakes(self):
        remaining_intakes = {}
        for nutrient_name in self.recommended_intakes:
            remaining_intake = self.calculate_remaining_intake(nutrient_name)
            if remaining_intake is not None:
                remaining_intakes[nutrient_name] = remaining_intake
        return remaining_intakes



    def confirm_quantity_to_food_basket(self, food_description, quantity):
        if food_description in self.food_basket:
            self.food_basket[food_description] += quantity
        else:
            self.food_basket[food_description] = quantity

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
            auto_dismiss=False
        )

        # Get the Food object for the selected food description
        food_instance = self.foods.get(food_description)

        dual_input_widget = DualInput(food_instance)

        # Create a button to confirm the input type
        confirm_button = Button(text='Confirm Input Type')
        confirm_button.bind(on_release=lambda instance: confirm_input_type(instance))

        def confirm_input_type(instance):
            input_type = dual_input_widget.input_type.text.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
            if hasattr(food_instance, 'portion_name') and input_type == food_instance.portion_name.lower():
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

        def confirm_grams(instance):
            grams = float(grams_input.text)
            self.confirm_grams_to_food_basket(food_description, grams)  # Add to food_basket
            print(f'You consumed {grams} grams of {food_description}')
            grams_popup.dismiss()

        confirm_button.bind(on_release=confirm_grams)

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
                for nutrient_name, nutrient_amount in food_instance.nutrients.items():
                    if nutrient_name in total_nutrients:
                        total_nutrients[nutrient_name] += (nutrient_amount * amount)
                    else:
                        total_nutrients[nutrient_name] = (nutrient_amount * amount)
        return total_nutrients



    def change_screen(self, screen_name):
        self.root.current = screen_name







    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_string(navigation_helper)  # Load the Kivy language string
        Liste = self.root.get_screen("home").ids.container


        # Read the Excel sheets into pandas DataFrames
        deneme_df = pd.read_csv(
            'deneme.csv')
        food_nutrients_df = pd.read_csv(
            'food_nutrientt.csv')
        nutrient_df = pd.read_csv(
            'nutrientt.csv')
        # food portions calculation
        food_portion_df = pd.read_csv(
            'food_portionn.csv')
        measure_unit_df = pd.read_csv(
            'measure_unitt.csv')

        # Merge food_nutrients_df with nutrient_df to get nutrient names and units
        merged_nutrient_df = pd.merge(food_nutrients_df, nutrient_df, left_on='nutrient_id', right_on='id')

        # Merge deneme_df with merged_nutrient_df on fdc_id
        result_df = pd.merge(deneme_df, merged_nutrient_df, left_on='fdc_id', right_on='fdc_id')

        # Group by food and nutrient name to sum the amounts
        grouped_df = result_df.groupby(['description', 'name', 'unit_name', 'fdc_id'])['amount'].sum().reset_index()

        food_portion_edited_df = food_portion_df.merge(measure_unit_df, on="measure_unit_id", how="left")
        selected_columns = ["fdc_id", "measure_unit_id", "portion_name", "portion_amount", "gram_weight"]
        food_portion_final_df = food_portion_edited_df[selected_columns]

        final_df = pd.merge(grouped_df, food_portion_final_df, left_on='fdc_id', right_on='fdc_id')

        for _, row in final_df.iterrows():
            description = row['description']
            name = row['name']
            amount = row['amount']
            fdc_id = row['fdc_id']
            portion_amount = row["portion_amount"]
            portion_name = row["portion_name"]
            gram_weight = row["gram_weight"]

            if description not in self.foods:
                self.foods[description] = Food(description)

            self.foods[description].add_nutrient(name, amount)
            self.foods[description].add_fdc_id(fdc_id)
            self.foods[description].add_portion(portion_amount, portion_name, gram_weight)

        for _, row in grouped_df.iterrows():
            description = row['description']
            name = row['name']
            amount = row['amount']

            if description not in self.foods:
                self.foods[description] = Food(description)  # Pass fdc_id to Food constructor

            self.foods[description].add_nutrient(name, amount)

        for food_description, food_instance in self.foods.items():
            item = TwoLineAvatarIconListItem(text=food_description, secondary_text="Additional Info")
            item.bind(
                on_release=lambda x, food_description=food_description: self.show_dual_input_popup(food_description))

            Liste.add_widget(item)


        return self.root








DemoApp().run()
