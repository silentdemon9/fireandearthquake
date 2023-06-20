import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import pygame
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = "ACe5bccfa22d2f589e12b6e44e044c06c9"
auth_token = "978e6f6b273eeb04ac0deec69b37d58e"

# The phone number that you want to send the SMS message to
phone_number = "+639085620981"

# Initialize pygame
pygame.init()

# Load the sound files
fire_alarm_sound = pygame.mixer.Sound("Fire Drill Sound Effect.wav")
evacuation_alarm_sound = pygame.mixer.Sound("oearth.wav")

# Function to send an SMS message using Twilio
def send_sms(instance):
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=instance.sms_message_textbox.text, from_='+15076398221', to=phone_number)

# Function to play the fire alarm sound
def play_fire_alarm(instance):
    fire_alarm_sound.play()

# Function to play the evacuation alarm sound
def play_evacuation_alarm(instance):
    evacuation_alarm_sound.play()

# Function to stop the currently playing sound
def stop_alarm(instance):
    pygame.mixer.stop()

class FireAlarmApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create the header label
        header_label = Label(text="San Mateo Senior High School", font_size=40)
        layout.add_widget(header_label)

        # Create a layout for the fire and earthquake alarm buttons
        alarm_layout = BoxLayout()
        layout.add_widget(alarm_layout)

        # Create the "Fire Alarm" button
        fire_alarm_button = Button(text="Fire Alarm", size_hint=(0.5, 1), background_color=(1, 0, 0, 1), font_size=20)
        fire_alarm_button.bind(on_release=play_fire_alarm)
        alarm_layout.add_widget(fire_alarm_button)

        # Create the "Earthquake Alarm" button
        evacuation_alarm_button = Button(text="Earthquake Alarm", size_hint=(0.5, 1), background_color=(0, 1, 0, 1), font_size=20)
        evacuation_alarm_button.bind(on_release=play_evacuation_alarm)
        alarm_layout.add_widget(evacuation_alarm_button)

        # Create the SMS message text input
        self.sms_message_textbox = TextInput(hint_text="SMS Message", font_size=15)
        layout.add_widget(self.sms_message_textbox)

        # Create the "Send SMS" button
        sms_button = Button(text="Send SMS", font_size=15)
        sms_button.bind(on_release=send_sms)
        layout.add_widget(sms_button)

        # Create the "Stop Alarm" button
        stop_alarm_button = Button(text="Stop Alarm", font_size=15)
        stop_alarm_button.bind(on_release=stop_alarm)
        layout.add_widget(stop_alarm_button)

        return layout

if __name__ == '__main__':
    FireAlarmApp().run()
