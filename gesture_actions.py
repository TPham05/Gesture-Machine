import os
from music_control import open_spotify, play_previous_song, play_next_song, play_current_song
from volume_control import adjust_volume
import time
import pyautogui

# Cooldowns to ensure multiple commansd don't repeat too quickly
last_media_command_time = 0
MEDIA_COMMAND_COOLDOWN = 2.0 
last_scroll_command_time = 0
SCROLL_COMMAND_COOLDOWN = 0.4


def can_execute_media_command():
    global last_media_command_time
    now = time.time()
    if now - last_media_command_time > MEDIA_COMMAND_COOLDOWN:
        last_media_command_time = now
        return True
    return False

def can_execute_scroll_command():
    global last_scroll_command_time
    now = time.time()
    if now - last_scroll_command_time > SCROLL_COMMAND_COOLDOWN:
        last_scroll_command_time = now
        return True
    return False

def handle_gesture_action(gesture, volume_ctrl):
    if gesture == "tea":
        open_spotify()
    elif gesture == "play_music" and can_execute_media_command():
        play_current_song()
    elif gesture == "previous_song" and can_execute_media_command():
        play_previous_song()
    elif gesture == "next_song" and can_execute_media_command():
        play_next_song()
    elif gesture == "volume_up":
        adjust_volume("volume_up", volume_ctrl)
    elif gesture == "volume_down":
        adjust_volume("volume_down", volume_ctrl)
    elif gesture == "scroll_up" and can_execute_scroll_command():
        pyautogui.scroll(300)
    elif gesture == "scroll_down" and can_execute_scroll_command():
        pyautogui.scroll(-300)
    elif gesture == "y_sign" and can_execute_media_command():
        os.system("start chrome")
    elif gesture == "ok" and can_execute_media_command():
        pyautogui.press('enter')
    elif gesture == "l_sign":
        pyautogui.press('backspace')
   
